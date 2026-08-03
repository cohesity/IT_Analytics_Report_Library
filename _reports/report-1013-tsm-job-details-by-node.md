---
title: "TSM Job Details by Node"
report_id: 1013
rtd_name: "TSM Job Details by Node.rtd"
description: "TSM Job Details by Node"
problem_statement: ""
author: "rich.rose@aptare.colm\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.colm\n--Last Modified: 04/05/2012\nSELECT \ntj.server_name,\ntj.client_id,\ntj.client_name tcp_name,\ntj.node_id,\ntj.node_name,\ntj.job_type_name,\ntj.domain_name,\ntj.schedule_name,\ntsp.storage_pool_name,\nCASE tj.summary_status \nWHEN 0 THEN 'blue'\nWHEN 1 THEN 'yellow'\nELSE 'red'\nEND status_color,\nCASE tj.summary_status \nWHEN 0 THEN 'Successful'\nWHEN 1 THEN 'Partial'\nELSE 'Failed'\nEND status_name,\nCASE tj.vendor_status\nWHEN 1 THEN 'Completed'\nWHEN 2 THEN 'Missed'\nWHEN 3 THEN 'Failed'\nWHEN 4 THEN 'Started'\nWHEN 5 THEN 'Restarted'\nWHEN 6 THEN 'Severed'\nWHEN 7 THEN 'Future'\nWHEN 8 THEN 'Pending'\nWHEN 9 THEN 'Uncertain'\nWHEN 10 THEN 'In Progress'\nWHEN null THEN 'Unknown'\nELSE 'Unknown'\nEND state,\ntj.start_date,\ntj.finish_date,\nrtd.secsToHoursMinSecs((finish_date-start_date)*24*60*60) duration,\ntj.kilobytes/1024/1024 size_gb, \ntj.nbr_of_files, \ntj.mbytes_sec \nFROM apt_v_tsm_job tj, apt_v_tsm_storage_pool tsp\nWHERE tj.client_id IN (${hosts})\nAND tj.finish_date BETWEEN ${startDate} AND ${endDate}\nAND tj.storage_pool_id = tsp.storage_pool_id(+)\nORDER BY tj.finish_date DESC"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
