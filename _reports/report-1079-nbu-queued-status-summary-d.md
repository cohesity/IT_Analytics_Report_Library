---
title: "NBU Queued Status Summary.D"
report_id: 1079
rtd_name: "NBU Queued Status Summary.D.rtd"
description: "NBU Queued Status Summary"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 11/14/2012\n--NOTE: This is a drilldown report only and will not run standalone\n--The templateName is NBUQueuedStatusSummary.D\nWITH \nt1 AS (\nSELECT\nserver_id,\nmaster_host_name,\nclient_id,\nclient_host_name,\npolicy_name,\nschedule_name,\nstart_date,\nstarted_readwrite,\n(started_readwrite - start_date)*24*60 queue_min,\nfinish_date,\nvendor_status,\nCASE \nWHEN (started_readwrite - start_date)*24*60 < 5 THEN 'l5'\nWHEN (started_readwrite - start_date)*24*60 BETWEEN 5 AND 15 THEN '515'\nWHEN (started_readwrite - start_date)*24*60 >= 15 THEN 'g15' \nEND q_code\nFROM apt_v_nbu_job_detail\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND server_id = ${theServerID}\nAND summary_status IS NOT NULL\n)\nSELECT * \nFROM t1 \nWHERE \nq_code = '${theQueueCode}'"
has_explanation: false
products: []
categories: []
product_slugs: []
category_slugs: []
---
