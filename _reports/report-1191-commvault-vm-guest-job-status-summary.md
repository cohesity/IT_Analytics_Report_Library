---
title: "CommVault VM Guest Job Status Summary"
report_id: 1191
rtd_name: "CommVault VM Guest Job Status Summary.rtd"
description: "CommVault VM Guest Job Status Summary"
problem_statement: ""
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 06/28/2017\nSELECT \nTRUNC(vm_start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) the_date,\nSUM(CASE WHEN INSTR(NVL(r.description,'xxx'),'Warning') = 0 AND vm_status = 0 THEN 1 ELSE 0 END) success,\nSUM(CASE WHEN INSTR(r.description,'Warning') > 0 AND vm_status = 0 THEN 1 ELSE 0 END) warning,\nSUM(CASE WHEN vm_status > 0 THEN 1 ELSE 0 END) failure\nFROM apt_v_cmv_job_vm jv, apt_v_cmv_reason r\nWHERE\njv.client_id IN (${hosts})\nAND vm_start_date BETWEEN ${startDate} AND ${endDate}\nAND jv.vm_failed_reason_id = r.cmv_reason_code (+) \nGROUP BY \nTRUNC(vm_start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY'))"
has_explanation: false
products: [{"slug": "backup-manager-commvault", "name": "CommVault"}]
categories: []
product_slugs: ["backup-manager-commvault"]
category_slugs: []
---
