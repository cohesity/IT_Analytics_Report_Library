---
title: "NBU Client DeDupe Report CL"
report_id: 1200
rtd_name: "NBU Client DeDupe Report CL.rtd"
description: "NBU Client DeDupe Report CL"
problem_statement: "Show the DeDuplication rates for individual clients.  the \"CL\" designates that youcan report on individual or groups of clients regardless of thier Master Server"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last updated: 04/04/2018\nWITH\nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays,\n${startDate} startDate,\nDECODE('${freeCombo1}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by\nFROM apt_v_dual\n)\nSELECT\nj.master_host_name,\nj.client_host_name,\n(100-SUM(dj.cr_sent)/SUM(DECODE(dj.scanned_kb,0,NULL,dj.scanned_kb))*100) dedupe_savings_pct, \nCOUNT(j.job_id) job_count,\nSUM(dj.scanned_kb/div_by) scanned,\nSUM(dj.cr_sent/div_by) cr_sent,\nSUM(dj.cr_sent)/SUM(DECODE(dj.scanned_kb,0,NULL,dj.scanned_kb)) pct_sent,\nSUM(dj.cr_sent)/SUM(DECODE(dj.scanned_kb,0,NULL,dj.scanned_kb))*100 sent_pct,\nSUM(dj.hdr_tir_scanned_kb/div_by) tir_scanned,\nSUM(dj.hdr_tir_cr_sent_kb/div_by) tir_cr_sent,\nSUM(dj.hdr_tir_cr_sent_kb)/SUM(DECODE(dj.hdr_tir_scanned_kb,0,NULL,dj.hdr_tir_scanned_kb)) tir_pct_sent,\nSUM(dj.hdr_tir_cr_sent_kb)/SUM(DECODE(dj.hdr_tir_scanned_kb,0,NULL,dj.hdr_tir_scanned_kb))*100 tir_sent_pct   \nFROM apt_v_nbu_dedup_job dj, apt_v_nbu_job_detail j,var\nWHERE j.job_id = dj.job_id\nAND j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.summary_status < 2\nAND dj.scanned_kb > 0\nAND j.server_id <> j.client_id\nGROUP BY \nj.master_host_name,\nj.client_host_name\nORDER BY 3 ASC"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
