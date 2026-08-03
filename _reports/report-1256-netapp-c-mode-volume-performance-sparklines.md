---
title: "NetApp C-Mode Volume Performance Sparklines"
report_id: 1256
rtd_name: "NetApp C-Mode  Volume Performance Sparklines.rtd"
description: "NetApp C-Mode Volume Performance Sparklines"
problem_statement: "For an array or group of array show me the daily performance stats for each Volume over a given time period"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 11/28/2018\nWITH \nt1 AS (\nSELECT\nTRUNC(log_date) log_date,\nntc_storage_system_id,\narray_name,\nntc_volume_id,\nvolume_name,\nMAX(read_latency_ms) max_read_latency_ms,\nMAX(read_BPS) max_read_BPS,\nMAX(read_OPS) max_read_OPS\nFROM \naps_v_ntc_volume_perform_log\nWHERE\nntc_storage_system_id IN (${arrays})\nAND log_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nTRUNC(log_date),\nntc_storage_system_id,\narray_name,\nntc_volume_id,\nvolume_name\nORDER BY\n1 DESC\n),\nt2 AS (\nSELECT\nntc_storage_system_id,\narray_name,\nntc_volume_id,\nvolume_name,\nMIN(log_date) min_log_date,\nMAX(log_date) max_log_date,\nAVG(max_read_latency_ms) avg_read_latency_ms,\nMAX(max_read_latency_ms) max_read_latency_ms,\nrtd.collectString(CAST(COLLECT(TO_CHAR(max_read_latency_ms) ORDER BY log_date) AS StringListType),', ') read_latency_spk,\nROUND(AVG(max_read_BPS/1024),2) avg_read_MPS,\nROUND(MAX(max_read_BPS/1024),2) max_read_MPS,\nrtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(max_read_BPS/1024,2)) ORDER BY log_date) AS StringListType),', ') read_MPS_spk,\nAVG(max_read_OPS) avg_read_OPS,\nMAX(max_read_OPS) max_read_OPS,\nrtd.collectString(CAST(COLLECT(TO_CHAR(max_read_OPS) ORDER BY log_date) AS StringListType),', ') read_OPS_spk\nFROM t1\nGROUP BY \nntc_storage_system_id,\narray_name,\nntc_volume_id,\nvolume_name\n)\nSELECT\nntc_storage_system_id,\narray_name,\nntc_volume_id,\nvolume_name,\nmin_log_date,\nmax_log_date,\n--Convert dates to unix timestamps for the drilldown\nROUND((min_log_date - TO_DATE('1970-01-01','YYYY-MM-DD')) * 60 * 60 * 24) start_date,\nROUND((max_log_date - TO_DATE('1970-01-01','YYYY-MM-DD')) * 60 * 60 * 24)  end_date,\navg_read_latency_ms,\nmax_read_latency_ms,\nread_latency_spk,\navg_read_MPS,\nmax_read_MPS,\nread_MPS_spk,\navg_read_OPS,\nmax_read_OPS,\nread_OPS_spk\nFROM t2"
has_explanation: false
products: [{"slug": "capacity-manager-netapp-c-mode", "name": "NetApp C-Mode"}]
categories: []
product_slugs: ["capacity-manager-netapp-c-mode"]
category_slugs: []
---
