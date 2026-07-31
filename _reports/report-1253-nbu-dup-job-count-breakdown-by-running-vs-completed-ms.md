---
title: "NBU Dup Job Count Breakdown by Running vs Completed MS"
report_id: 1253
rtd_name: "NBU Dup Job Count Breakdown by Running vs Complete MS.rtd"
description: "NBU Dup Job Count Breakdown by Running vs Completed MS"
problem_statement: "Show me what my backlog is of SLP Duplication"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 11/15/2018\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo2}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT\nTO_CHAR(trunc(start_date,DECODE('${freeCombo1}','Hour','HH','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY HH24') the_date,\nTO_CHAR(trunc(start_date,DECODE('${freeCombo1}','Hour','HH','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24') sort_order,\nROUND(SUM(DECODE(vendor_state,3,1,0)),2) complete,\nROUND(SUM(DECODE(vendor_state,1,1,0)),2) running\nFROM apt_v_nbu_duplication_job, var\nWHERE server_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY to_char(TRUNC(start_date,DECODE('${freeCombo1}','Hour','HH','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY HH24'),\nTO_CHAR(trunc(start_date,DECODE('${freeCombo1}','Hour','HH','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24')\nORDER BY 2"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
