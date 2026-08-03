---
title: "NBU Most Mounted Media"
report_id: 939
rtd_name: "NBU Most Mounted Media.rtd"
description: "NBU Most Mounted Media"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "WITH t1 AS (\nSELECT s.hostname master_server,\ntape_media_id,media_name barcode, nbr_of_mounts\nFROM apt_v_nbu_tape_media tm,apt_v_server s \nWHERE tm.server_id IN (${hosts})\nAND tm.server_id = s.server_id\nORDER BY tm.nbr_of_mounts DESC\n)\nSELECT master_server,tape_media_id, barcode, nbr_of_mounts\nFROM t1 WHERE ROWNUM <= ${freeCombo1}"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
