---
title: "Backup Hogs"
report_id: 1143
rtd_name: "Backup Hogs.rtd"
description: "Backup Hogs"
problem_statement: "I need to identify which clients are backing up the most data so I can make decisions on how this will impact the overall backup infrastructure."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/30/2015\nWITH \nt1 AS (--get the largest backup\nSELECT /*+ NO_MERGE  */\nj.server_id,\nj.server_name,\nj.client_id,\nj.client_name,\nMAX(j.kilobytes) max_kb\nFROM \napt_v_job j\nWHERE j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\n--AND j.server_id <> j.client_id\nAND j.summary_status IN (0,1)\nGROUP BY \nj.server_id,\nj.server_name,\nj.client_id,\nj.client_name\nHAVING \nMAX(j.kilobytes) >= ${freeText1} * 1024 * 1024\n)--Now get the job Id for that backup\nSELECT /*+ NO_MERGE(t1) */\nj.product_type_name,\nj.job_id,\nt1.server_id,\nt1.server_name,\nt1.client_id,\nt1.client_name,\nj.finish_date,\nj.job_type_name,\nj.nbr_of_files,\nt1.max_kb\nFROM \napt_v_job j, t1\nWHERE j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\n--AND j.server_id <> j.client_id\nAND j.client_id = t1.client_id\nAND j.server_id = t1.server_id\nAND j.summary_status IN (0,1)\nAND j.kilobytes = t1.max_kb\nORDER BY max_kb DESC"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
