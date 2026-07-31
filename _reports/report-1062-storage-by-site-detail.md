---
title: "Storage by Site Detail"
report_id: 1062
rtd_name: "Storage by Site Detail.rtd"
description: "Storage by Site Detail"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 05/30/2012\nSELECT \nrtd.getObjectAttributeValue(storage_array_id,'Site','A') site,\nvendor_name,\narray_name,\nraw_capacity_gb/1024 raw_capacity_gb,\nraw_allocated_gb/1024 raw_allocated_gb,\nraw_available_gb/1024 raw_available_gb,\ncapacity_gb/1024 capacity_tb,\nallocated_gb/1024 allocated_tb,\navailable_gb/1024 available_tb,\nother_allocated_gb/1024 other_allocated_tb,\nlargest_free_space_gb/1024 largest_free_space_tb,\nnbr_of_luns,\nnbr_allocated_luns\nFROM aps_v_storage_array\nWHERE\n'${queryCombo1}' IN \n  CASE \n    WHEN '${queryCombo1}' NOT IN (' All Vendors') THEN\n      CASE\n        WHEN vendor_name = '${queryCombo1}' THEN '${queryCombo1}'\n      END\n   ELSE ' All Vendors'\nEND"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
