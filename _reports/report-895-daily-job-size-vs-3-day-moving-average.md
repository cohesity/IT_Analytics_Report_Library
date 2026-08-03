---
title: "Daily Job Size vs 3 Day Moving Average"
report_id: 895
rtd_name: "Daily Job Size vs 3 Day Moving Average.rtd"
description: "Daily Job Size vs 3 Day Moving Average"
problem_statement: ""
author: "rich.rose@aptare.com\r\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 11/26/2012\nWITH t1 AS (\nSELECT\nTRUNC(start_date,'DD') the_date,\nserver_name,\nROUND(SUM(kilobytes/1024/1024),2) job_size\nFROM apt_v_job\nWHERE\nclient_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY trunc(start_date,'DD'), server_name\nORDER BY 1,2\n)\nSELECT \nthe_date,server_name,job_size,\navg(job_size) OVER (PARTITION BY server_name ORDER BY the_date ROWS BETWEEN ${freeCombo1} PRECEDING AND 0 FOLLOWING) moving_average FROM t1\nORDER BY 2,1 DESC"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
