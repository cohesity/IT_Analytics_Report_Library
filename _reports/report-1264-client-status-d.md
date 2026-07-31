---
title: "Client Status.D"
report_id: 1264
rtd_name: "Client Status Summary.D.rtd"
description: "Client Status.D"
problem_statement: "A Drilldown only report required for Backup Job and Client Status per Backup Server CL and Backup Job and Client Status per Backup Server MS"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 10/02/2012\n--NOTE: This is a drilldown report only and will not run standalone\n--The templateName is ClientStatusSummary.D\nWITH \nd1 AS (\nSELECT\n--Dates Required for Drilldown \nTO_CHAR(${startDate},'MM/DD/YYYY') start_date_char,\nTO_CHAR(${startDate},'HH24') start_hour_char,\nTO_CHAR(${endDate},'MM/DD/YYYY') finish_date_char,\nTO_CHAR(${endDate},'HH24') finish_hour_char\nFROM apt_v_dual\n),\nt1 AS (\nSELECT\nserver_id,\nserver_name,\nclient_id,\nclient_name,\nCOUNT(job_id) job_count,\nmin(summary_status) min_summary_status,\nmax(summary_status) max_summary_status,\nSUM(DECODE(summary_status,0,1,0)) successful_jobs,\nSUM(DECODE(summary_status,1,1,0)) partial_jobs,\nSUM(DECODE(summary_status,2,1,0)) failed_jobs\nFROM apt_v_job \nWHERE\nclient_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nAND summary_status IS NOT NULL\nAND server_id = ${the_server_id}\nGROUP BY \nserver_id,\nserver_name,\nclient_id,\nclient_name\n),\nt2 AS (\nSELECT\nserver_id,\nserver_name,\nclient_id,\nclient_name,\nCASE \nWHEN min_summary_status = 2 AND max_summary_status = 2 THEN 'Failed'\nWHEN min_summary_status = 1 AND max_summary_status = 1 THEN 'Partial'\nWHEN min_summary_status = 0 AND max_summary_status = 0 THEN 'Successful'\nWHEN min_summary_status <> max_summary_status THEN 'Mixed'\nEND status,\n(successful_jobs+partial_jobs+failed_jobs) total_jobs,\nsuccessful_jobs,\npartial_jobs,\nfailed_jobs\nFROM t1\n)\nSELECT t2.*,d1.* \nFROM t2, d1\nWHERE status = DECODE('${the_status}','All',status,'${the_status}')"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
