---
title: "NBU Client Job Stats Heat Map"
report_id: 1160
rtd_name: "NBU Client Job Stats Heat Map.rtd"
description: "NBU Client Job Stats Heat Map"
problem_statement: "I need to see if my clients backup job sizes are varying x Percent"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 03/31/2015\nWITH \nVAR AS (\nSELECT\nDECODE('${freeCombo2}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by,\nDECODE('${freeCombo3}',\n'10%',10,'20%',20,'30%',30,'40%',40,'50%',50,'60%',60,'70%',70,'80%',80,'90%',90,'100%',100,'200%',200,'300%',300) threshold\nFROM apt_v_dual\n),\nt1 AS (\nSELECT\nTRUNC(j.start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) the_date,\nj.client_id,\nj.client_host_name,\nSUM(j.kilobytes/div_by) the_size\nFROM\napt_v_nbu_job_detail j, var\nWHERE j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.client_id IN (${hosts})\nAND j.job_type_name LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\nGROUP BY\nTRUNC(j.start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),\nj.client_id,\nj.client_host_name\nORDER BY 1,2\n),\nt2 AS (--Rank them\nSELECT\nthe_date,\nclient_id,\nclient_host_name,\nthe_size,\nAVG(the_size) OVER (PARTITION BY client_id, client_host_name) avg_size,\nRATIO_TO_REPORT(the_size) OVER (PARTITION BY client_id, client_host_name) rr_size,\nDENSE_RANK() OVER (PARTITION BY client_id, client_host_name ORDER BY the_size DESC) dr_size\nFROM t1\nORDER BY 1,2\n),\nt3 AS (--Assign colors to the rankings\nSELECT\nthe_date,\nclient_id,\nclient_host_name,\nROUND(the_size,2) the_size,\nROUND(rr_size*100,2) rr_size,\nROUND(dr_size,2) dr_size,\nROUND(avg_size,2) avg_size,\nABS(ROUND(((avg_size-the_size)/DECODE(avg_size,0,null,avg_size))*100,2)) avg_pct_of_size,\nCASE \nWHEN the_size >= avg_size  THEN 'Greater Than'\nWHEN the_size <= avg_size  THEN 'Less Than'\nEND the_comparison,\nCASE\nWHEN ABS(ROUND(((avg_size-the_size)/DECODE(avg_size,0,null,avg_size))*100,2)) >= threshold\nTHEN '<b>*</b>' \nELSE ' ' END alert,\nCASE\nWHEN dr_size = 1 THEN '#610B0B'\nWHEN dr_size = 2 THEN '#8A0808'\nWHEN dr_size = 3 THEN '#B40404'\n--WHEN dr_size = 4 THEN '#DF0101'\n--WHEN dr_size = 5 THEN '#FE2E2E'\n--WHEN dr_size = 6 THEN '#F78181'\n--WHEN dr_size = 7 THEN '#F6CECE'\n--WHEN dr_size = 8 THEN '#FBEFEF'\nELSE '#FBEFEF'\nEND cell_color,\nCASE\nWHEN dr_size = 1 THEN '#FBEFEF'\nWHEN dr_size = 2 THEN '#F6CECE'\nWHEN dr_size = 3 THEN '#F78181'\n--WHEN dr_size = 4 THEN '#FE2E2E'\n--WHEN dr_size = 5 THEN '#DF0101'\n--WHEN dr_size = 6 THEN '#B40404'\n--WHEN dr_size = 7 THEN '#8A0808'\n--WHEN dr_size = 8 THEN '#610B0B'\nELSE '#610B0B'\nEND font_color\nFROM t2, var\nORDER BY 1,2\n)\nSELECT\nthe_date,\nclient_id,\nclient_host_name,\nthe_size,\nrr_size,\ndr_size,\navg_size,\navg_pct_of_size,\nthe_comparison,\n'<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><td style=background-color:'||cell_color||' align=right>'||'<font color='||font_color||'>'||alert||the_size||'</font></td></table>' heatmap\nFROM t3\nORDER BY 1,2"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
