---
title: "NetApp SnapVault Daily GB Transferred per Filer Heat Map"
report_id: 1025
rtd_name: "NetApp SnapVault Daily GB Transferred per Filer Heat Map.rtd"
description: "NetApp SnapVault Daily GB Transferred per Filer Heat Map"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 06/14/2012\nWITH t1 AS (\nSELECT\nto_char(nss.mirror_timestamp,'MM/DD/YYYY')  the_date,\nnsc.source_system_name||' >> '||nsc.destination_system_name source_dest,\nsum(nss.last_transfer_size_kb/1024/1024) last_transfer_size_gb\nFROM\naps_v_nap_snapvault_config nsc,\naps_v_nap_snapvault_status nss\nWHERE\nnsc.nap_snapvault_config_id = nss.nap_snapvault_config_id (+)\nAND nss.mirror_timestamp BETWEEN ${startDate} AND ${endDate}\nAND to_char(nss.mirror_state) = 'snapvaulted'\nGROUP BY to_char(nss.mirror_timestamp,'MM/DD/YYYY'),\nnsc.source_system_name||' >> '||nsc.destination_system_name\n),\n\nt2 AS (\nSELECT source_dest,\navg(last_transfer_size_gb) avg_transfer_size_gb\nFROM t1\nGROUP BY source_dest\n)\nSELECT\nt1.the_date,\nt1.source_dest,\nCASE WHEN t1.last_transfer_size_gb > t2.avg_transfer_size_gb+(t2.avg_transfer_size_gb*(${freeCombo1}/100)) THEN '<font color=red>'||to_char(t1.last_transfer_size_gb,'999,999,999.99')||'</font>'\nELSE to_char(t1.last_transfer_size_gb,'999,999,999.99') END last_transfer_size_gb\nFROM t1,t2\nWHERE\nt1.source_dest = t2.source_dest\nORDER by 1 DESC"
has_explanation: false
products: [{"slug": "capacity-manager-netapp-reports-7-mode", "name": "NetApp Reports (7 Mode)"}]
categories: []
product_slugs: ["capacity-manager-netapp-reports-7-mode"]
category_slugs: []
---
