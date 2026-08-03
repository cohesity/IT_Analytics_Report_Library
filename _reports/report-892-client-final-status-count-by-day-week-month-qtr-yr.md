---
title: "Client Final Status Count by Day,Week,Month,Qtr,Yr"
report_id: 892
rtd_name: "Client Final Status Count by Day,Week,Month,Qtr,Yr.rtd"
description: "Client Final Status Count by Day,Week,Month,Qtr,Yr"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 12/11/2012\n--Daily Client Final Status by Day,Week,Month,Quarter,Year\n--This report helps to see if how the overall client status is doing over time.\n--This report determines the final client status based on a user defined cutoff time\n--Then it aggregates that count by Day, Week, Month, or Year\n--If the all the clients jobs failed the client is flagged as failed\n--If all the client's jobs were successful then the client is flagged as successful\n--If all the client's jobs were partially successful then the client is flagged as partial\n--If there is any combination of the above then the client is flagged as mixed \n--NOTE: Successful and Partials are hidden by default to help focus on the problems\n--they can be enabled by editing the Report Template and checking the columns in the \n--Formatting tab.\nWITH\nd0 AS (\nSELECT\nDECODE('${freeCombo2}','Midnight','1am',1,'2am',2,'3am',3,'4am',4,'5am',5,'6am',6,'7am',7,'8am',8,'9am',9,'10am',10,'11am',11,'12pm',12) cutoff_time\nFROM dual\n),\nt1 AS (\nSELECT\nTRUNC(start_date)+(d0.cutoff_time/24) cutoff_date_time,\nj.client_name,\nCOUNT(job_id) job_count,\nMIN(summary_status) min_summary_status,\nMAX(summary_status) max_summary_status,\nSUM(DECODE(summary_status,0,1,0)) status_0_count,\nSUM(DECODE(summary_status,1,1,0)) status_1_count,\nSUM(DECODE(summary_status,2,1,0)) status_2_count\nFROM apt_v_job j,d0\nWHERE j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nTRUNC(start_date)+(d0.cutoff_time/24),\nj.client_name\n),\nt2 AS (\nSELECT\ncutoff_date_time,\nSUM(DECODE(min_summary_status,2,1,0)) failed_clients,\nSUM(DECODE(min_summary_status,1,1,0)) partial_clients,\nSUM(DECODE(max_summary_status,0,1,0)) successful_clients,\nSUM(CASE WHEN min_summary_status < 2 AND max_summary_status = 2 THEN 1 ELSE 0 END) success_and_failed_clients\nFROM t1\nGROUP BY cutoff_date_time\n)\nSELECT\nTO_CHAR(TRUNC(cutoff_date_time,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYY/MM/DD') the_date,\nSUM(successful_clients) successful_clients,\nSUM(partial_clients) partial_clients,\nSUM(success_and_failed_clients) success_and_failed_clients,\nSUM(failed_clients) failed_clients\nFROM t2\nGROUP BY TO_CHAR(TRUNC(cutoff_date_time,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYY/MM/DD')"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
