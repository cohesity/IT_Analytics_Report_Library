---
title: "NBU Disk Pool Used Available Capacity"
report_id: 1156
rtd_name: "NBU Disk Pool Used Available Capacity.rtd"
description: "NBU Disk Pool Used Available Capacity"
problem_statement: ""
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
sql_query: "WITH\nvar AS (\nSELECT\n'${freeCombo2}' unit,\nDECODE('${freeCombo2}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\nt1 AS (\nSELECT\nto_char(trunc(vl.log_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY') the_date,\nto_char(trunc(vl.log_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24MI') sort_order,\ns.display_name||'-'||vl.disk_volume_name server_volume, \nROUND(MAX(vl.free_space_kb/div_by),2) free_space,\nROUND(MAX((vl.total_capacity_kb - vl.free_space_kb)/div_by),2) used_space\nFROM apt_v_nbu_disk_volume_log vl, apt_v_server s, var\nWHERE\nvl.management_server_id IN (${hosts})\nAND vl.management_server_id = s.server_id\nAND vl.log_date BETWEEN ${startDate} AND  ${endDate}\nAND s.display_name||'-'||vl.disk_volume_name = '${queryCombo1}'\nGROUP BY \nto_char(trunc(vl.log_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY'),\nto_char(trunc(vl.log_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24MI'),\ns.display_name||'-'||vl.disk_volume_name\n)\nSELECT\nthe_date,\nsort_order,\nserver_volume,\nfree_space,\nused_space\nFROM t1, var\nORDER BY 2 DESC,3"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
