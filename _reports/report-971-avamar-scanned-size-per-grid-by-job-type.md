---
title: "Avamar Scanned Size Per Grid by Job Type"
report_id: 971
rtd_name: "Avamar Scanned Size Per Grid by Job Type.rtd"
description: "Avamar Scanned Size Per Grid by Job Type"
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
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Updated: 08/20/2012\nSELECT \ngsan_system_id, gsan_system_name,\nMAX(DECODE(job_type_name,'Scheduled Backup',scanned_kb,0)/1024/1024) sb_scanned_gb,\nMAX(DECODE(job_type_name,'Restore',scanned_kb,0)/1024/1024) r_scanned_gb,\nMAX(DECODE(job_type_name,'On-Demand Backup',scanned_kb,0)/1024/1024) od_scanned_gb,\nMAX(DECODE(job_type_name,'Replication Source',scanned_kb,0)/1024/1024) rs_scanned_gb,\nMAX(DECODE(job_type_name,'Replication Destination',scanned_kb,0)/1024/1024) rd_scanned_gb\nFROM apt_v_avm_activities\nWHERE \nscanned_kb > 0\nAND recorded_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY \ngsan_system_id, gsan_system_name"
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
