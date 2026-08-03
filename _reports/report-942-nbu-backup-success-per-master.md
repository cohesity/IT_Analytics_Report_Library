---
title: "NBU Backup Success per Master"
report_id: 942
rtd_name: "NBU Backup Success per Master.rtd"
description: "NBU Backup Success per Master"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "WITH q1 AS (\nSELECT \nnj.master_host_name,\ncount(DISTINCT j.client_id) client_count,\nsum(j.kilobytes/1024/1024/1024) job_volume,\ncount(j.job_id) job_count,\nsum(DECODE(j.vendor_status_name,'Successful',1,0)) Successful_job_count,\nsum(DECODE(j.vendor_status_name,'Failed',1,0)) failed_job_count,\nsum(DECODE(j.vendor_status_name,'Partial',1,0)) partial_job_count,\nround((sum(DECODE(j.vendor_status_name,'Successful',1,0))+sum(DECODE(j.vendor_status_name,'Partial',1,0)))\n/count(j.job_id)*100,2) success_rate\nFROM apt_v_job j,apt_v_nbu_job nj\nWHERE j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.job_id = nj.job_id\nAND j.server_id IN (${hosts})\nGROUP BY \nnj.master_host_name\n)\nSELECT master_host_name,\nCASE \nWHEN success_rate BETWEEN ${freeCombo2} AND 99.999 THEN 'green'\nWHEN success_rate BETWEEN ${freeCombo1} AND ${freeCombo2} THEN 'yellow'\nWHEN success_rate < ${freeCombo1} THEN 'red'\nWHEN success_rate = 100 THEN 'blue'\nELSE 'white'\nEND status_dot,\nclient_count,\njob_volume,\njob_count,\nsuccessful_job_count,\nfailed_job_count,\npartial_job_count,\nsuccess_rate\nFROM q1\nORDER BY 8"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
