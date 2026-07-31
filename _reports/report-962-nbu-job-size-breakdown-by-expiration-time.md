---
title: "NBU Job Size Breakdown by Expiration Time"
report_id: 962
rtd_name: "NBU Job Size Breakdown by Expiration Time.rtd"
description: "NBU Job Size Breakdown by Expiration Time"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 12/27/2012\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo2}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM dual\n)\nSELECT to_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'YYYY/MM/DD') the_date,\nSUM(kilobytes)/var.div_by total_unexpired_data,\nROUND(SUM(CASE WHEN expiration_date BETWEEN start_date AND start_date+30 THEN kilobytes END)/var.div_by,2) less_than_30,\nROUND(SUM(CASE WHEN expiration_date BETWEEN start_date+30 AND start_date+90 THEN kilobytes END)/var.div_by,2) bt_30_and_90,\nROUND(SUM(CASE WHEN expiration_date BETWEEN start_date+90 AND start_date+365.25 THEN kilobytes END)/var.div_by,2) bt_90_and_1yr,\nROUND(SUM(CASE WHEN expiration_date BETWEEN start_date+365.25 AND start_date+1825 THEN kilobytes END)/var.div_by,2) bt_1_and_5yrs,\nROUND(SUM(CASE WHEN expiration_date > start_date+1825 THEN kilobytes END)/var.div_by,2) over_5yrs\nFROM apt_v_nbu_job_detail, var\nWHERE client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nAND expiration_date > start_date\nAND job_type <> 105\nGROUP BY to_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'YYYY/MM/DD')\nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
