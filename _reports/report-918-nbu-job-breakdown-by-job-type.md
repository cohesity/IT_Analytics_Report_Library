---
title: "NBU Job Breakdown by Job Type"
report_id: 918
rtd_name: "NBU Job Breakdown by Job Type.rtd"
description: "NBU Job Breakdown by Job Type"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 05/07/2012\nSELECT\nto_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'MM/DD/YY') the_date,\nSUM(DECODE(job_type,101,1,0)) AS \"Full\",\nSUM(DECODE(job_type,102,1,0)) AS \"Incremental\",\nSUM(DECODE(job_type,103,1,0)) AS \"Catalog\",\nSUM(DECODE(job_type,104,1,0)) AS \"Archive\",\nSUM(DECODE(job_type,105,1,0)) AS \"Restore\",\nSUM(DECODE(job_type,106,1,0)) AS \"Verify\",\nSUM(DECODE(job_type,107,1,0)) AS \"Duplication\",\nSUM(DECODE(job_type,108,1,0)) AS \"Import\",\nSUM(DECODE(job_type,109,1,0)) AS \"Vault\",\nSUM(DECODE(job_type,110,1,0)) AS \"Label\",\nSUM(DECODE(job_type,111,1,0)) AS \"Media Erase\",\nSUM(DECODE(job_type,112,1,0)) AS \"Application\",\nSUM(DECODE(job_type,113,1,0)) AS \"Tape Request\",\nSUM(DECODE(job_type,114,1,0)) AS \"Drive Cleaning\",\nSUM(DECODE(job_type,115,1,0)) AS \"Optical Format\",\nSUM(DECODE(job_type,116,1,0)) AS \"Inventory Library\",\nSUM(DECODE(job_type,117,1,0)) AS \"DB Recover\",\nSUM(DECODE(job_type,118,1,0)) AS \"Media Listing\",\nSUM(DECODE(job_type,119,1,0)) AS \"Job Qualification\"\nFROM apt_v_nbu_job\nWHERE client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY to_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'MM/DD/YY')"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
