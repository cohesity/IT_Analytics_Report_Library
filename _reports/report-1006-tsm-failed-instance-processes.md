---
title: "TSM Failed Instance Processes"
report_id: 1006
rtd_name: "TSM Failed Instance Processes.rtd"
description: "TSM Failed Instance Processes"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 10/03/2011\nWITH \nvar AS (\nSELECT\n--User Defined Threshholds\n1 AS yellow_threshold,\n2 AS red_threshold\nFROM apt_v_dual\n),\nq1 AS (\nSELECT\nto_char(${startDate},'MM/DD/YYYY') start_date_char,\nto_char(${startDate},'HH24') start_hour_char,\nto_char(${endDate},'MM/DD/YYYY') finish_date_char,\nto_char(${endDate},'HH24') finish_hour_char,\nserver_id,\nserver_name,\nsum(DECODE(job_type_name,'Expiration',1,0)) Expiration,\nsum(DECODE(job_type_name,'Full DB Backup',1,0)) Full_DB_Backup,\nsum(DECODE(job_type_name,'Incremental DB Backup',1,0)) Incr_DB_Backup,\nsum(DECODE(job_type_name,'Migration',1,0)) migration,\nsum(DECODE(job_type_name,'Move Media',1,0)) move_media,\nsum(DECODE(job_type_name,'Reclamation',1,0)) reclamation,\nsum(DECODE(job_type_name,'Storage Pool Backup',1,0)) stg_pool_backup,\nsum(DECODE(job_type_name,'Incr Backup',1,0)) Incr_Backup,\nsum(DECODE(job_type_name,'Archive',1,0)) Archive,\nsum(DECODE(job_type_name,'Command',1,0)) Command,\nsum(DECODE(job_type_name,'Restore',1,0)) restore,\nsum(DECODE(job_type_name,'Selective Backup',1,0)) selective_backup\nFROM apt_v_job\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND server_id IN (${hosts})\nAND summary_status = 2\nGROUP BY server_id,server_name\n)\nSELECT\nstart_date_char,\nstart_hour_char,\nfinish_date_char,\nfinish_hour_char,\nserver_id,\nserver_name,\nexpiration,\nCASE WHEN expiration >= var.red_threshold THEN 'red' WHEN expiration >= var.yellow_threshold THEN 'yellow'  ELSE 'green' END expiration_dot,\nfull_DB_Backup,\nCASE WHEN full_DB_Backup >= var.red_threshold THEN 'red' WHEN full_DB_Backup >= var.yellow_threshold THEN 'yellow'  ELSE 'green' END full_DB_Backup_dot,\nincr_DB_Backup,\nCASE WHEN incr_DB_Backup >= var.red_threshold THEN 'red' WHEN incr_DB_Backup >= var.yellow_threshold THEN 'yellow' ELSE 'green' END incr_DB_Backup_dot,\nmigration,\nCASE WHEN migration >= var.red_threshold THEN 'red' WHEN migration >= var.yellow_threshold THEN 'yellow' ELSE 'green' END migration_dot,\nmove_media,\nCASE WHEN move_media >= var.red_threshold THEN 'red' WHEN move_media >= var.yellow_threshold THEN 'yellow' ELSE 'green' END move_media_dot,\nreclamation,\nCASE WHEN reclamation >= var.red_threshold THEN 'red' WHEN reclamation >= var.yellow_threshold THEN 'yellow' ELSE 'green' END reclamation_dot,\nstg_pool_backup,\nCASE WHEN stg_pool_backup >= var.red_threshold THEN 'red' WHEN stg_pool_backup >= var.yellow_threshold THEN 'yellow' ELSE 'green' END stg_pool_backup_dot,\nincr_backup,\nCASE WHEN incr_backup >= var.red_threshold THEN 'red' WHEN incr_backup >= var.yellow_threshold THEN 'yellow' ELSE 'green' END incr_backup_dot,\nArchive,\nCASE WHEN archive >= var.red_threshold THEN 'red' WHEN archive >= var.yellow_threshold THEN 'yellow' ELSE 'green' END archive_dot,\ncommand,\nCASE WHEN command >= var.red_threshold THEN 'red' WHEN command >= var.yellow_threshold THEN 'yellow' ELSE 'green' END command_dot,\nrestore,\nCASE WHEN restore >= var.red_threshold THEN 'red' WHEN restore >= var.yellow_threshold THEN 'yellow' ELSE 'green' END restore_dot,\nselective_backup,\nCASE WHEN selective_backup >= var.red_threshold THEN 'red' WHEN selective_backup >= var.yellow_threshold THEN 'yellow' ELSE 'green' END selective_backup_dot,\nvar.yellow_threshold,var.red_threshold\nFROM q1,var"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
