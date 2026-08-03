---
title: "HDS DP Pool Usage History Single Array"
report_id: 1074
rtd_name: "HDS DP Pool Usage History Single Array.rtd"
description: "HDS DP Pool Usage History Single Array"
problem_statement: ""
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 02/22/2018\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo1}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\na0 AS (--Get the indiviapt_v_dual pools then add them up in the end \nSELECT\nTRUNC(log_date,DECODE('${freeCombo2}','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')) log_date,\narray_name,\npool_id,\nROUND(MAX(allocated_kb/div_by),2) allocated,\nROUND(MAX(unallocated_kb/div_by),2) unallocated,\nROUND(MAX(available_kb/div_by),2) available,\nROUND(MAX(capacity_kb/div_by),2) capacity,\nROUND(MAX(capacity_of_vvols_kb/div_by),2) capacity_of_vvols,\nROUND(MAX(touched_kb/div_by),2) touched,\nROUND(MAX(associated_warn_kb/div_by),2) associated_warn,\nROUND(MAX(allocated_warn_kb/div_by),2) allocated_warn\nFROM \naps_v_hds_journal_pool_log, var\nWHERE \nlog_date BETWEEN ${startDate} AND ${endDate}\nAND array_name = '${queryCombo1}'\nAND array_name is not null\nGROUP BY \nTRUNC(log_date,DECODE('${freeCombo2}','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),\narray_name,\npool_id\nHAVING MAX(allocated_kb) > 0\n)\nSELECT \nlog_date,\nSUM(a0.allocated) allocated,\nSUM(a0.unallocated) unallocated,\nSUM(a0.capacity) capacity,\nSUM(a0.capacity_of_vvols) capacity_of_vvols, \nSUM(a0.touched) touched,\nSUM(a0.available) available,\nSUM(a0.touched + a0.available) associated,\nSUM(a0.associated_warn) associated_warn,\nSUM(a0.allocated_warn) allocated_warn\nFROM \na0\nGROUP BY\nlog_date\nORDER BY \nlog_date ASC\n"
has_explanation: false
products: [{"slug": "capacity-manager-hds-reports", "name": "HDS Reports"}]
categories: []
product_slugs: ["capacity-manager-hds-reports"]
category_slugs: []
---
