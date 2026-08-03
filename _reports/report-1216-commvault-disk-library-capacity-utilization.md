---
title: "CommVault Disk Library Capacity & Utilization"
report_id: 1216
rtd_name: "CommVault Disk Library Capacity & Usage.rtd"
description: "CommVault Disk Library Capacity & Utilization"
problem_statement: "I need to understand the capcity of my disk targets to plan for my backups"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 07/24/2018\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo1}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\nt1 AS (\nSELECT\ns.server_id s_server_id,\ns.display_name s_display_name,\ncdl.cmv_disk_library_id,\ncdl.library_external_name,\nCOUNT(DISTINCT cdm.cmv_disk_media_id) nbr_drives,\nSUM(cdm.total_space_kb/div_by) total_space,\nSUM(cdm.free_space_kb/div_by) free_space,\nSUM(cdm.used_space_kb/div_by) used_space,\nSUM(cdm.used_space_kb)/SUM(NULLIF(cdm.total_space_kb,0)) pct_used,\nSUM(cdm.used_space_kb)/SUM(NULLIF(cdm.total_space_kb,0))*100 used_pct,\nSUM(cdm.nbr_backups) nbr_backups, \nMAX(last_backup_time) last_backup_time, \nSUM(cdm.nbr_restores) nbr_restores, \nMAX(last_restore_time) last_restore_time,\nSUM(NVL(cdm.nbr_hard_errors,0)+NVL(cdm.nbr_soft_errors,0)) nbr_of_errors\nFROM\nvar, apt_v_server s, apt_v_cmv_disk_media cdm, apt_v_cmv_disk_library cdl\nWHERE\ncdm.server_id = s.server_id\nAND cdm.server_id IN (${hosts})\nAND cdm.cmv_disk_library_id =  cdl.cmv_disk_library_id\nGROUP BY\ns.server_id,\ns.display_name,\ncdl.cmv_disk_library_id,\ncdl.library_external_name\n),\nt2 AS (\nSELECT \ncdm.cmv_disk_library_id,\nCOUNT(DISTINCT j.job_id) nbr_of_jobs,\nSUM(j.kilobytes/div_by) job_volume,\nrtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(j.kilobytes/div_by,2)) ORDER BY j.start_date) AS StringListType),', ') the_spk\nFROM apt_v_job j, apt_v_cmv_job_disk_media jdm, apt_v_cmv_disk_media cdm, var\nWHERE jdm.job_id = j.job_id\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.server_id IN (${hosts})\nAND jdm.cmv_disk_media_id = cdm.cmv_disk_media_id\nGROUP BY cdm.cmv_disk_library_id\n)\nSELECT \nt1.s_server_id,\nt1.s_display_name,\nt1.library_external_name,\nt1.nbr_drives,\nt1.total_space,\nt1.free_space,\nt1.used_space,\nt1.pct_used,\nt1.used_pct,\nt1.last_backup_time, \nt1.last_restore_time,\nt1.nbr_of_errors,\nt2.nbr_of_jobs,\nNVL(t2.job_volume,0) job_volume,\nt2.the_spk\nFROM t1, t2\nWHERE \nt1.cmv_disk_library_id = t2.cmv_disk_library_id (+)\n--AND t2.nbr_of_jobs >  0\nORDER BY NVL(t2.job_volume,0) DESC"
has_explanation: false
products: [{"slug": "backup-manager-commvault", "name": "CommVault"}]
categories: []
product_slugs: ["backup-manager-commvault"]
category_slugs: []
---
