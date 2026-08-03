---
title: "EMC VMAX Pool Usage History"
report_id: 1031
rtd_name: "EMC VMAX Pool Usage History.rtd"
description: "EMC VMAX Pool Usage History"
problem_statement: ""
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 02/03/2014\n--Plots a stacked bar graph depicting the Used vs Available values in \n--EMC VMAX storage pools.\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo2}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\na0 AS (\nSELECT\nTRUNC(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) the_date,\narray_name,\npool_name,\nROUND(MAX(total_capacity_kb/div_by),2) total_capacity,\nROUND(MAX(used_capacity_kb/div_by),2) used,\nROUND(MAX(available_capacity_kb/div_by),2) available,\nROUND(MAX(subscribed_capacity_kb/div_by),2) subscribed\nFROM aps_v_emc_sym_storage_pool_log spl, var\nWHERE log_date BETWEEN ${startDate} AND ${endDate}\nAND array_name LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\nAND array_name IS NOT NULL\nGROUP BY \ntrunc(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),\narray_name,pool_name\n)\nSELECT \nto_char(the_date,'MM/DD/YY') the_date,\nSUM(total_capacity) total_capacity,\nSUM(used) used,\nSUM(available) available,\nSUM(subscribed) subscribed\nFROM a0\nGROUP BY to_char(the_date,'MM/DD/YY')"
has_explanation: false
products: [{"slug": "capacity-manager-emc-reports", "name": "EMC Reports"}]
categories: []
product_slugs: ["capacity-manager-emc-reports"]
category_slugs: []
---
