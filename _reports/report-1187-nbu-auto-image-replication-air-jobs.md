---
title: "NBU Auto Image Replication (AIR) Jobs"
report_id: 1187
rtd_name: "NBU Auto Image Replication (AIR) Jobs.rtd"
description: "NBU Auto Image Replication (AIR) Jobs"
problem_statement: "I want to be sure my AIR policies are being replicated to a remote master server"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 11/01/2017\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo1}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\nt1 AS (--Get the Replication Import Jobs and their pathnames which are the original backup image\nSELECT \njd.job_id,\njd.nbu_job_id,\njd.master_host_name,\njd.client_host_name,\njd.job_type_name,\njd.start_date,\njd.finish_date,\njd.vendor_status,\njf.pathname\nFROM apt_v_nbu_job jd, apt_v_nbu_job_file jf\nWHERE jd.server_id IN (${hosts})\nAND jd.start_date BETWEEN ${startDate} AND ${endDate}\nAND jd.job_id = jf.job_id\nAND jd.job_type = 122\n)\nSELECT\n--Source\njd.job_id o_job_id,\njd.nbu_job_id,\njd.master_host_name,\njd.client_host_name,\njd.policy_id,\njd.policy_name,\njd.lifecycle_policy_name,\njd.schedule_name,\njd.job_type_name,\njd.start_date,\njd.finish_date,\njd.expiration_date,\njd.vendor_status,\njd.kilobytes/div_by job_size,\n--Target\nt1.job_id t_job_id,\nt1.nbu_job_id t_nbu_job_id,\nt1.master_host_name t_master_host_name,\nt1.client_host_name t_client_host_name,\nt1.job_type_name t_job_type_name,\nt1.start_date t_start_date,\nt1.finish_date t_finish_date,\nt1.vendor_status t_vendor_status,\nt1.pathname t_pathname\nFROM apt_v_nbu_job_detail jd, t1, var\nWHERE jd.client_id IN (${hosts})\nAND jd.start_date BETWEEN ${startDate} AND ${endDate}\nAND jd.backup_id = t1.pathname"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
