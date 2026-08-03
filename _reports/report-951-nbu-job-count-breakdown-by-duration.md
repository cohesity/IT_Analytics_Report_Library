---
title: "NBU Job Count Breakdown by Duration"
report_id: 951
rtd_name: "NBU Job Count Breakdown by Duration.rtd"
description: "NBU Job Count Breakdown by Duration"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 12/06/2012\nSELECT\nto_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'YYYY/MM/DD') the_date,\nSUM(CASE WHEN duration_secs/60/60 < 1 THEN 1 ELSE 0 END ) job_l1_count,\nSUM(CASE WHEN duration_secs/60/60 BETWEEN 1 AND 12 THEN 1 ELSE 0 END ) job_112_count,\nSUM(CASE WHEN duration_secs/60/60 BETWEEN 12 AND 24 THEN 1 ELSE 0 END ) job_1224_count,\nSUM(CASE WHEN duration_secs/60/60 >= 24 THEN 1 ELSE 0 END ) job_g24_count\nFROM apt_v_nbu_job_detail\nWHERE client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY to_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'YYYY/MM/DD')\nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
