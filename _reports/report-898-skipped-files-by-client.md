---
title: "Skipped Files by Client"
report_id: 898
rtd_name: "Skipped Files by Client.rtd"
description: "Skipped Files by Client"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 04/30/2012\nSELECT\nj.server_name,\nj.client_name,\nREPLACE(aptStringConcat(sbf.skipped_filename),',','<br>') skipped_file,\nCOUNT(j.job_id) skipped_file_count\nFROM apt_v_job j, apt_v_skipped_backup_file sbf\nWHERE j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.job_id = sbf.job_id\nAND j.summary_status = 1\nAND sbf.skipped_filename IS NOT NULL\nGROUP BY \nj.server_name,\nj.client_name"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
