---
title: "TSM Stale Filespaces"
report_id: 1157
rtd_name: "TSM Stale Filespaces.rtd"
description: "TSM Stale Filespaces"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "WITH t1 as (\nSELECT f.node_name node,f.filespace_name filespace,\nmax(f.backup_finish_date) last_backup\nFROM apt_v_tsm_filespace f, apt_v_tsm_node n\nWHERE f.backup_finish_date BETWEEN ${startDate} AND ${endDate}\nAND f.node_id = n.node_id\nAND n.client_id in (${hosts})\nGROUP BY f.node_name,f.filespace_name\n)\nSELECT node, filespace, last_backup,\n(sysdate - last_backup) days_since_last_backup\nFROM t1\nWHERE (sysdate - last_backup) > ${freeCombo1} \nORDER BY node, filespace"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
