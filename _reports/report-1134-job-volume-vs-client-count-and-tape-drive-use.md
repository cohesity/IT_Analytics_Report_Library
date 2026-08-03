---
title: "Job Volume vs Client Count and Tape Drive Use"
report_id: 1134
rtd_name: "Job Volume vs Client Count and Tape Drive Use.rtd"
description: "Job Volume vs Client Count and Tape Drive Use"
problem_statement: "I need to see if my backup volume is being evenly distributed across my backup window and that my tape drives are not all being used and any particular hour."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 12/03/2014\nWITH \nj1 AS (\nSELECT \nTO_CHAR(TRUNC(j.start_date,'HH24'),'HH24') the_date,\nTO_CHAR(j.start_date,'MM/DD/YY HH24') pretty_date,\nCOUNT(DISTINCT job_id) job_count,\nRATIO_TO_REPORT(COUNT(DISTINCT job_id)) OVER() rr_job_count,\nCOUNT(DISTINCT client_id) client_count,\nRATIO_TO_REPORT(COUNT(DISTINCT client_id)) OVER() rr_client_count,\nSUM(kilobytes/1024/1024) gb_written,\nRATIO_TO_REPORT(SUM(kilobytes/1024/1024)) OVER() rr_gb_written\nFROM apt_v_job j\nWHERE\nj.server_name = '${queryCombo1}'\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nTO_CHAR(TRUNC(j.start_date,'HH24'),'HH24'),\nTO_CHAR(j.start_date,'MM/DD/YY HH24')\n),\nt1 AS (\nSELECT \nTO_CHAR(TRUNC(tdl.poll_time,'HH24'),'HH24') the_date,\nTO_CHAR(tdl.poll_time,'MM/DD/YY HH24') pretty_date,\nSUM(DECODE(tdl.in_use,'Y',1,0)) in_use_count\nFROM\napt_v_tape_drive td, apt_v_tape_drive_log tdl\nWHERE \ntd.drive_id = tdl.drive_id\nAND td.management_server_name = '${queryCombo1}'\nAND poll_time BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nTO_CHAR(TRUNC(tdl.poll_time,'HH24'),'HH24'),\nTO_CHAR(tdl.poll_time,'MM/DD/YY HH24') \n)\nSELECT\nj1.the_date,\nj1.pretty_date,\nt1.in_use_count,\nj1.job_count,\nROUND((j1.rr_job_count*100),2) rr_job_count,\nj1.client_count,\nj1.rr_client_count,\nROUND((j1.rr_client_count*100),2) rr_client_count, \nROUND(gb_written,2) gb_written,\nROUND((rr_gb_written*100),2) rr_gb_written,\nDECODE('${freeCombo1}','Job Count',j1.job_count,'Job Volume',j1.gb_written) the_metric\nFROM j1, t1\nWHERE j1.pretty_date = t1.pretty_date (+)"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
