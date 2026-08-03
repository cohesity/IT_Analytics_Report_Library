---
title: "NBU Job Count Breakdown Queue Time"
report_id: 917
rtd_name: "NBU Job Count Breakdown Queue Time.rtd"
description: "NBU Job Count Breakdown Queue Time"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 12/06/2012\nSELECT\nto_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'YYYY/MM/DD') the_date,\nSUM(CASE WHEN (started_readwrite - start_date)*24*60 < 5 THEN 1 ELSE 0 END ) qjobl5_count,\nSUM(CASE WHEN (started_readwrite - start_date)*24*60 BETWEEN 5 AND 15 THEN 1 ELSE 0 END ) qjob515_count,\nSUM(CASE WHEN (started_readwrite - start_date)*24*60 >= 15 THEN 1 ELSE 0 END ) qjob15_count\nFROM apt_v_nbu_job_detail\nWHERE client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY to_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'YYYY/MM/DD')\nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
