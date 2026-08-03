---
title: "TSM Database Cache Hit Rate"
report_id: 992
rtd_name: "TSM Database Cache Hit Rate.rtd"
description: "TSM Database Cache Hit Rate"
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
sql_query: "SELECT to_char(log_date, 'MM/DD/YY') log_date,hostname server,  cache_hit_pct, cache_wait_pct\nFROM apt_v_tsm_database_log d,  apt_v_server s\nWHERE d.server_id=s.server_id\nAND d.server_id IN (${hosts})\nAND log_date BETWEEN ${startDate} AND ${endDate}"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
