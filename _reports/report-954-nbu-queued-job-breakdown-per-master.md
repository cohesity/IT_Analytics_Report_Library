---
title: "NBU Queued Job Breakdown per Master"
report_id: 954
rtd_name: "NBU Queued Job Breakdown per Master.rtd"
description: "NBU Queued Job Breakdown per Master"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "SELECT \nj.server_id,\nj.master_host_name,\nCOUNT(j.job_id ) job_count,\nSUM(CASE WHEN (started_readwrite - start_date)*24*60 < 5 THEN 1 ELSE 0 END ) qjobl5_count,\nSUM(CASE WHEN (started_readwrite - start_date)*24*60 BETWEEN 5 AND 15 THEN 1 ELSE 0 END ) qjob515_count,\nSUM(CASE WHEN (started_readwrite - start_date)*24*60 >= 15 THEN 1 ELSE 0 END ) qjobg15_count\nFROM apt_v_nbu_job_detail j\nWHERE j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.job_type <> 105\nGROUP BY \nj.server_id,\nj.master_host_name\nORDER BY 3 DESC"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
