---
title: "Allocated Used by Site"
report_id: 1056
rtd_name: "Allocated Used by Site.rtd"
description: "Allocated Used by Site"
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
sql_query: "--Group By:Day,Week,Month,Quarter,Year\n--Array:SELECT DISTINCT array_name, array_name FROM aps_v_hds_journal_pool_log order by upper(1)\nWITH \na0 as (\nSELECT\ntrunc(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')) log_date,\nnvl(rtd.getObjectAttributeValue(storage_array_id,'Site','A'),'Other') site,\nsum(allocated_gb/1024) allocated_tb,\nsum(available_gb/1024) available_tb\nFROM aps_v_storage_array_log\nWHERE log_date BETWEEN ${startDate} AND ${endDate}\nAND nvl(rtd.getObjectAttributeValue(storage_array_id,'Site','A'),'Other') = '${queryCombo1}'\nGROUP BY trunc(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),\nnvl(rtd.getObjectAttributeValue(storage_array_id,'Site','A'),'Other')\n)\nSELECT to_char(log_date,'MM/DD/YY') the_date,\na0.site,\na0.allocated_tb,\na0.available_tb\nFROM a0"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
