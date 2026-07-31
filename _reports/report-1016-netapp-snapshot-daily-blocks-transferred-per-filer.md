---
title: "NetApp Snapshot Daily Blocks Transferred per Filer"
report_id: 1016
rtd_name: "NetApp Snapshot Daily Blocks Transferred per Filer.rtd"
description: "NetApp Snapshot Daily Blocks Transferred per Filer"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "WITH \nt1 AS (\nSELECT \nto_char(ns.access_time,'MM/DD/YYYY') the_date, \nns.system_name NetApp_filer, \nsum(ns.total) total_blocks\nFROM aps_v_nap_snapshot ns\nWHERE ns.access_time BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nto_char(ns.access_time,'MM/DD/YYYY'), ns.system_name\n), \nt2 AS (\nSELECT netapp_filer, \navg(total_blocks) avg_blocks\nFROM t1\nGROUP BY netapp_filer\n)\nSELECT\nt1.the_date,\nt1.netapp_filer,\nCASE WHEN t1.total_blocks > t2.avg_blocks+(t2.avg_blocks*(${freeCombo1}/100)) THEN '<font color=red>'||to_char(t1.total_blocks,'999,999,999,999')||'</font>'\nELSE to_char(t1.total_blocks,'999,999,999,999') END total_blocks\nFROM t1,t2\nWHERE\nt1.netapp_filer = t2.netapp_filer\nORDER by 1 DESC"
has_explanation: false
products: [{"slug": "capacity-manager-netapp-reports-7-mode", "name": "NetApp Reports (7 Mode)"}]
categories: []
product_slugs: ["capacity-manager-netapp-reports-7-mode"]
category_slugs: []
---
