---
title: "NBU Image Action Distribution Report"
report_id: 1152
rtd_name: "NBU Image Action Distribution Report.rtd"
description: "NBU Image Action Distribution Report"
problem_statement: ""
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 08/27/2015\nWITH \nvar AS (\nSELECT\n'${freeCombo2}' unit,\nDECODE('${freeCombo2}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT\nj.master_host_name,\nto_char(trunc(l.trans_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY') the_date,\nto_char(trunc(l.trans_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24MI') sort_order,\nvar.unit unit,\nROUND(SUM(j.kilobytes/div_by),2) total_size,\nCOUNT(l.backup_id) total_count,\nSUM(DECODE(l.trans_type,'D',1,0)) dup_count,\nROUND(SUM(DECODE(l.trans_type,'D',j.kilobytes,0)/div_by),2) dup_size,\nSUM(DECODE(l.trans_type,'E',1,0)) exp_count,\nROUND(SUM(DECODE(l.trans_type,'E',j.kilobytes,0)/div_by),2) exp_size,\nSUM(DECODE(l.trans_type,'P',1,0)) pch_count,\nROUND(SUM(DECODE(l.trans_type,'P',j.kilobytes,0)/div_by),2) pch_size\nFROM apt_v_nbu_image_log l,  apt_v_nbu_job j, var \nWHERE l.client_id IN (${hosts})\nAND j.client_id IN (${hosts})\nAND l.job_id = j.job_id\nAND l.trans_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nj.master_host_name,\nto_char(trunc(l.trans_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY'),\nto_char(trunc(l.trans_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24MI'),\nvar.unit\nORDER BY 1,3 DESC\n"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
