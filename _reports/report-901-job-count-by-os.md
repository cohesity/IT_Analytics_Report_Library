---
title: "Job Count by OS"
report_id: 901
rtd_name: "Job Count by OS.rtd"
description: "Job Count by OS"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "\n\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nSELECT \nto_char(start_date, 'MM/DD/YY') job_date,\nNVL(SUM(CASE WHEN UPPER(os_version) LIKE '%WIN%' THEN 1 END),0) Windows,\nNVL(SUM(CASE WHEN UPPER(os_version) LIKE '%SOL%' THEN 1 END),0) Solaris,\nNVL(SUM(CASE WHEN UPPER(os_version) LIKE '%LIN%' THEN 1 END),0) Linux,\nNVL(SUM(CASE WHEN UPPER(os_version) LIKE '%AIX%' THEN 1 END),0) AIX,\nNVL(SUM(CASE WHEN UPPER(os_version) LIKE '%HP%' THEN 1 END),0) HPUX\nFROM\napt_v_job j, apt_v_server s\nWHERE j.client_id=s.server_id\nAND j.client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY to_char(start_date, 'MM/DD/YY')"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
