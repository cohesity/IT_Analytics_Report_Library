---
title: "NBU Mission Control by Master"
report_id: 965
rtd_name: "NBU Mission Control by Master.rtd"
description: "NBU Mission Control by Master"
problem_statement: "Displays the general health of a large backup environment by representing the overall backup job success rate in the form of KPI's"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/11/2012\nWITH t1 AS (\nSELECT\nto_char(start_date,'MM/DD/YY') the_date,\nmaster_host_name,\ncount(job_id) total_jobs,\nsum(DECODE(summary_status,0,1,0)) success,\nsum(DECODE(summary_status,1,1,0)) partial,\nsum(DECODE(summary_status,2,1,0)) failed\nFROM apt_v_nbu_job\nWHERE client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nAND summary_status IS NOT NULL\nGROUP BY to_char(start_date,'MM/DD/YY'),master_host_name\n)\nSELECT \nthe_date,\nmaster_host_name,\nsuccess,\npartial,\nfailed,\nCASE \nWHEN\nround(success/total_jobs*100,2) < ${freeCombo1} THEN 'red'\nWHEN\nround(success/total_jobs*100,2) BETWEEN ${freeCombo1} AND ${freeCombo2} THEN 'yellow'\nWHEN\nround(success/total_jobs*100,2) > ${freeCombo2} THEN 'green'\nELSE 'white'\nEND success_pct,\nround(success/total_jobs*100,2) pct_success\nFROM t1"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
