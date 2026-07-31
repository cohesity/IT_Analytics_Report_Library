---
title: "TSM Node Filespace Last Backup"
report_id: 1002
rtd_name: "TSM Node Filespace Last Backup.rtd"
description: "TSM Node Filespace Last Backup"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com    Date: 07/07/2011\n--\n--\nWITH t1 as (\nSELECT f.node_name node,f.filespace_name filespace,\nmax(f.backup_finish_date) last_backup,\nmax(f.capacity_kbytes/1024/1024) last_size_gb\nFROM apt_v_tsm_filespace f, apt_v_tsm_node n\nWHERE f.backup_finish_date BETWEEN ${startDate} AND ${endDate}\nAND f.node_id = n.node_id\nAND n.client_id in (${hosts})\nGROUP BY f.node_name,f.filespace_name\n)\nSELECT node, filespace, last_backup, last_size_gb,\n(sysdate - last_backup) days_since_last_backup\nFROM t1\nWHERE (sysdate - last_backup) > ${freeCombo1} \nORDER BY node, filespace"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
