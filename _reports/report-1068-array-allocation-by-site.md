---
title: "Array Allocation by Site"
report_id: 1068
rtd_name: "Array Allocation by Site.rtd"
description: "Array Allocation by Site"
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
sql_query: "SELECT\nnvl(rtd.getObjectAttributeValue(storage_array_id,'Site','A'),'Other') Site,\nsum(allocated_gb/1024) Allocated_tb\nFROM aps_v_storage_array\nGROUP BY rtd.getObjectAttributeValue(storage_array_id,'Site','A')"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
