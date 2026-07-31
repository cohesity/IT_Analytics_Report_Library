---
title: "Backup Skipped File and Reason"
report_id: 1114
rtd_name: "Backup Skipped Files and Reason.rtd"
description: "Backup Skipped File and Reason"
problem_statement: "I need to see which files are being skipped and what is the reason they are skipped."
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/30/201\nSELECT\nj.product_type_name,\nj.server_name,\nj.client_name,\nCOUNT(j.job_id) skipped_file_count,\nREPLACE(aptStringConcat(DISTINCT sbf.skipped_filename),',','<br>') skipped_file,\nREPLACE(aptStringConcat(DISTINCT jml.message),',','<br>') reason\nFROM apt_v_job j, apt_v_skipped_backup_file sbf,apt_v_job_message_log jml\nWHERE j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.summary_status=1\nAND j.job_id = sbf.job_id\nAND j.job_id = jml.job_id\nGROUP BY \nj.product_type_name,\nj.server_name,\nj.client_name\nORDER BY 1,2,3"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
