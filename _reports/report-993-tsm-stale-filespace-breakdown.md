---
title: "TSM Stale Filespace Breakdown"
report_id: 993
rtd_name: "TSM Stale Filespace Breakdown.rtd"
description: "TSM Stale Filespace Breakdown"
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
sql_query: "--TSM Stale Filespaces Breakdown\nWITH t1 as (\nSELECT f.node_name node,f.filespace_name filespace,\nmax(f.backup_finish_date) last_backup\nFROM apt_v_tsm_filespace f, apt_v_tsm_node n\nWHERE f.backup_finish_date BETWEEN ${startDate} AND ${endDate}\nAND f.node_id = n.node_id\nAND n.client_id in (${hosts})\nGROUP BY f.node_name,f.filespace_name\n),\nt2 as (\nSELECT node, filespace, last_backup,\n(sysdate - last_backup) days_since_last_backup\nFROM t1\nORDER BY node, filespace\n)\nSELECT\n0 ord,'Less Than 3 Days' unit, count(CASE WHEN days_since_last_backup < 3 THEN 1 END) metric\nFROM t2\nUNION\nSELECT\n1 ord, '3 to 14 Days' unit, count(CASE WHEN days_since_last_backup BETWEEN 3 AND 14 THEN 1 END) metric\nFROM t2\nUNION\nSELECT\n2 ord,'Greater Than 14 Days' unit, count(CASE WHEN days_since_last_backup > 14 THEN 1 END) metric\nFROM t2"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
