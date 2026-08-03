---
title: "Avamar Client DeDupe Report"
report_id: 968
rtd_name: "Avamar Client DeDupe Report.rtd"
description: "Avamar Client DeDupe Report"
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
sql_query: "SELECT\nj.client_id,\nj.client_name,\nROUND(MAX(scanned_kb/1024/1024),2) scanned,\nROUND(SUM(modified_not_sent_kb/1024/1024),2) modified_not_sent_gb,\nROUND(SUM(modified_sent_kb/1024/1024),2) modified_sent_gb,\n(SUM(modified_sent_kb)/(SUM(modified_not_sent_kb)+.0001))*100 dedupe_pct,\n(SUM(modified_sent_kb)/(SUM(modified_not_sent_kb)+.0001)) pct_dedupe\nFROM \napt_v_avm_activities aa, apt_v_job j\nWHERE \naa.job_id = j.job_id\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.client_id IN (${hosts})\nGROUP BY\nj.client_id, \nj.client_name\nORDER BY 7 DESC"
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
