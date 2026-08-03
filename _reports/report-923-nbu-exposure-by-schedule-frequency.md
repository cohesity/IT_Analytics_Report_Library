---
title: "NBU Exposure by Schedule Frequency"
report_id: 923
rtd_name: "NBU Exposure by Schedule Frequency.rtd"
description: "NBU Exposure by Schedule Frequency"
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
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/25/2012\n--Determines the recovery point of a backup and shows true exposure based on the \n--expirarion of the image.\nWITH \nt1 AS (\nSELECT DISTINCT \npc.client_id, \npc.client_name, \npc.server_id,\ns.hostname master_server,\npc.policy_id, \npc.policy_name,\nDECODE(pc.is_active,'Y','Yes','N','No') is_active, \nDECODE(sc.selection_type,1,'Frequency Based Schedule',2,'Calendar Based Schedule')  selection_type, \nsc.schedule_id,\nsc.schedule_name schedule_name, \nsc.frequency seconds, \nDECODE(\nsc.frequency,3600,'Every Hour',\n7200,'Every 2 Hours',\n64800,'Every 18 Hours',\n72000,'Every 20 Hours',\n82800,'Every 23 Hours',\n86400,'Every Day',\n345600,'Every 4 Days',\n604800,'Every 7 Days',\n21168000,'Every 245 Days',\nNULL,'Calendar') frequency, \nDECODE(sc.schedule_type,\n0,'Full Backup',\n1,'Cumulative Incremantal',\n2,'Application Backup',\n4,'Differential Incremental',\n5,'Archive') as \"Backup Type\" , \nsc.retention_days,\nsc.retention_days||' Days' Retain_Data_For \nFROM apt_v_server s, apt_v_server c, \napt_v_nbu_schedule sc, apt_v_nbu_policy_client pc \nWHERE pc.client_id IN (${hosts})\nAND pc.client_id = c.server_id\nAND pc.server_id = s.server_id \nAND pc.policy_id = sc.policy_id (+)\nORDER BY pc.client_name\n),\nt2 AS (\nSELECT \nlnb.server_id,\nlnb.client_id,\nlnb.schedule_id,\nmax(lnb.job_id) last_job_id\nFROM apt_v_last_nbu_backup lnb,apt_v_last_client_job lcj, t1\nWHERE lcj.job_id = lnb.job_id\nAND lnb.server_id = t1.server_id \nAND lnb.client_id = t1.client_id  \nAND lnb.schedule_id = t1.schedule_id\nAND lcj.summary_status < 2\nGROUP BY\nlnb.server_id,\nlnb.client_id,\nlnb.schedule_id\n),\nt3 AS (\nSELECT\nnj.job_id,\nnj.finish_date last_good_backup_date,\nnj.duration_secs\nFROM apt_v_nbu_job nj,t2\nWHERE nj.job_id = t2.last_job_id\n) \nSELECT \nt1.server_id,\nt1.master_server,\nt1.client_id, \nclient_name, \npolicy_id, \npolicy_name,\nis_active, \nschedule_name, \nselection_type, \nt1.schedule_id,\nseconds, \nfrequency, \nretain_data_for,\nlast_good_backup_date,\nrtd.secsToHoursMinSecs(t3.duration_secs) duration,\n(sysdate + (t3.duration_secs/60/60/24)) earliest_recovery_date,\nCASE \nWHEN retention_days - (sysdate-last_good_backup_date) > 0 THEN to_char(trunc(retention_days - (sysdate-last_good_backup_date)))\nELSE 'Too Late'\nEND days_left,\nCASE  \nWHEN (retention_days - (sysdate-last_good_backup_date)) > 0 THEN 'green' \nWHEN (retention_days - (sysdate-last_good_backup_date)) = 0 THEN 'white' \nWHEN (retention_days - (sysdate-last_good_backup_date)) < 0 THEN 'red'\nEND \nstatus\nFROM t1, t2, t3\nWHERE t1.server_id = t2.server_id \nAND t1.client_id = t2.client_id  \nAND t1.schedule_id = t2.schedule_id\nAND t3.job_id = t2.last_job_id"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
