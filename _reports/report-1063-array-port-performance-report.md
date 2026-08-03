---
title: "Array Port Performance Report"
report_id: 1063
rtd_name: "Array Port Performance Report.rtd"
description: "Array Port Performance Report"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 11/16/2012\nSELECT \ne.storage_Array_id,array_name,\ni.port_id,port_name,port_wwn_id,port_role,\nROUND(SUM(diff_total_io)/SUM(((log_date-prev_log_date )*86400))) total_io,\nRATIO_TO_REPORT(SUM(diff_total_io)/SUM(((log_date-prev_log_date )*86400))) OVER(PARTITION BY e.storage_array_id)*100 total_io_pct,\nROUND(SUM((diff_kbytes_transferred)/1024),2) mb_transferred, \nRATIO_TO_REPORT(SUM((diff_kbytes_transferred/1024))) OVER(PARTITION BY e.storage_array_id)*100 MB_transferred_pct\nFROM aps_v_array_port_stats_log l,aps_v_array_port i, aps_v_storage_array e\nWHERE i.storage_array_id = e.storage_array_id\nAND i.port_id = l.port_id(+)\nAND l.log_date(+) BETWEEN ${startDate} AND ${endDate}\nAND array_name = '${queryCombo1}'\nGROUP BY e.storage_Array_id,array_name,\ni.port_id,port_name,port_wwn_id,port_role\nORDER BY 2,4"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
