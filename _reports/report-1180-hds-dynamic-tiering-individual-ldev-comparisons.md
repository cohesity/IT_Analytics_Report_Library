---
title: "HDS Dynamic Tiering Individual LDEV Comparisons"
report_id: 1180
rtd_name: "HDS Dynamic Tiering Individual LDEV History Comparison.rtd"
description: "HDS Dynamic Tiering Individual LDEV Comparisons"
problem_statement: "HDT"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/28/2017\nWITH\nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays, \n${startDate} startDate, \nDECODE('${freeCombo1}', 'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual \n),\nt1 AS (\nSELECT\nll.storage_array_id,\nll.array_name,\nll.ldev_id,\nl.label,\nTRUNC(ll.log_date,'HH24') the_date,\nMAX(ll.dp_tier0_consumed_kb/div_by) max_tier0,\nMAX(ll.dp_tier1_consumed_kb/div_by) max_tier1,\nMAX(ll.dp_tier2_consumed_kb/div_by) max_tier2\nFROM aps_v_hds_ldev_log ll, aps_v_hds_ldev l, var\nWHERE \nll.storage_array_id IN (${arrays})\nAND ll.ldev_id = l.ldev_id\nAND ll.log_date BETWEEN ${startDate} AND ${endDate}\nAND ll.dp_tier0_consumed_kb+ll.dp_tier2_consumed_kb+ll.dp_tier2_consumed_kb > 0\nGROUP BY\nll.storage_array_id,\nll.array_name,\nll.ldev_id,\nl.label,\nTRUNC(ll.log_date,'HH24')\nORDER BY 1\n),\nt2 AS (--Get the values of the first and last periods to caclulate deltas\nSELECT DISTINCT\nstorage_array_id,\nldev_id,\nFIRST_VALUE(max_tier0) OVER (PARTITION BY storage_array_id, ldev_id ORDER BY the_date ASC) first_tier0, \nFIRST_VALUE(max_tier0) OVER (PARTITION BY storage_array_id, ldev_id ORDER BY the_date DESC) last_tier0,\nFIRST_VALUE(max_tier1) OVER (PARTITION BY storage_array_id, ldev_id ORDER BY the_date ASC) first_tier1, \nFIRST_VALUE(max_tier1) OVER (PARTITION BY storage_array_id, ldev_id ORDER BY the_date DESC) last_tier1,\nFIRST_VALUE(max_tier2) OVER (PARTITION BY storage_array_id, ldev_id ORDER BY the_date ASC) first_tier2, \nFIRST_VALUE(max_tier2) OVER (PARTITION BY storage_array_id, ldev_id ORDER BY the_date DESC) last_tier2\nFROM T1\n),\nt3 AS (--Build the sparlines \nSELECT \nstorage_array_id,\narray_name,\nldev_id,\nlabel,\nMIN(the_date) first_sample,\nMAX(the_date) last_sample,\nCOUNT(the_date) sample_count,\nMAX(max_tier0) max_tier0,\nrtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(max_tier0,2)) ORDER BY the_date) AS StringListType),', ') spk_tier0,\nMAX(max_tier1) max_tier1,\nrtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(max_tier1,2)) ORDER BY the_date) AS StringListType),', ') spk_tier1,\nMAX(max_tier2) max_tier2,\nrtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(max_tier2,2)) ORDER BY the_date) AS StringListType),', ') spk_tier2\nFROM t1\nGROUP BY\nstorage_array_id,\narray_name,\nldev_id,\nlabel\n)\nSELECT\nt3.storage_array_id,\nt3.array_name,\nt3.ldev_id,\nt3.label,\nt3.first_sample,\nt3.last_sample,\nt3.sample_count,\n--Tier 0\nt3.max_tier0,\nt2.first_tier0,\nt2.last_tier0,\nt2.first_tier0 - t2.last_tier0 delta_t0,\nt3.spk_tier0,\n--Tier 1\nt3.max_tier1,\nt2.first_tier1,\nt2.last_tier1,\nt2.first_tier1 - t2.last_tier1 delta_t1,\nt3.spk_tier1,\n--Tier 2\nt3.max_tier2,\nt2.first_tier2,\nt2.last_tier2,\nt2.first_tier2 - t2.last_tier2 delta_t2,\nt3.spk_tier2\nFROM \nt2, t3\nWHERE \nt2.storage_array_id = t3.storage_array_id\nAND t2.ldev_id = t3.ldev_id\nAND (ABS(ROUND(t2.first_tier0)-ROUND(t2.last_tier0)) > DECODE('${freeCombo2}','Only LDEVs that changed',0, -1))\nORDER BY \nABS(t2.first_tier0 - t2.last_tier0) DESC"
has_explanation: false
products: [{"slug": "capacity-manager-hds-reports", "name": "HDS Reports"}]
categories: []
product_slugs: ["capacity-manager-hds-reports"]
category_slugs: []
---
