---
title: "TSM Primary Copy Pool Differences"
report_id: 1092
rtd_name: "TSM Primary Copy Pool Differences.rtd"
description: "TSM Primary Copy Pool Differences"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 02/29/2012\nWITH \nq1 AS (\nSELECT \ninstance_name,\nsum(DECODE(storage_pool_type,'Primary',1,0)) primary_pools,\nsum(DECODE(storage_pool_type,'Primary',est_mbyte_capacity,0)/1024/1024) primary_capacity,\nsum(DECODE(storage_pool_type,'Copy',1,0)) copy_pools,\nsum(DECODE(storage_pool_type,'Copy',est_mbyte_capacity,0)/1024/1024) copy_capacity\nFROM apt_v_tsm_storage_pool\nGROUP BY instance_name\nHAVING sum(DECODE(storage_pool_type,'Primary',est_mbyte_capacity,0)/1024) > 0\n)\nSELECT\ninstance_name,\nprimary_pools,primary_capacity,\ncopy_pools,copy_capacity,\nround(copy_capacity/DECODE(primary_capacity,0,null,primary_capacity)*100,2) copy_pct\nFROM q1"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
