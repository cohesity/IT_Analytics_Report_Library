---
title: "TSM Process Count Breakdown per Instance"
report_id: 979
rtd_name: "TSM Process Count Breakdown per Instance.rtd"
description: "TSM Process Count Breakdown per Instance"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/09/2011\nSELECT\nto_char(${startDate},'MM/DD/YYYY') start_date_char,\nto_char(${startDate},'HH24') start_hour_char,\nto_char(${endDate},'MM/DD/YYYY') finish_date_char,\nto_char(${endDate},'HH24') finish_hour_char,\nserver_id,\nserver_name,\nsum(DECODE(summary_status,2,1)) failed_count,\nsum(DECODE(job_type_name,'Expiration',1,0)) Expiration,\nsum(DECODE(job_type_name,'Full DB Backup',1,0)) Full_DB_Backup,\nsum(DECODE(job_type_name,'Incremental DB Backup',1,0)) Incr_DB_Backup,\nsum(DECODE(job_type_name,'Migration',1,0)) migration,\nsum(DECODE(job_type_name,'Move Media',1,0)) move_media,\nsum(DECODE(job_type_name,'Reclamation',1,0)) reclamation,\nsum(DECODE(job_type_name,'Storage Pool Backup',1,0)) stg_pool_backup,\nsum(DECODE(job_type_name,'Incr Backup',1,0)) Incr_Backup,\nsum(DECODE(job_type_name,'Archive',1,0)) Archive,\nsum(DECODE(job_type_name,'Command',1,0)) Command,\nsum(DECODE(job_type_name,'Restore',1,0)) restore,\nsum(DECODE(job_type_name,'Selective Backup',1,0)) selective_backup\nFROM apt_v_job\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND client_id IN (${hosts})\nGROUP BY server_id,server_name"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
