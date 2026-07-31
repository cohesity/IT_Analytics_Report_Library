---
title: "Allocated Available by Array"
report_id: 1061
rtd_name: "Allocated Available by Array.rtd"
description: "Allocated Available by Array"
problem_statement: "I have a new application to deploy, I need to look across all my storage arrays to see which ones have enough available capacity to satisfy the storage requirements for the application."
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "SELECT \nArray_name,\nallocated_gb, available_gb\nFROM aps_v_storage_array\nWHERE\n'${queryCombo1}' IN \n  CASE \n    WHEN '${queryCombo1}' NOT IN (' All') THEN\n      CASE\n        WHEN vendor_name = '${queryCombo1}' THEN '${queryCombo1}'\n      END\n   ELSE ' All'\nEND\nORDER BY available_gb DESC"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
