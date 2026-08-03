---
title: "TSM Backup Count Breakdown per Instance"
report_id: 989
rtd_name: "TSM Backup Count Breakdown per Instance.rtd"
description: "TSM Backup Count Breakdown per Instance"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/09/2011\nSELECT\ninstance_name,\ncount(job_id) job_count,\nsum(DECODE(job_type_name,'Incr Backup',1,0)) Incr_Backup,\nsum(DECODE(job_type_name,'Archive',1,0)) Archive,\nsum(DECODE(job_type_name,'Command',1,0)) Command,\nsum(DECODE(job_type_name,'Restore',1,0)) restore,\nsum(DECODE(job_type_name,'Selective Backup',1,0)) selective_backup\nFROM apt_v_tsm_job\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND server_id IN (${hosts})\nAND job_type_name IN ('Incr Backup','Archive','Command','Restore','Selective Backup')\nGROUP BY instance_name\nORDER BY 2 DESC"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
