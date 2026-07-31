---
title: "TSM Backups Size and Counts over Time"
report_id: 1167
rtd_name: "TSM Backups Size and Counts over Time.rtd"
description: "TSM Backups Size and Counts over Time"
problem_statement: "I'm looking for a single graphical report which shows me the number of jobs and size of the jobs, broken down  by type i.e. Fulls, Incrementals, Command, Restores, etc. with the ability to group them on a daily, weekly, monthly or yearly basis."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 10/30/2015\nWITH\nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays, \n${startDate} startDate, \n'${freeCombo2}' unit,\nDECODE('${freeCombo2}', 'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual \n)\nSELECT\nTO_CHAR(trunc(start_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY HH24:MI') the_date,\nTO_CHAR(trunc(start_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24MI') sort_order,\nvar.unit,\nSUM(DECODE(job_type_name,'Archive',1,0)) archive,\nROUND(SUM(DECODE(job_type_name,'Archive',kilobytes/div_by,0)),2) archive_size,\nSUM(DECODE(job_type_name,'Command',1,0)) command,\nROUND(SUM(DECODE(job_type_name,'Command',kilobytes/div_by,0)),2) command_size,\nSUM(DECODE(job_type_name,'Selective Backup',1,0)) selective_backup,\nROUND(SUM(DECODE(job_type_name,'Selective Backup',kilobytes/div_by,0)),2) selective_backup_size,\nSUM(DECODE(job_type_name,'Restore',1,0)) restore,\nROUND(SUM(DECODE(job_type_name,'Restore',kilobytes/div_by,0)),2) restore_size,\nSUM(DECODE(job_type_name,'Incr Backup',1,0)) incr_Backup,\nROUND(SUM(DECODE(job_type_name,'Incr Backup',kilobytes/div_by,0)),2) incr_Backup_size\nFROM apt_v_tsm_job tj, var\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND server_id IN (${hosts})\nAND instance_name = '${queryCombo1}'\nGROUP BY \nTO_CHAR(trunc(start_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY HH24:MI'),\nTO_CHAR(trunc(start_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24MI'),\nvar.unit"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
