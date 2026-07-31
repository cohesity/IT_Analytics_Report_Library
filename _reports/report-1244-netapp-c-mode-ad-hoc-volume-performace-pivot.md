---
title: "NetApp C-Mode Ad Hoc Volume Performace Pivot"
report_id: 1244
rtd_name: "NetApp C Ad Hoc Volume Performance Pivot.rtd"
description: "NetApp C-Mode Ad Hoc Volume Performace Pivot"
problem_statement: "I want to see the daily performance of my NetApp volumes over a period of time so I can tell which ones are most active.  It has to be in a pivot table format so I can see multiple array/volume combinations.  I also want to be able to look at different metrics like: Avg_Latency_ms, Avg_Other_Latency_ms, Other_OPS, Read_BPS, Read_Latency_ms, Read_OPS, Total_OPS, Write_BPS, Write_Latency_ms, Write_OPS"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 10/22/2018\nSELECT\nTO_CHAR(TRUNC(log_date),'MM/DD/YY') log_date,\narray_name||' - '||volume_name array_volume,\nMAX(${freeCombo1}) the_metric\nFROM \naps_v_ntc_volume_perform_log\nWHERE\nntc_storage_system_id IN (${arrays})\nAND log_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nTO_CHAR(TRUNC(log_date),'MM/DD/YY'),\narray_name||' - '||volume_name\nORDER BY\n1 DESC"
has_explanation: false
products: [{"slug": "capacity-manager-netapp-c-mode", "name": "NetApp C-Mode"}]
categories: []
product_slugs: ["capacity-manager-netapp-c-mode"]
category_slugs: []
---
