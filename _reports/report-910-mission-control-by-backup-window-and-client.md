---
title: "Mission Control by Backup Window and Client"
report_id: 910
rtd_name: "Mission Control by Backup Window and Client.rtd"
description: "Mission Control by Backup Window and Client"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 06/14/2012\nWITH\nt1 as (--Seed the backup window dates based on the window_id from the dropdown\nSELECT start_date, finish_date  \nFROM TABLE(rtd.ListOfBackupWindowDates(${startDate},${endDate},${queryCombo1})) bw\n),\nt2 as ( \nSELECT \nt1.start_date, t1.finish_date,\nj.client_name,\nDECODE(min(summary_status),0,'green' ,1,'green',2,'red','white') status\nFROM apt_v_job j,t1\nWHERE j.start_date BETWEEN t1.start_date AND t1.finish_date\nAND t1.start_date >= ${startDate}\nAND j.client_id IN (${hosts})\nAND j.job_type_name like '%Backup'\nGROUP BY  \nt1.start_date, t1.finish_date,\nj.client_name\n)\nSELECT \nto_char(start_date,'MM/DD/YY')||'<br/>'||to_char(start_date,'hh:mm')||'-'||to_char(finish_date,'hh:mm') window,\nclient_name,\nstatus\nFROM t2"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
