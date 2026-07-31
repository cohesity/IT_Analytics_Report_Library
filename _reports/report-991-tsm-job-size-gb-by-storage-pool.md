---
title: "TSM job Size(GB) by Storage Pool"
report_id: 991
rtd_name: "TSM Job Size(GB) by Storage Pool.rtd"
description: "TSM Job Size(GB) by Storage Pool"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--TSM Job Size by Storage Pool\nSELECT to_char(tj.start_date,'MM/DD/YY') run_date, sp.storage_pool_name,  \nsum(tj.kilobytes/1024/1024) size_gb\nFROM apt_v_tsm_job tj, apt_v_tsm_storage_pool sp\nWHERE tj.start_date BETWEEN ${startDate} AND ${endDate}\nAND tj.client_id in (${hosts})\nAND tj.storage_pool_id = sp.storage_pool_id\nGROUP BY to_char(tj.start_date,'MM/DD/YY'), sp.storage_pool_name\nORDER BY to_char(tj.start_date,'MM/DD/YY'), sp.storage_pool_name"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
