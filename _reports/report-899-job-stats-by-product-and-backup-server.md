---
title: "Job Stats by Product and Backup Server"
report_id: 899
rtd_name: "Job Stats by Product and Backup Server.rtd"
description: "Job Stats by Product and Backup Server"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 09/26/2011\nWITH t1 as (\nSELECT\nj.product_type_name,j.server_name,\ncount(DISTINCT j.client_id) Clients,\ncount(j.job_id) total_jobs,\nsum(DECODE(j.summary_status,0,1)) Success,\nsum(DECODE(j.summary_status,1,1)) Partial,\nsum(DECODE(j.summary_status,2,1)) Failed,\ncount(DISTINCT tl.library_id) libraries,\ncount(DISTINCT td.drive_id) drives\nFROM apt_v_job j, apt_v_tape_library tl, apt_v_tape_drive td\nWHERE j.client_id IN (${hosts})\nAND j.start_date BETWEEN  ${startDate} AND ${endDate}\nAND j.server_id = tl.server_id\nAND j.server_id = td.management_server_id\nGROUP BY j.product_type_name,j.server_name\nORDER BY j.product_type_name,j.server_name\n)\nSELECT product_type_name,server_name,clients,\ntotal_jobs,success,partial,failed,\nsuccess/total_jobs success_rate,\nCASE \nWHEN success/total_jobs*100 = 100 then 'blue'\nWHEN success/total_jobs*100 BETWEEN 97 AND 99 THEN 'green'\nWHEN success/total_jobs*100 BETWEEN 85 AND 97 THEN 'yellow'\nWHEN success/total_jobs*100 BETWEEN 0  AND 90 THEN 'red'\nEND status_dot,\nlibraries,drives\nFROM t1"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
