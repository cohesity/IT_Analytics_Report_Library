---
title: "HDS DP Array Pool Usage History"
report_id: 1069
rtd_name: "HDS DP Array Pool Usage History.rtd"
description: "HDS DP Array Pool Usage History"
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
sql_query: "WITH \na0 as (\nSELECT\ntrunc(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')) log_date,\narray_name,\nmax(allocated_kb/1024/1024) allocated_gb,\nmax(unallocated_kb/1024/1024) unallocated_gb,\nmax(available_kb/1024/1024) available_gb,\nmax(capacity_kb/1024/1024) capacity_gb,\nmax(capacity_of_vvols_kb/1024/1024) capacity_of_vvols_gb,\nmax(touched_kb/1024/1024) touched_gb,\nmax(associated_warn_kb/1024/1024) associated_warn_gb,\nmax(allocated_warn_kb/1024/1024) allocated_warn_gb\nFROM aps_v_hds_journal_pool_log\nWHERE log_date BETWEEN ${startDate} AND ${endDate}\nAND  array_name||'-Pool:'||pool_id = '${queryCombo1}'\nAND array_name is not null\nGROUP BY trunc(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),array_name\nHAVING max(allocated_kb) > 0\n)\nSELECT to_char(log_date,'MM/DD/YY') the_date,\na0.array_name,a0.allocated_gb,\na0.unallocated_gb,\na0.capacity_gb,\na0.capacity_of_vvols_gb, \na0.touched_gb,\na0.available_gb,\na0.touched_gb + a0.available_gb associated_gb,\na0.associated_warn_gb,\na0.allocated_warn_gb\nFROM a0"
has_explanation: false
products: [{"slug": "capacity-manager-hds-reports", "name": "HDS Reports"}]
categories: []
product_slugs: ["capacity-manager-hds-reports"]
category_slugs: []
---
