---
title: "NBU Master Server DeDupe Report MS"
report_id: 1098
rtd_name: "NBU DeDupe Report MS.rtd"
description: "Displays the delta's between what data was scanned vs sent per master server.  That delta is the De-Duplication value."
problem_statement: "Show me the benefit realized by leveraging NetBackup's DeDuplication technology."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last updated: 04/04/2018\n--Reports on NBU PureDisk DeDupe metrics over time\nWITH\nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays,\n${startDate} startDate,\nDECODE('${freeCombo1}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by\nFROM apt_v_dual\n)\nSELECT\nj.master_host_name,\n(100-SUM(dj.cr_sent)/SUM(DECODE(dj.scanned_kb,0,NULL,dj.scanned_kb))*100) dedupe_savings_pct, \nCOUNT(j.job_id) job_count,\nCOUNT(DISTINCT j.client_id) client_count,\nSUM(dj.scanned_kb/div_by) scanned,\nSUM(dj.cr_sent/div_by) cr_sent,\nSUM(dj.cr_sent)/SUM(DECODE(dj.scanned_kb,0,NULL,dj.scanned_kb)) pct_sent,\nSUM(dj.cr_sent)/SUM(DECODE(dj.scanned_kb,0,NULL,dj.scanned_kb))*100 sent_pct,\nSUM(dj.hdr_tir_scanned_kb/div_by) tir_scanned,\nSUM(dj.hdr_tir_cr_sent_kb/div_by) tir_cr_sent,\nSUM(dj.hdr_tir_cr_sent_kb)/SUM(DECODE(dj.hdr_tir_scanned_kb,0,NULL,dj.hdr_tir_scanned_kb)) tir_pct_sent,\nSUM(dj.hdr_tir_cr_sent_kb)/SUM(DECODE(dj.hdr_tir_scanned_kb,0,NULL,dj.hdr_tir_scanned_kb))*100 tir_sent_pct   \nFROM apt_v_nbu_dedup_job dj, apt_v_nbu_job_detail j,var\nWHERE j.job_id = dj.job_id\nAND j.server_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.summary_status < 2\nGROUP BY \nj.master_host_name"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
