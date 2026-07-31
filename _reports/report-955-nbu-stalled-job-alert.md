---
title: "NBU Stalled Job Alert"
report_id: 955
rtd_name: "NBU Stalled Job Alert.rtd"
description: "NBU Stalled Job Alert"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nSELECT\njob_id,\nmaster_host_name,media_host_name,client_host_name,\nvendor_state_name,vendor_status_name,\nstart_date,\n(sysdate-start_date)*1440 job_duration_min,\nrtd.secsToHoursMinSecs((sysdate-start_date)*86400) job_duration,\nstarted_readwrite,\n(sysdate - nvl(started_readwrite,sysdate))*1440 rw_duration_min,\nrtd.secsToHoursMinSecs((sysdate - nvl(started_readwrite,sysdate))*86400) rw_duration,\n(kilobytes/1024) mb_written,\n((sysdate - nvl(started_readwrite,sysdate))*86400)/((kilobytes/1024)+.0001) mb_sec\nFROM apt_v_nbu_job_try\nWHERE client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nAND is_active = 'Y'"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
