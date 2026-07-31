---
title: "LUN Performance with Sparklines"
report_id: 1197
rtd_name: "LUN Performance Sparklines.rtd"
description: "LUN Performance with Sparklines"
problem_statement: "Ability to see the trendlines of activity for multiple LUNs at once, by using sparklines"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 04/02/2018\nSELECT \nstorage_array_id,\narray_name,\nlogical_unit_id,\nlogical_unit_name,\nrtd.collectString(CAST(COLLECT(TO_CHAR(read_io) ORDER BY log_date) AS StringListType),', ') read_io_spk,\nMAX(read_io) max_read_io,\nAVG(read_io) avg_read_io,\nrtd.collectString(CAST(COLLECT(TO_CHAR(write_io) ORDER BY log_date) AS StringListType),', ') write_io_spk,\nMAX(write_io) max_write_io,\nAVG(write_io) avg_write_io,\nrtd.collectString(CAST(COLLECT(TO_CHAR(total_io) ORDER BY log_date) AS StringListType),', ') total_io_spk,\nMAX(total_io) max_total_io,\nAVG(total_io) avg_total_io,\nrtd.collectString(CAST(COLLECT(TO_CHAR(read_io_response_time) ORDER BY log_date) AS StringListType),', ') read_io_response_spk,\nMAX(read_io_response_time) max_read_io_response,\nAVG(read_io_response_time) avg_read_io_response,\nrtd.collectString(CAST(COLLECT(TO_CHAR(write_io_response_time) ORDER BY log_date) AS StringListType),', ') write_io_response_spk,\nMAX(write_io_response_time) max_write_io_response,\nAVG(write_io_response_time) avg_write_io_response\nFROM aps_v_lun_perform_log pl\nWHERE pl.storage_array_id IN (${arrays})\nAND log_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nstorage_array_id,\narray_name, \nlogical_unit_id,\nlogical_unit_name"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
