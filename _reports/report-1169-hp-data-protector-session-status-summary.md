---
title: "HP Data Protector Session Status Summary"
report_id: 1169
rtd_name: "HP Data Protector Session Status Summary.rtd"
description: "HP Data Protector Session Status Summary"
problem_statement: "I'm looking for a summarized report of my HP Data Protector sessions so I can quickly see at a glance if there are any areas of concern."
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
sql_query: "--Author:rich.rose@aptare.com\n--Last Modified: 11/02/2015\nWITH\nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays, \n${startDate} startDate, \n'${freeCombo1}' unit,\nDECODE('${freeCombo1}', 'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual \n),\nt1 AS (\nSELECT\nhj.session_id,\nhj.session_name,\nMIN(hj.start_date) started,\nMAX(finish_date) ended,\nCOUNT(DISTINCT hj.client_id) clients,\nSUM(kilobytes/div_by) job_size,\nCOUNT(hj.job_id) total_jobs,\nSUM(DECODE(hj.summary_status,0,1,0)) success,\nSUM(DECODE(hj.summary_status,1,1,0)) partial,\nSUM(DECODE(hj.summary_status,2,1,0)) failed,\nSUM(DECODE(hj.summary_status,null,1,0)) incomplete,\nSUM(DECODE(hj.vendor_status,5,1,0)) running,\nSUM(DECODE(hj.vendor_status,6,1,0)) pending\nFROM apt_v_hpd_job hj, var\nWHERE\nhj.client_id IN (${hosts})\nAND hj.start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nhj.session_id,\nhj.session_name\n)\nSELECT\nsession_id,\nsession_name,\nstarted,\nended,\nclients,\njob_size,\ntotal_jobs,\nsuccess,\npartial,\nfailed,\nfailed/DECODE((total_jobs - incomplete),0,null,(total_jobs - incomplete)) pct_fail,\nfailed/DECODE((total_jobs - incomplete),0,null,(total_jobs - incomplete))*100 fail_pct,\nincomplete,\nrunning,\npending,\nincomplete/DECODE(total_jobs,0,null,total_jobs) pct_incomplete,\nincomplete/DECODE(total_jobs,0,null,total_jobs)*100 incomplete_pct\nFROM t1\nORDER BY \nstarted DESC"
has_explanation: false
products: [{"slug": "backup-manager-hpdp", "name": "HPDP"}]
categories: []
product_slugs: ["backup-manager-hpdp"]
category_slugs: []
---
