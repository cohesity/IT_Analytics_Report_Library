---
title: "TSM Daily Backup Size by Client - Node"
report_id: 1015
rtd_name: "TSM Daily Backup Size by Client - Node.rtd"
description: "TSM Daily Backup Size by Client - Node"
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
sql_query: "--Author: rich.rose@aptare.com    Date: 07/07/2011\n--\n--\nSELECT to_char(start_date,'MM/DD/YY') run_date, client_name || ' - ' || node_name,  \ntrunc(sum(kilobytes/1024/1024)) size_gb\nFROM apt_v_tsm_job\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND client_id in (${hosts})\nGROUP BY to_char(start_date,'MM/DD/YY'), client_name || ' - ' || node_name\nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
