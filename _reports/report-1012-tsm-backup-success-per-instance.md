---
title: "TSM Backup Success per Instance"
report_id: 1012
rtd_name: "TSM Backup Success per Instance.rtd"
description: "TSM Backup Success per Instance"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "WITH q1 AS (\nSELECT \ntj.instance_name,\ncount(j.job_id) job_count,\nsum(DECODE(vendor_status_name,'Successful',1,0)) Successful_job_count,\nsum(DECODE(vendor_status_name,'Failed',1,0)) failed_job_count,\nsum(DECODE(vendor_status_name,'Missed',1,0)) missed_job_count,\nsum(DECODE(vendor_status_name,'Partial',1,0)) partial_job_count,\nround((sum(DECODE(vendor_status_name,'Successful',1,0))+sum(DECODE(vendor_status_name,'Partial',1,0)))\n/count(j.job_id)*100,2) success_rate\nFROM apt_v_job j,apt_v_tsm_job tj\nWHERE j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.job_id = tj.job_id\nGROUP BY \ntj.instance_name\n)SELECT instance_name,\nCASE \nWHEN success_rate BETWEEN ${freeCombo2} AND 99.999 THEN 'green'\nWHEN success_rate BETWEEN ${freeCombo1} AND ${freeCombo2} THEN 'yellow'\nWHEN success_rate < ${freeCombo1} THEN 'red'\nWHEN success_rate = 100 THEN 'blue'\nELSE 'white'\nEND status_dot,\njob_count,\nsuccessful_job_count,\nfailed_job_count,missed_job_count,\npartial_job_count,\nsuccess_rate\nFROM q1"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
