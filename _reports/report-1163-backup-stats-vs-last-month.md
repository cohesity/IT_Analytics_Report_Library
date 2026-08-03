---
title: "Backup Stats vs Last Month"
report_id: 1163
rtd_name: "Backup Stats vs  Last Month.rtd"
description: "Backup Stats vs Last Month"
problem_statement: "I need high level KPI's on my backup environment that I can present to my CIO, i.e. more information, less data."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/18/2015\n--Compare backup metrics today vs same time last month\nWITH \nVAR AS (\nSELECT \n'${freeCombo1}' unit,\nDECODE('${freeCombo1}', 'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by,\nADD_MONTHS(TRUNC(sysdate,'MM'),-1) p_first, \nLAST_DAY(ADD_MONTHS(sysdate,-1)) p_last, \nADD_MONTHS(TRUNC(sysdate,'DD'),-1) p_day,\nTRUNC(sysdate,'MM') c_first, \nLAST_DAY(sysdate) c_last,\nTRUNC(sysdate,'DD') c_day\nFROM apt_v_dual\n),\np0 AS (\nSELECT\nCOUNT(DISTINCT client_id) clients,\nROUND(SUM(kilobytes/div_by),2) volume,\nSUM(DECODE(summary_status,2,1,0)) failed_jobs,\nSUM(nbr_of_files/1000000) nbr_of_files\nFROm apt_v_job j, var\nWHERE client_id IN (${hosts}) AND j.finish_date BETWEEN p_first AND p_day\n),\nc0 AS (\nSELECT\nCOUNT(DISTINCT client_id) clients,\nROUND(SUM(kilobytes/div_by),2) volume,\nSUM(DECODE(summary_status,2,1,0)) failed_jobs,\nSUM(nbr_of_files/1000000) nbr_of_files\nFROM apt_v_job j, var\nWHERE client_id IN (${hosts}) AND j.finish_date BETWEEN c_first AND c_day\n)\n-- Metrics Start Here --\nSELECT\n1 sort_order,\n'Backup Clients' metric,\np0.clients p_value,\nc0.clients c_value, \n(c0.clients - p0.clients) delta, \nROUND((c0.clients - p0.clients) / DECODE(p0.clients,0,NULL,p0.clients),2) delta_pct,\nABS(ROUND((c0.clients - p0.clients) / DECODE(p0.clients,0,NULL,p0.clients),2)) pct_delta\nFROM p0, c0\nUNION\nSELECT\n2 sort_order,\n'Backup Volume'||' ('||var.unit||')' metric,\np0.volume p_value,\nc0.volume c_value, \n(c0.volume - p0.volume) delta, \nROUND((c0.volume - p0.volume) / DECODE(p0.volume,0,NULL,p0.volume),2) delta_pct,\nABS(ROUND((c0.volume - p0.volume) / DECODE(p0.volume,0,NULL,p0.volume),2)) pct_delta\nFROM p0, c0, var\nUNION\nSELECT\n3 sort_order,\n'Failed Backups' metric,\np0.failed_jobs p_value,\nc0.failed_jobs c_value, \n(c0.failed_jobs - p0.failed_jobs) delta, \nROUND((c0.failed_jobs - p0.failed_jobs) / DECODE(p0.failed_jobs,0,NULL,p0.failed_jobs),2) delta_pct,\nABS(ROUND((c0.failed_jobs - p0.failed_jobs) / DECODE(p0.failed_jobs,0,NULL,p0.failed_jobs),2)) pct_delta\nFROM p0, c0\nUNION\nSELECT\n4 sort_order,\n'Files Protected (Millions)' metric,\np0.nbr_of_files p_value,\nc0.nbr_of_files c_value, \n(c0.nbr_of_files - p0.nbr_of_files) delta, \nROUND((c0.nbr_of_files - p0.nbr_of_files) / DECODE(p0.nbr_of_files,0,NULL,p0.nbr_of_files),2) delta_pct,\nABS(ROUND((c0.nbr_of_files - p0.nbr_of_files) / DECODE(p0.nbr_of_files,0,NULL,p0.nbr_of_files),2)) pct_delta\nFROM p0, c0"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
