---
title: "OSSV Daily Status Detail"
report_id: 1018
rtd_name: "OSSV Daily Status Detail.rtd"
description: "OSSV Daily Status Detail"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 01/28/2012\nWITH \nt1 AS (\nSELECT \nto_char(nss.mirror_timestamp,'MM/DD/YY') the_date,\nnsc.source_system_name  ||' '||nsc.source_volume_name source,\nmax(nss.summary_status) status,\nsum(DECODE(nss.summary_status,2,1,0)) failed,\nsum(DECODE(nss.summary_status,1,1,0)) partial,\nsum(DECODE(nss.summary_status,0,1,0)) success\nFROM \naps_v_nap_snapvault_config nsc,\naps_v_nap_snapvault_status nss\nWHERE\nnsc.nap_snapvault_config_id = nss.nap_snapvault_config_id (+)\nAND nss.mirror_timestamp BETWEEN ${startDate} AND ${endDate}\nAND nsc.source_system_name LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\nAND nsc.source_storage_system_id IS NULL\nGROUP BY\nto_char(nss.mirror_timestamp,'MM/DD/YY'),\nnsc.source_system_name ||' '|| nsc.source_volume_name\n)\nSELECT\nthe_date, lower(source) source,\nDECODE(status,null,'white',0,'green',1,'yellow',2,'red') status,\nfailed, \npartial, \nsuccess\nFROM t1\nORDER BY the_date DESC"
has_explanation: false
products: [{"slug": "capacity-manager-netapp-reports-7-mode", "name": "NetApp Reports (7 Mode)"}]
categories: []
product_slugs: ["capacity-manager-netapp-reports-7-mode"]
category_slugs: []
---
