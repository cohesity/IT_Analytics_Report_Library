---
title: "NBU Active vs Expired Job Volume Summary"
report_id: 1138
rtd_name: "NBU Active vs Expired Job Volume Sumary.rtd"
description: "07/23/2015 NBU Active vs Expired Job Volume Summary"
problem_statement: "I need a visual representation of how much data I'm backing up in relation to when it's expiring, in order to see if I'm at a sustainable rate."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 01/20/2015\nWITH \nvar AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays,\nDECODE('${freeCombo2}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\nt1 AS (\nSELECT\nTRUNC(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) the_date,\nCOUNT(DISTINCT client_id) client_count,\nROUND(SUM(CASE WHEN expiration_date < sysdate THEN (kilobytes/div_by) ELSE 0 END),2) exp_job_volume,\nROUND(SUM(CASE WHEN expiration_date > sysdate THEN (kilobytes/div_by) ELSE 0 END),2) job_volume\nFROM apt_v_nbu_job_detail j, var\nWHERE j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND REGEXP_LIKE(j.policy_name,'${freeText1}')\nGROUP BY\nTRUNC(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY'))\n)\nSELECT\nTO_CHAR(the_date,'MM/DD/YY') the_date,\nTO_CHAR(the_date,'YYYYMMDD') sort_order,\nclient_count,\nexp_job_volume,\njob_volume\nFROM t1\nORDER BY 2"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
