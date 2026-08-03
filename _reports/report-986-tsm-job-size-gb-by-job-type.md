---
title: "TSM Job Size(GB) by Job Type"
report_id: 986
rtd_name: "TSM Job Size(GB) by Job Type.rtd"
description: "TSM Job Size(GB) by Job Type"
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
sql_query: "--TSM Job Size by Job Type\nSELECT to_char(start_date,'MM/DD/YY') run_date, job_type_name,  \nsum(kilobytes/1024/1024) size_gb\nFROM apt_v_tsm_job\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND client_id in (${hosts})\nGROUP BY to_char(start_date,'MM/DD/YY'), job_type_name\nORDER BY to_char(start_date,'MM/DD/YY'), job_type_name"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
