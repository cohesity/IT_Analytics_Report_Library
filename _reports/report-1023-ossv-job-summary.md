---
title: "OSSV Job Summary"
report_id: 1023
rtd_name: "OSSV Job Summary.rtd"
description: "OSSV Job Summary"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 06/14/2012\nSELECT \nnss.mirror_timestamp the_date,\nnsc.source_system_name,\nnsc.source_volume_name,\nDECODE(nss.summary_status,0,'Successful',1,'Partial',2,'Failed') status_name,\nDECODE(summary_status,null,'white',0,'green',1,'yellow',2,'red') status_color,\nnss.mirror_state,\nnss.mirror_status,\nnss.transfer_progress,\nnsc.destination_system_name,\nnsc.destination_qtree_name,\nrtd.secsToHoursMinSecs(nss.lag_time) lag_time,\nnss.last_transfer_size_kb/1024/1024 last_transfer_size_gb\nFROM \naps_v_nap_snapvault_config nsc,\naps_v_nap_snapvault_status nss\nWHERE\nnsc.nap_snapvault_config_id = nss.nap_snapvault_config_id (+)\nAND nss.mirror_timestamp BETWEEN ${startDate} AND ${endDate}\nAND nsc.source_system_name LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\nAND nsc.destination_system_name LIKE DECODE('${queryCombo2}',' All','%','${queryCombo2}')\nAND nsc.source_storage_system_id IS NULL\nAND to_char(nss.summary_status) LIKE DECODE('${freeCombo1}','Successful','0','Partial','1','Failed','2','All','%')"
has_explanation: false
products: [{"slug": "capacity-manager-netapp-reports-7-mode", "name": "NetApp Reports (7 Mode)"}]
categories: []
product_slugs: ["capacity-manager-netapp-reports-7-mode"]
category_slugs: []
---
