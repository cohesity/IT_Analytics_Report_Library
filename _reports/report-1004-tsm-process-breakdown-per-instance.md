---
title: "TSM Process Breakdown per Instance"
report_id: 1004
rtd_name: "TSM Process Breakdown per Instance.rtd"
description: "TSM Process Breakdown per Instance"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 10/09/2011\n--Similar to TSM Process Count Breakdown except as a bar chart\nSELECT\ninstance_name,\ncount(job_id) job_count,\nsum(DECODE(job_type_name,'Expiration',1,0)) Expiration,\nsum(DECODE(job_type_name,'Full DB Backup',1,0)) Full_DB_Backup,\nsum(DECODE(job_type_name,'Incremental DB Backup',1,0)) Incr_DB_Backup,\nsum(DECODE(job_type_name,'Migration',1,0)) migration,\nsum(DECODE(job_type_name,'Move Media',1,0)) move_media,\nsum(DECODE(job_type_name,'Reclamation',1,0)) reclamation,\nsum(DECODE(job_type_name,'Storage Pool Backup',1,0)) stg_pool_backup\nFROM apt_v_tsm_process\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND server_id IN (${hosts})\nAND job_type_name IN ('Expiration','Full DB Backup','Incremental DB Backup','Migration','Move Media','Reclamation','Storage Pool Backup')\nGROUP BY instance_name\nORDER BY 2 DESC"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
