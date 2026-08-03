---
title: "NBU Image Action Distribution"
report_id: 1153
rtd_name: "NBU Image Action Distribution.rtd"
description: "NBU Image Action Distribution"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 08/27/2015\nWITH \nvar AS (\nSELECT\n'${freeCombo2}' unit,\nDECODE('${freeCombo2}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT\nto_char(trunc(l.trans_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY HH24:MI') the_date,\nto_char(trunc(l.trans_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24MI') sort_order,\nvar.unit unit,\nROUND(SUM(j.kilobytes/div_by),2) total_size,\nROUND(SUM(DECODE(l.trans_type,'D',j.kilobytes,0)/div_by),2) dup_size,\nROUND(SUM(DECODE(l.trans_type,'E',j.kilobytes,0)/div_by),2) exp_size,\nROUND(SUM(DECODE(l.trans_type,'P',j.kilobytes,0)/div_by),2) pch_size,\nCOUNT(l.backup_id) total_count,\nCOUNT(DECODE(l.trans_type,'D',l.backup_id,0)) dup_count,\nCOUNT(DECODE(l.trans_type,'E',l.backup_id,0)) exp_count,\nCOUNT(DECODE(l.trans_type,'P',l.backup_id,0)) pch_count\nFROM apt_v_nbu_image_log l,  apt_v_nbu_job j, var \nWHERE l.client_id IN (${hosts})\nAND j.client_id IN (${hosts})\nAND l.job_id = j.job_id\nAND l.trans_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nto_char(trunc(l.trans_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY HH24:MI'),\nto_char(trunc(l.trans_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24MI'),\nvar.unit\nORDER BY 2"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
