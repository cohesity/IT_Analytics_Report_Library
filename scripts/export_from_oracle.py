"""
Exports the published report library from Oracle (RTD_REPORT + product/category
xrefs) into export/reports.json plus per-report content files under
export/content/{report_id}/.

Uses python-oracledb in thin mode, so no Oracle Instant Client install is needed.

Connection - two ways to reach the DB:

1. You already open your own SSH tunnel (e.g. `ssh -L 1521:dbhost:1521 user@bastion`)
   before running this. Just set:
     ORACLE_USER, ORACLE_PASSWORD, ORACLE_DSN=127.0.0.1:1521/SERVICE_NAME
   SSH_HOST must be unset for this path.

2. Let this script open (and close) the SSH tunnel itself, so one command does
   the whole job - useful since the full export can run long enough that
   babysitting a second terminal gets old. Set:
     ORACLE_USER, ORACLE_PASSWORD, ORACLE_SERVICE_NAME
     SSH_HOST, SSH_USER, and either SSH_KEY_FILE or SSH_PASSWORD
     ORACLE_REMOTE_HOST (Oracle's host as seen FROM the SSH host, default localhost)
     ORACLE_REMOTE_PORT (default 1521), ORACLE_LOCAL_PORT (default 1521)
   Do not set ORACLE_DSN in this case - it's derived from the tunnel.

Run: python export_from_oracle.py
"""
import contextlib
import json
import os
import re
import sys

import oracledb

EXPORT_DIR = os.path.join(os.path.dirname(__file__), "..", "export")
CONTENT_DIR = os.path.join(EXPORT_DIR, "content")

METADATA_QUERY = """
SELECT
  r.REPORT_ID,
  r.REPORT_NAME,
  r.REPORT_DESC,
  r.LONG_DESC,
  r.PROBLEM_STMT,
  r.TAGS,
  r.AUTHOR,
  TO_CHAR(r.CREATE_DT, 'YYYY-MM-DD') CREATE_DATE,
  TO_CHAR(r.MODIFY_DT, 'YYYY-MM-DD') MODIFY_DATE,
  r.RTD_NAME,
  r.HAS_VIDEO,
  r.VIDEO_URL,
  r.RTD_DOWNLOAD_COUNT,
  (SELECT LISTAGG(p.PRODUCT || ' / ' || p.COMPONENT, ';;') WITHIN GROUP (ORDER BY p.DISPLAY_ORDER)
     FROM RTD_PRODUCT_XREF px JOIN RTD_PRODUCT p ON p.PRODUCT_ID = px.PRODUCT_ID
     WHERE px.REPORT_ID = r.REPORT_ID) AS PRODUCTS,
  (SELECT LISTAGG(c.CATEGORY, ';;') WITHIN GROUP (ORDER BY c.CATEGORY_ID)
     FROM RTD_CATEGORY_XREF cx JOIN RTD_CATEGORY c ON c.CATEGORY_ID = cx.CATEGORY_ID
     WHERE cx.REPORT_ID = r.REPORT_ID) AS CATEGORIES
FROM RTD_REPORT r
WHERE r.GA = 'Y'
ORDER BY r.REPORT_NAME
"""

CONTENT_QUERY = """
SELECT RTD_FILE, ZIP_FILE, INPUT_NAME, INPUT_FILE, OUTPUT_IMAGE, OUTPUT_TYPE
FROM RTD_REPORT
WHERE REPORT_ID = :report_id
"""

PLACEHOLDER_THUMBNAILS = {"blankreportdesigner.png"}


def safe_filename(name):
    return re.sub(r'[<>:"/\\|?*]', "_", name).strip() or "template.rtd"


def lob_to_str(value):
    return value.read() if hasattr(value, "read") else value


def lob_to_bytes(value):
    if value is None:
        return None
    return value.read() if hasattr(value, "read") else value


def fetch_metadata(cursor):
    cursor.execute(METADATA_QUERY)
    columns = [c[0].lower() for c in cursor.description]
    reports = []
    for row in cursor:
        record = dict(zip(columns, row))
        for key in ("report_desc", "long_desc", "problem_stmt", "products", "categories"):
            record[key] = lob_to_str(record.get(key))
        record["products"] = (record["products"] or "").split(";;") if record["products"] else []
        record["categories"] = (record["categories"] or "").split(";;") if record["categories"] else []
        record["has_video"] = record["has_video"] == "Y"
        reports.append(record)
    return reports


def fetch_and_write_content(cursor, report_id, rtd_name):
    cursor.execute(CONTENT_QUERY, report_id=report_id)
    row = cursor.fetchone()
    if row is None:
        print(f"  ! no RTD_REPORT row for {report_id}", file=sys.stderr)
        return False

    rtd_file, zip_file, input_name, input_file, output_image, output_type = row
    out_dir = os.path.join(CONTENT_DIR, str(report_id))
    os.makedirs(out_dir, exist_ok=True)

    rtd_text = lob_to_str(rtd_file)
    if rtd_text:
        with open(os.path.join(out_dir, safe_filename(rtd_name)), "w", encoding="utf-8") as f:
            f.write(rtd_text)

    # ZIP_FILE is misnamed in the source schema - it's the pre-rendered sample
    # output HTML, not an actual zip archive.
    sample_html = lob_to_str(zip_file)
    if sample_html:
        with open(os.path.join(out_dir, "sample.html"), "w", encoding="utf-8") as f:
            f.write(sample_html)
    else:
        # A handful of legacy reports (mostly 2024 NBU additions) never got a
        # ZIP_FILE HTML render - their sample output was only ever captured as
        # a static image snapshot in OUTPUT_IMAGE. Wrap it in a bare sample.html
        # so it displays through the same iframe/link as every other report.
        image_bytes = lob_to_bytes(output_image)
        if image_bytes:
            ext = (output_type or "image/png").split("/")[-1]
            image_filename = f"output.{ext}"
            with open(os.path.join(out_dir, image_filename), "wb") as f:
                f.write(image_bytes)
            with open(os.path.join(out_dir, "sample.html"), "w", encoding="utf-8") as f:
                f.write(
                    "<html><body style=\"margin:0\">"
                    f"<img src=\"{image_filename}\" style=\"max-width:100%\">"
                    "</body></html>"
                )

    thumb_bytes = lob_to_bytes(input_file)
    if thumb_bytes and (input_name or "").lower() not in PLACEHOLDER_THUMBNAILS:
        with open(os.path.join(out_dir, "thumbnail.png"), "wb") as f:
            f.write(thumb_bytes)

    return True


@contextlib.contextmanager
def oracle_connection():
    """Yields a live oracledb connection, opening an SSH tunnel first if
    SSH_HOST is set (see module docstring for the two supported setups)."""
    user = os.environ["ORACLE_USER"]
    password = os.environ["ORACLE_PASSWORD"]

    ssh_host = os.environ.get("SSH_HOST")
    if not ssh_host:
        dsn = os.environ["ORACLE_DSN"]
        with oracledb.connect(user=user, password=password, dsn=dsn) as conn:
            yield conn
        return

    # sshtunnel 0.4.0 (2021) unconditionally references paramiko.DSSKey when
    # building its key-type table, even for password auth. Modern paramiko
    # dropped DSSKey (DSA keys are deprecated/insecure) so the import crashes
    # without this shim. Not actually used for password auth or non-DSA keys.
    import paramiko
    if not hasattr(paramiko, "DSSKey"):
        paramiko.DSSKey = paramiko.RSAKey

    from sshtunnel import SSHTunnelForwarder

    ssh_port = int(os.environ.get("SSH_PORT", "22"))
    ssh_user = os.environ["SSH_USER"]
    ssh_key_file = os.environ.get("SSH_KEY_FILE")
    ssh_password = os.environ.get("SSH_PASSWORD")
    oracle_remote_host = os.environ.get("ORACLE_REMOTE_HOST", "localhost")
    oracle_remote_port = int(os.environ.get("ORACLE_REMOTE_PORT", "1521"))
    oracle_service_name = os.environ["ORACLE_SERVICE_NAME"]
    local_port = int(os.environ.get("ORACLE_LOCAL_PORT", "1521"))

    if not ssh_key_file and not ssh_password:
        raise SystemExit("Set SSH_KEY_FILE or SSH_PASSWORD to authenticate the SSH tunnel.")

    print(f"Opening SSH tunnel via {ssh_user}@{ssh_host}:{ssh_port} "
          f"-> {oracle_remote_host}:{oracle_remote_port} ...")
    with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_pkey=ssh_key_file,
        ssh_password=ssh_password,
        remote_bind_address=(oracle_remote_host, oracle_remote_port),
        local_bind_address=("127.0.0.1", local_port),
    ) as tunnel:
        dsn = f"127.0.0.1:{tunnel.local_bind_port}/{oracle_service_name}"
        print(f"Tunnel up on local port {tunnel.local_bind_port}. Connecting to Oracle...")
        with oracledb.connect(user=user, password=password, dsn=dsn) as conn:
            yield conn
        print("Closing SSH tunnel...")


def main():
    os.makedirs(EXPORT_DIR, exist_ok=True)
    os.makedirs(CONTENT_DIR, exist_ok=True)

    with oracle_connection() as conn:
        with conn.cursor() as cursor:
            print("Fetching report metadata...")
            reports = fetch_metadata(cursor)
            print(f"  {len(reports)} published reports")

            print("Fetching per-report content (template, sample, thumbnail)...")
            for i, r in enumerate(reports, 1):
                fetch_and_write_content(cursor, r["report_id"], r["rtd_name"])
                if i % 50 == 0:
                    print(f"  {i}/{len(reports)}")

    with open(os.path.join(EXPORT_DIR, "reports.json"), "w", encoding="utf-8") as f:
        json.dump(reports, f, indent=2, default=str)

    print(f"Done. Wrote {os.path.join(EXPORT_DIR, 'reports.json')} and content/ for {len(reports)} reports.")


if __name__ == "__main__":
    main()
