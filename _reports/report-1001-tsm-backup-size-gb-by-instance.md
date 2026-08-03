---
title: "TSM Backup Size(GB) by Instance"
report_id: 1001
rtd_name: "TSM Backup Size(GB) by Instance.rtd"
description: "TSM Backup Size(GB) by Instance"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com    Date: 07/07/2011\n--\n--\nSELECT to_char(start_date,'MM/DD/YY') run_date, instance_name,  \ntrunc(sum(kilobytes/1024/1024)) size_gb\nFROM apt_v_tsm_job\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND client_id in (${hosts})\nGROUP BY to_char(start_date,'MM/DD/YY'), instance_name\nORDER BY to_char(start_date,'MM/DD/YY'), instance_name"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
