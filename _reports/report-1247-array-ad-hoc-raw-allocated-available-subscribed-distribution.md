---
title: "Array Ad Hoc Raw Allocated Available Subscribed Distribution"
report_id: 1247
rtd_name: "Array Ad Hoc Raw Allocated Available Subscribed Distribution.rtd"
description: "Array Ad Hoc Raw Allocated Available Subscribed Distribution"
problem_statement: "I need to see my array capacity values grouped by vendor, array family and individual arrays"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/22/2017\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo1}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)SELECT\nDECODE ('${freeCombo2}','Array Vendor',vendor_name,'Array Family',array_family,'Array Name',array_name) report_on,\nROUND(SUM(raw_capacity_kb/div_by),2) raw_capacity,\nROUND(SUM(thin_pool_subscribed_kb/div_by),2) subscribed,\nROUND(SUM(allocated_kb/div_by),2) allocated,\nROUND(SUM(available_kb/div_by),2) available\nFROM aps_v_storage_array sa, var\nWHERE storage_array_id IN (${arrays})\nGROUP BY \nDECODE('${freeCombo2}','Array Vendor',vendor_name,'Array Family',array_family,'Array Name',array_name)"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
