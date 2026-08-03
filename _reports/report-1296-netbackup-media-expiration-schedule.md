---
title: "NetBackup Media Expiration Schedule"
report_id: 1296
rtd_name: "NetBackup Media Expiration Schedule.rtd"
description: "Report gives a graphical representation of the expiration schedule for Tape media in a stacked bar chart format."
problem_statement: "Please provide a report that mimics the OpsCenter Report 'Media Expiration Schedule'"
author: "mandar.kulkarni@veritas.com"
modified_date: "2024-08-26"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "SELECT expiration_date,\n       DECODE('${freeCombo1}','Day','mm-dd-yyyy','Week','WW','Month','MM-YYYY','Quarter','Q','Year','YYYY') date_format,\n       media_type,\n       media_count \nFROM\n(\nSELECT TO_CHAR(TRUNC(ntmd.expiration_date),DECODE('${freeCombo1}','Day','mm-dd-yyyy','Week','WW','Month','MM-YYYY','Quarter','Q','Year','YYYY')) expiration_date,\n       ntmd.vendor_media_type_name media_type,\n       COUNT(*) media_count\nFROM apt_v_nbu_tape_media_detail ntmd\nWHERE ntmd.expiration_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY TO_CHAR(TRUNC(ntmd.expiration_date),DECODE('${freeCombo1}','Day','mm-dd-yyyy','Week','WW','Month','MM-YYYY','Quarter','Q','Year','YYYY')),\n         ntmd.vendor_media_type_name\nORDER BY expiration_date asc\n)"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: [{"slug": "opscenter-reports", "name": "OpsCenter Reports"}]
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: ["opscenter-reports"]
---
