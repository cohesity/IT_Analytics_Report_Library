---
title: "TSM Job Size(GB) by Instance"
report_id: 999
rtd_name: "TSM Job Size(GB) by Instance.rtd"
description: "TSM Job Size(GB) by Instance"
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
sql_query: "SELECT to_char(start_date,'MM/DD/YY') run_date, instance_name,  \ntrunc(sum(kilobytes/1024/1024)) size_gb\nFROM apt_v_tsm_job\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND client_id in (${hosts})\nGROUP BY to_char(start_date,'MM/DD/YY'), instance_name\nORDER BY to_char(start_date,'MM/DD/YY'), instance_name"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
