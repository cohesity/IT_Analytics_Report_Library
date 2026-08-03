---
title: "TSM Database Information"
report_id: 1009
rtd_name: "TSM Database Information.rtd"
description: "TSM Database Information"
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
sql_query: "SELECT hostname, avail_space_mbytes, capacity_mbytes, max_extension_mbytes, max_reduction_mbytes, page_size_bytes, used_pages, physical_volumes, buffer_pool_pages, total_buffer_requests, cache_hit_pct, cache_wait_pct, is_backup_running, incrementals_since_full, change_since_backup_mbytes, pct_changed, last_backup_date,(sysdate - last_backup_date) days_since_last_backup \nFROM apt_v_tsm_database d,  apt_v_server s\nWHERE d.server_id=s.server_id\nAND d.server_id IN (${hosts})"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
