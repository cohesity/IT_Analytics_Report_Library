---
title: "TSM Process Size and Counts over Time"
report_id: 1168
rtd_name: "TSM Process Size and Counts over Time.rtd"
description: "TSM Process Size and Counts over Time"
problem_statement: "I'm looking for a single graphical report which shows me the number of TSM processes and their size , broken down  by type i.e. Reclamations, Migrations, Stg Pool Backups, DB Backups, etc. with the ability to group them on a daily, weekly, monthly or yearly basis."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 10/30/2015\nWITH\nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays, \n${startDate} startDate, \n'${freeCombo2}' unit,\nDECODE('${freeCombo2}', 'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual \n)\nSELECT\nTO_CHAR(trunc(start_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY HH24:MI') the_date,\nTO_CHAR(trunc(start_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24MI') sort_order,\nvar.unit,\nSUM(DECODE(job_type_name,'Expiration',1,0)) expiration,\nROUND(SUM(DECODE(job_type_name,'Expiration',kilobytes/div_by,0)),2) expiration_size,\nSUM(DECODE(job_type_name,'Full DB Backup',1,0)) full_DB_Backup,\nROUND(SUM(DECODE(job_type_name,'Full DB Backup',kilobytes/div_by,0)),2) full_DB_Backup_size,\nSUM(DECODE(job_type_name,'Incremental DB Backup',1,0)) incr_DB_Backup,\nROUND(SUM(DECODE(job_type_name,'Incremental DB Backup',kilobytes/div_by,0)),2) incr_DB_Backup_size,\nSUM(DECODE(job_type_name,'Migration',1,0)) migration,\nROUND(SUM(DECODE(job_type_name,'Migration',kilobytes/div_by,0)),2) migration_size,\nSUM(DECODE(job_type_name,'Move Media',1,0)) move_media,\nROUND(SUM(DECODE(job_type_name,'Move Media',kilobytes/div_by,0)),2) move_media_size,\nSUM(DECODE(job_type_name,'Reclamation',1,0)) reclamation,\nROUND(SUM(DECODE(job_type_name,'Reclamation',kilobytes/div_by,0)),2) reclamation_size,\nSUM(DECODE(job_type_name,'Storage Pool Backup',1,0)) stg_pool_backup,\nROUND(SUM(DECODE(job_type_name,'Storage Pool Backup',kilobytes/div_by,0)),2) stg_pool_backup_size\nFROM apt_v_tsm_process tp, var\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND server_id IN (${hosts})\nAND instance_name = '${queryCombo1}'\nGROUP BY \nTO_CHAR(trunc(start_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY HH24:MI'),\nTO_CHAR(trunc(start_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24MI'),\nvar.unit"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
