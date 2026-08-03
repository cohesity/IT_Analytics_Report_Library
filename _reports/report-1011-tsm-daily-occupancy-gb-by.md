---
title: "TSM Daily Occupancy(GB) by"
report_id: 1011
rtd_name: "TSM Daily Occupancy by.rtd"
description: "TSM Daily Occupancy by"
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
sql_query: "\n--Author: rich.rose@aptare.com    Date: 07/07/2011\n--\n--\nWITH t1 as (\nSELECT to_char(poll_date,'MM/DD/YY') poll_date,\nhost_name tcp_client_name, \nnode_name node,\nnode_name||' - '||storage_pool_name node_storage_pool,\nnode_name||' - '||filespace_name node_filespace,\nstorage_pool_name storage_pool,\nfilespace_name filespace,\nstorage_pool_name,  \n(stg_pool_phy_mbytes/1024) size_gb\nFROM apt_v_tsm_occupancy_log\nWHERE poll_date BETWEEN ${startDate} AND ${endDate}\nAND client_id in (${hosts})\n)\nSELECT poll_date, to_char(${freeCombo1}) unit,sum(size_gb) size_gb\nFROM t1\nGROUP BY poll_date, to_char(${freeCombo1})"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
