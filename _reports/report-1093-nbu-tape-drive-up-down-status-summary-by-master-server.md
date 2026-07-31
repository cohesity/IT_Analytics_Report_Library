---
title: "NBU Tape Drive Up-Down Status Summary by Master Server"
report_id: 1093
rtd_name: "NBU Tape Drive Up-Down Status Summary by Master Server.rtd"
description: "NBU Tape Drive Up-Down Status Summary by Master Server"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/04/2012\nWITH t1 AS (\nSELECT\ntl.master_host_name,\nCOUNT(DISTINCT tl.library_id) libraries,\nSUM(CASE WHEN td.drive_status_name IN ('Down','Unknown') THEN 1 ELSE 0 END) down_count,\nSUM(CASE WHEN td.drive_status_name IN ('Up','Up OPR Mode') THEN 1 ELSE 0 END) up_count\nFROM apt_v_nbu_tape_drive td, apt_v_nbu_tape_library tl\nWHERE td.library_id = tl.library_id\nAND tl.server_id IN (${hosts})\nGROUP BY tl.master_host_name\nHAVING count(td.drive_id) > 0\n)\nSELECT \nmaster_host_name,\nlibraries,\n(up_count+down_count) total_drives,\nup_count,\ndown_count,\nround(down_count/(up_count+down_count+.0001)*100,2) down_pct,\nCASE WHEN round(down_count/(up_count+down_count+.0001)*100,2) > ${freeCombo1} THEN 'red' ELSE 'green' END down_dot\nFROM t1\nORDER BY 6 DESC"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
