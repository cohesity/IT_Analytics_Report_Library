---
title: "TSM Disk Media Volume Pools"
report_id: 988
rtd_name: "TSM Disk Media Volume Pools.rtd"
description: "TSM Disk Media Volume Pools"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "SELECT s.hostname, dm.media_name,sp.storage_pool_name, dm.est_mbyte_capacity, dm.pct_utilized \nFROM apt_v_tsm_disk_media dm, apt_v_tsm_storage_pool sp, apt_v_server s\nWHERE dm.storage_pool_id=sp.storage_pool_id\nAND dm.server_id=s.server_id\nAND dm.server_id IN (${hosts})\nORDER BY s.hostname, dm.media_name"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
