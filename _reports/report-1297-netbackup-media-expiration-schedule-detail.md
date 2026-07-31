---
title: "NetBackup Media Expiration Schedule Detail"
report_id: 1297
rtd_name: "NetBackup Media Expiration Schedule Detail.rtd"
description: "Drilldown from the bar for a specific date to obtain complete details about the Tape Media such as the barcode, serial number, Used KB etc"
problem_statement: "Shows details from mimic of OpsCenter report \u201cMedia Expiration Schedule\u201d"
author: "mandar.kulkarni@veritas.com"
modified_date: "2024-08-26"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "-- drilldown report\n\nSELECT ntmd.tape_media_id,\n       s.hostname server,\n       ntmd.media_name Media,\n       ntmd.vendor_media_type_name Media_Type,\n       ntmd.bar_code,\n       ntd.serial_number,\n       ntmd.volume_pool_name,\n       ntmd.written_kilobytes Used_Kb,\n       ntd.robot_drive_index robot_number,\n       ntd.drive_name robot_name,\n       ntmd.expiration_date     \nFROM apt_v_nbu_tape_media_detail ntmd,\n     apt_v_nbu_tape_drive ntd,\n     apt_v_server s\nWHERE ntmd.vendor_media_type_name= '${the_media_type}'\n  AND ntmd.server_id=ntd.controlling_server_id (+)\n  AND ntmd.last_mounted_drive_id=ntd.drive_id (+)\n  AND ntmd.server_id=s.server_id  (+)\n  AND TO_CHAR(TRUNC(ntmd.expiration_date),'${the_date_format}') = '${the_date_char}'\n  AND ntmd.expiration_date BETWEEN ${startDate} AND ${endDate}\nORDER BY ntmd.expiration_date"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: [{"slug": "opscenter-reports", "name": "OpsCenter Reports"}]
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: ["opscenter-reports"]
---
