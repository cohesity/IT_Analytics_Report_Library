---
title: "OSSV Status Distribution"
report_id: 1024
rtd_name: "OSSV Status Distribution.rtd"
description: "OSSV Status Distribution"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 01/28/2012\nWITH \nt1 AS (\nSELECT \nnss.summary_status status_name,\ncount(*) status_count\nFROM \naps_v_nap_snapvault_config nsc,\naps_v_nap_snapvault_status nss\nWHERE\nnsc.nap_snapvault_config_id = nss.nap_snapvault_config_id (+)\nAND nss.mirror_timestamp BETWEEN ${startDate} AND ${endDate}\nAND nsc.source_system_name LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\nAND nsc.source_storage_system_id IS NULL\nGROUP BY nss.summary_status\n)\nSELECT\nDECODE(status_name,0,'Successful',1,'Partial',2,'Failed') status_name,\nstatus_count\nFROM t1"
has_explanation: false
products: [{"slug": "capacity-manager-netapp-reports-7-mode", "name": "NetApp Reports (7 Mode)"}]
categories: []
product_slugs: ["capacity-manager-netapp-reports-7-mode"]
category_slugs: []
---
