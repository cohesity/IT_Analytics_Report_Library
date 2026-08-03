---
title: "What if Client Count Increased"
report_id: 894
rtd_name: "What if Client Count Increased.rtd"
description: "What if Client Count Increased"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 05/25/2012\nWITH t1 as (\nSELECT\nDECODE('${freeCombo1}','100%',1,'90%',.90,'80%',.80,'70%',.70,'60%',.60,'50%',.50,'40%',.40,'30%',.30,'20%',.20,'10%',.10) pct_increase\nFROM dual\n)\nSELECT  to_char(finish_date,'DD-MM-YYYY') Backup_Date,\ncount(DISTINCT client_id) client_count,\nsum(kilobytes/1024/1024) volume_gb,\nsum(kilobytes/1024/1024) * t1.pct_increase what_if_gb,\n${freeText1} max_client\nFROM apt_v_job,t1\nwhere client_id in (${hosts})\nAND finish_date BETWEEN ${startDate} AND ${endDate}\ngroup BY to_char(finish_date,'DD-MM-YYYY')"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
