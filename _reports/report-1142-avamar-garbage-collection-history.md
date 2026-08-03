---
title: "Avamar Garbage Collection History"
report_id: 1142
rtd_name: "Avamar Garbage Collection History.rtd"
description: "Avamar Garbage Collection History"
problem_statement: "I need to see how much data is being reclaimed in my Avamar grid by garbage collection tasks so I can plan for growth."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/29/2015\nWITH \nvar AS (\nSELECT\n'${freeCombo2}' unit,\nDECODE('${freeCombo2}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT\nunit,\nto_char(trunc(end_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY HH24:MI') the_date,\nto_char(trunc(end_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24MI') sort_order,\nROUND(SUM(elapsed_minutes/60/60),2) elapsed_hrs,--actually stored in seconds\nROUND(SUM((recovered_bytes)/div_by),2) recovered --actually stored in KB\nFROM apt_v_avm_gc_status gc, apt_v_server s, var\nWHERE \nend_date BETWEEN ${startDate} AND ${endDate}\nAND s.server_id = gc.master_server_id\nAND s.display_name LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\nGROUP BY\nunit,\nto_char(trunc(end_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY HH24:MI'),\nto_char(trunc(end_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24MI')\nORDER BY 3"
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
