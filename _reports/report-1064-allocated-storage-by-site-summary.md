---
title: "Allocated Storage by Site Summary"
report_id: 1064
rtd_name: "Allocated Storage by Site Summary.rtd"
description: "Allocated Storage by Site Summary"
problem_statement: "Enables the benefit of aligning business assets with enterprise objects."
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "SELECT \nnvl(rtd.getObjectAttributeValue(storage_array_id,'Site','A'),'Other') site,\ncount(DISTINCT host_id) nbr_of_hosts,\ncount(DISTINCT storage_array_id) nbr_of_arrays,\ncount(DISTINCT storage_domain_id) nbr_storage_domains,\nsum(nbr_of_luns) nbr_of_luns,\nsum(nbr_allocated_luns) nbr_allocated_luns,\nsum(nbr_of_luns-nbr_allocated_luns) available_luns,\nsum(total_capacity_kb/1024/1024/1024) total_capacity_tb\nFROM aps_v_storage_path\nGROUP BY nvl(rtd.getObjectAttributeValue(storage_array_id,'Site','A'),'Other')"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
