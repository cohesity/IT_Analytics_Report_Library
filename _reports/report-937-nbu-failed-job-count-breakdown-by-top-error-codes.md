---
title: "NBU Failed Job Count Breakdown by Top Error Codes"
report_id: 937
rtd_name: "NBU Failed Job Count Breakdown by Top Error Codes.rtd"
description: "NBU Failed Job Count Breakdown by Top Error Codes"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 12/06/2012\nSELECT\nto_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'YYYY/MM/DD') the_date,\nSUM(CASE WHEN vendor_status = 2074 THEN 1 ELSE 0 END ) e2074,\nSUM(CASE WHEN vendor_status = 84 THEN 1 ELSE 0 END ) e84,\nSUM(CASE WHEN vendor_status = 96 THEN 1 ELSE 0 END ) e96,\nSUM(CASE WHEN vendor_status = 196 THEN 1 ELSE 0 END ) e196,\nSUM(CASE WHEN vendor_status = 830 THEN 1 ELSE 0 END ) e830,\nSUM(CASE WHEN vendor_status = 58 THEN 1 ELSE 0 END ) e58,\nSUM(CASE WHEN vendor_status = 156 THEN 1 ELSE 0 END ) e156,\nSUM(CASE WHEN vendor_status = 83 THEN 1 ELSE 0 END ) e83,\nSUM(CASE WHEN vendor_status = 50 THEN 1 ELSE 0 END ) e50,\nSUM(CASE WHEN vendor_status = 6 THEN 1 ELSE 0 END ) e6,\nSUM(CASE WHEN vendor_status = 13 THEN 1 ELSE 0 END ) e13,\nSUM(CASE WHEN vendor_status NOT IN (204,84,96,196,830,58,156,83,50,6,13) THEN 1 ELSE 0 END ) all_others\nFROM apt_v_nbu_job_detail\nWHERE client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nAND vendor_status NOT IN (0,1,150)\nGROUP BY to_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'YYYY/MM/DD')\nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
