---
title: "RAID Types by Array"
report_id: 1066
rtd_name: "RAID Types by Array.rtd"
description: "RAID Types by Array"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "SELECT sa.array_name||sa.serial_nbr array, \ndecode(lu.raid_type,null,'None',lu.raid_type) raid_type, \nsum(total_capacity_kb)/1024/1024 total_capacity_Gb\nFROM aps_v_logical_unit lu, aps_v_storage_array sa\nWHERE  sa.storage_array_id=lu.storage_array_id\nAND sa.vendor_name LIKE DECODE('${freeCombo1}','All','%','%${freeCombo1}%')\nGROUP BY sa.array_name||sa.serial_nbr, lu.raid_type"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
