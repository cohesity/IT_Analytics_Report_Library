---
title: "NetApp C-Mode Hot LUNs Top 10 I/O"
report_id: 1257
rtd_name: "NetApp C-Mode Hot LUNs Top 10 I_O.rtd"
description: "NetApp C-Mode Hot LUNs Top 10 I/O"
problem_statement: "Show me which NetApp LUNS are performing the worst or have a spike of 5x what they normally do"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 11/02/2018\nWITH \nvar AS (\nSELECT \nDECODE('${freeCombo2}','Total IO',1,'Read IO',2,'Write IO',3,'Read Latency',5,'Write Latency',6) top_by,\nDECODE('${freeCombo3}','1x',1,'5x',5,'10x',10,'15x',15,'20x',20,'25x',25,'30x',30,'35x',35,'40x',40,'45x',45,'50x',50,'55x',55,'60x',60,'65x',65,'70x',70,'75x',75,'80x',80,'85x',85,'90x',90,'95x',95,'100x',100) threshold\nFROM\napt_v_dual\n),\nt1 AS (\nSELECT \nstorage_array_id,\narray_name,\nlogical_unit_id,\nlogical_unit_name,\nMAX(read_io) max_read_io,\nAVG(read_io) avg_read_io,\nMAX(write_io) max_write_io,\nAVG(write_io) avg_write_io,\nMAX(total_io) max_total_io,\nAVG(total_io) avg_total_io,\nMAX(read_io_response_time) max_read_io_response,\nAVG(read_io_response_time) avg_read_io_response,\nMAX(write_io_response_time) max_write_io_response,\nAVG(write_io_response_time) avg_write_io_response,\nMAX(total_io_response_time) max_total_io_response,\nAVG(total_io_response_time) avg_total_io_response\nFROM aps_v_lun_perform_log pl, var\nWHERE pl.storage_array_id IN (${arrays})\nAND log_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nstorage_array_id,\narray_name, \nlogical_unit_id,\nlogical_unit_name\nORDER BY \nDECODE('${freeCombo2}','Total IO',MAX(total_io),'Read IO',MAX(read_io),'Write IO',MAX(write_io),'Read Latency',MAX(read_io_response_time),'Write Latency',MAX(write_io_response_time))  DESC\n)\nSELECT \nt1.storage_array_id,\nt1.array_name,\nt1.logical_unit_id,\nt1.logical_unit_name,\nt1.avg_read_io,\nt1.max_read_io,\n(max_read_io / DECODE(avg_read_io,0,NULL,avg_read_io)) moa_read_io,\nCASE \nWHEN(max_read_io / DECODE(avg_read_io,0,NULL,avg_read_io)) > threshold  THEN 'red' \nWHEN(max_read_io / DECODE(avg_read_io,0,NULL,avg_read_io)) < threshold  THEN 'green'\nELSE 'white'\nEND read_io_dot,\nt1.avg_write_io,\nt1.max_write_io,\n(max_write_io / DECODE(avg_write_io,0,NULL,avg_write_io)) moa_write_io,\nCASE \nWHEN(max_write_io / DECODE(avg_write_io,0,NULL,avg_write_io)) > threshold  THEN 'red' \nWHEN(max_write_io / DECODE(avg_write_io,0,NULL,avg_write_io)) < threshold  THEN 'green'\nELSE 'white' \nEND write_io_dot,\nt1.avg_read_io_response,\nt1.max_read_io_response,\n(max_read_io_response / DECODE(avg_read_io_response,0,NULL,avg_read_io_response)) moa_read_io_response,\nCASE \nWHEN(max_read_io_response / DECODE(avg_read_io_response,0,NULL,avg_read_io_response)) > threshold  THEN 'red' \nWHEN(max_read_io_response / DECODE(avg_read_io_response,0,NULL,avg_read_io_response)) < threshold  THEN 'green' \nELSE 'white' \nEND read_io_response_dot,\nt1.avg_write_io_response,\nt1.max_write_io_response,\n(max_write_io_response / DECODE(avg_write_io_response,0,NULL,avg_write_io_response)) moa_write_io_response,\nCASE \nWHEN(max_write_io_response / DECODE(avg_write_io_response,0,NULL,avg_write_io_response)) > threshold  THEN 'red' \nWHEN(max_write_io_response / DECODE(avg_write_io_response,0,NULL,avg_write_io_response)) < threshold  THEN 'green' \nELSE 'white' \nEND write_io_response_dot,\nt1.avg_total_io_response,\nt1.max_total_io_response,\n(max_total_io_response / DECODE(avg_total_io_response,0,NULL,avg_total_io_response)) moa_total_io_response,\nCASE \nWHEN(max_total_io_response / DECODE(avg_total_io_response,0,NULL,avg_total_io_response)) > threshold  THEN 'red' \nWHEN(max_total_io_response / DECODE(avg_total_io_response,0,NULL,avg_total_io_response)) < threshold  THEN 'green' \nELSE 'white' \nEND total_io_response_dot\nFROM t1, var\nWHERE \nROWNUM <= ${freeCombo1}\nORDER BY \nDECODE('${freeCombo2}','Read IO',max_read_io,'Write IO',max_write_io,'Read Latency',max_read_io_response,'Write Latency',max_write_io_response)  DESC"
has_explanation: false
products: [{"slug": "capacity-manager-netapp-c-mode", "name": "NetApp C-Mode"}]
categories: []
product_slugs: ["capacity-manager-netapp-c-mode"]
category_slugs: []
---
