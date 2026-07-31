---
title: "Client Job Success Rate Summary"
report_id: 905
rtd_name: "Client Job Success Rate Summary.rtd"
description: "Client Job Success Rate Summary"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 05/01/2012\n--Overall client success Rate\nWITH \nt1 AS ( \nSELECT\nto_char(start_date,'MM/DD') the_date,\nj.client_name,\nmin(summary_status) min_summary_status,\nmax(summary_status) max_summary_status,\nSUM(DECODE(summary_status,0,1,0)) status_0_count,\nSUM(DECODE(summary_status,1,1,0)) status_1_count,\nSUM(DECODE(summary_status,2,1,0)) status_2_count\nFROM apt_v_job j\nWHERE j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nto_char(start_date,'MM/DD'),\nj.client_name\n),\nt2 AS (\nSELECT\nthe_date,\nSUM(DECODE(min_summary_status,2,1,0)) failed_clients,\nSUM(DECODE(min_summary_status,1,1,0)) partial_clients,\nSUM(DECODE(max_summary_status,0,1,0)) successful_clients,\nSUM(CASE WHEN min_summary_status < 2 AND max_summary_status = 2 THEN 1 ELSE 0 END) success_and_failed_clients\nFROM t1\nGROUP BY the_date\n)\nSELECT\nthe_date,\nROUND(failed_clients/(failed_clients + partial_clients + successful_clients + success_and_failed_clients)*100,2) failure_rate,\nROUND(partial_clients/(failed_clients + partial_clients + successful_clients + success_and_failed_clients)*100,2) partial_rate,\nROUND(successful_clients/(failed_clients + partial_clients + successful_clients + success_and_failed_clients)*100,2) success_rate,\nROUND(success_and_failed_clients/(failed_clients + partial_clients + successful_clients + success_and_failed_clients)*100,2) mixed_rate\nFROM t2\n\n"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
