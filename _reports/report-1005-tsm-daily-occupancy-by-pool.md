---
title: "TSM Daily Occupancy by Pool"
report_id: 1005
rtd_name: "TSM Daily Occupancy by Pool.rtd"
description: "TSM Daily Occupancy by Pool"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com    Date: 07/07/2011\n--\n--\nSELECT to_char(poll_date,'MM/DD/YY') poll_date, storage_pool_name,\nsum(stg_pool_phy_mbytes)/1024 size_GB\nFROM apt_v_tsm_occupancy_log \nWHERE client_id IN (${hosts})\nAND poll_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY to_char(poll_date,'MM/DD/YY'), storage_pool_name\nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
