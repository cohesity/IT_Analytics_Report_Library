---
title: "TSM Job Details+"
report_id: 1000
rtd_name: "TSM Job Details.rtd"
description: "TSM Job Details"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 08/24/2011\n--Display TSM Job Details\nSELECT DISTINCT  \n       tj.server_name,\n       tj.client_name tcp_name,\n       tj.node_name,\n       tj.job_type_name,\n       tj.domain_name,\n       tj.schedule_name,\n       tsp.storage_pool_name,\n       tj.start_date,\n       tj.finish_date,\n       (finish_date-start_date)*24*60 duration_min,\n       CASE tj.vendor_status\n         WHEN 1 THEN 'Completed'\n         WHEN 2 THEN 'Missed'\n         WHEN 3 THEN 'Failed'\n         WHEN 4 THEN 'Started'\n         WHEN 5 THEN 'Restarted'\n         WHEN 6 THEN 'Severed'\n         WHEN 7 THEN 'Future'\n         WHEN 8 THEN 'Pending'\n         WHEN 9 THEN 'Uncertain'\n         WHEN 10 THEN 'In Progress'\n         WHEN null THEN 'Unknown'\n         ELSE 'Unknown'\n       END state,\n       CASE tj.summary_status \n         WHEN 0 THEN '<font color=blue>Successful'\n         WHEN 1 THEN '<font color=orange>Partial'\n         ELSE '<font color=red>Failed'\n       END status,\n       tj.kilobytes/1024/1024 size_gb, \n       tj.nbr_of_files, \n       tj.mbytes_sec \n    FROM apt_v_tsm_job tj,\n         apt_v_tsm_storage_pool tsp\n    WHERE tj.client_id IN (${hosts})\n      AND tj.finish_date BETWEEN ${startDate} AND ${endDate}\n      AND tj.storage_pool_id = tsp.storage_pool_id(+)\n      AND job_type_name LIKE DECODE('${freeCombo1}','All','%','${freeCombo1}')\n    ORDER BY tj.finish_date DESC"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
