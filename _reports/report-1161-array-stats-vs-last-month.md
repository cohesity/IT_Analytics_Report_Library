---
title: "Array Stats vs Last Month"
report_id: 1161
rtd_name: "Array Stats vs Last Month.rtd"
description: "Array Stats vs Last Month"
problem_statement: "I need high level KPI's on my storage arrays that I can present to my CIO, i.e. more information, less data."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/18/2015\n--Compare metrics today vs same time last month\nWITH \nVAR AS (\nSELECT \n'${freeCombo1}' unit,\nDECODE('${freeCombo1}', 'GB',1,'TB',1024,'PB',(1024*1024)) div_by,\nADD_MONTHS(TRUNC(sysdate,'MM'),-1) p_first, \nLAST_DAY(ADD_MONTHS(sysdate,-1)) p_last, \nADD_MONTHS(TRUNC(sysdate,'DD'),-1) p_day,\nTRUNC(sysdate,'MM') c_first, \nLAST_DAY(sysdate) c_last,\nTRUNC(sysdate,'DD') c_day,\ndomain_id  \nFROM aps_v_domain d\nWHERE domain_name = '${queryCombo1}'\n),\np0 AS (\nSELECT\nl.storage_array_id, \nMAX(l.thin_pool_subscribed_gb) thin_pool_subscribed,\nMAX(l.raw_capacity_gb) raw_capacity,\nMAX(l.allocated_gb) allocated\nFROM aps_v_storage_array_log l, aps_v_storage_array a, var\nWHERE a.storage_array_id = l.storage_array_id \nAND a.domain_id = var.domain_id\nAND l.log_date BETWEEN p_first AND p_day\nGROUP BY l.storage_array_id\n),\np1 AS (\nSELECT\nCOUNT(DISTINCT storage_array_id) storage_arrays,\nROUND(SUM(thin_pool_subscribed/div_by),2) thin_pool_subscribed,\nROUND(SUM(raw_capacity/div_by),2) raw_capacity,\nROUND(SUM(allocated/div_by),2) allocated\nFROM p0, var\n),\nc0 AS (\nSELECT\nl.storage_array_id, \nMAX(l.thin_pool_subscribed_gb) thin_pool_subscribed,\nMAX(l.raw_capacity_gb) raw_capacity,\nMAX(l.allocated_gb) allocated\nFROM aps_v_storage_array_log l, aps_v_storage_array a, var\nWHERE a.storage_array_id = l.storage_array_id \nAND a.domain_id = var.domain_id\nAND l.log_date BETWEEN c_first AND c_day\nGROUP BY l.storage_array_id\n),\nc1 AS (\nSELECT\nCOUNT(DISTINCT storage_array_id) storage_arrays,\nROUND(SUM(thin_pool_subscribed/div_by),2) thin_pool_subscribed,\nROUND(SUM(raw_capacity/div_by),2) raw_capacity,\nROUND(SUM(allocated/div_by),2) allocated\nFROM c0, var\n)\nSELECT\n1 sort_order,\n'Storage Arrays' metric,\np1.storage_arrays p_value,\nc1.storage_arrays c_value, \n(c1.storage_arrays - p1.storage_arrays) delta, \nROUND((c1.storage_arrays - p1.storage_arrays) / DECODE(p1.storage_arrays,0,NULL,p1.storage_arrays),2) delta_pct,\nABS(ROUND((c1.storage_arrays - p1.storage_arrays) / DECODE(p1.storage_arrays,0,NULL,p1.storage_arrays),2)) pct_delta\nFROM p1, c1\nUNION\nSELECT\n2 sort_order,\n'RAW Capacity'||' ('||var.unit||')' metric,\np1.raw_capacity p_value,\nc1.raw_capacity c_value, \n(c1.raw_capacity - p1.raw_capacity) delta, \nROUND((c1.raw_capacity - p1.raw_capacity) / DECODE(p1.raw_capacity,0,NULL,p1.raw_capacity),2) delta_pct,\nABS(ROUND((c1.raw_capacity - p1.raw_capacity) / DECODE(p1.raw_capacity,0,NULL,p1.raw_capacity),2)) pct_delta\nFROM p1, c1, var\nUNION\nSELECT\n3 sort_order,\n'Allocated Capacity'||' ('||var.unit||')' metric,\np1.allocated p_value,\nc1.allocated c_value, \n(c1.allocated - p1.allocated) delta, \nROUND((c1.allocated - p1.allocated) / DECODE(p1.allocated,0,NULL,p1.allocated),2) delta_pct,\nABS(ROUND((c1.allocated - p1.allocated) / DECODE(p1.allocated,0,NULL,p1.allocated),2)) pct_delta\nFROM p1, c1, var\nUNION\nSELECT\n4 sort_order,\n'Pool Used Capacity'||' ('||var.unit||')' metric,\np1.thin_pool_subscribed p_value,\nc1.thin_pool_subscribed c_value, \n(c1.thin_pool_subscribed - p1.thin_pool_subscribed) delta, \nROUND((c1.thin_pool_subscribed - p1.thin_pool_subscribed) / DECODE(p1.thin_pool_subscribed,0,NULL,p1.thin_pool_subscribed),2) delta_pct,\nABS(ROUND((c1.thin_pool_subscribed - p1.thin_pool_subscribed) / DECODE(p1.thin_pool_subscribed,0,NULL,p1.thin_pool_subscribed),2)) pct_delta\nFROM p1, c1, var"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
