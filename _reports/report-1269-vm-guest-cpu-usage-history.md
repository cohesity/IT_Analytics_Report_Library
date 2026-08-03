---
title: "VM Guest CPU Usage History"
report_id: 1269
rtd_name: "VM Guest CPU Usage History.rtd"
description: "VM Guest CPU Usage History"
problem_statement: "TBD"
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
sql_query: "--Author: rich.rose@veritas.com\n--Last Modified: 03/26/2020\nWITH \nvar AS (\nSELECT \n  DECODE('${freeCombo2}','Minutes',1,'Hours',1,'Days',1,'Weeks',7,'Months',31,'Quarters',93,'Years',365.25) AS the_multiplier,\n  TO_NUMBER('${freeCombo3}') AS forecast_periods\nFROM apt_v_dual\n), \nc1 AS (\nSELECT\n  TRUNC(l.end_log_date,DECODE('${freeCombo2}','Minutes','MI','Hours','HH24','Days','DD','Weeks','WW','Months','MM','Quarters','Q','Years')) AS the_date,\n  p.partition_id, \n  p.partition_name, \n  ROUND(AVG(NVL(l.avg_cpu_usage_mhz,0)/1000),2) avg_cpu_usage_ghz, --MHz converted to GHz\n  ROUND(AVG(NVL(l.avg_cpu_usage_pct,0)),2) avg_cpu_usage_pct,\n  ROUND(AVG(NVL(l.avg_cpu_wait_ms,0)),2) avg_cpu_wait_ms,\n  ROUND(AVG(NVL(l.avg_cpu_ready_ms,0)),2) avg_cpu_ready_ms,\n  ROUND(MAX(NVL(l.avg_cpu_usage_mhz,0)/1000),2) max_cpu_usage_ghz, --MHz converted to GHz\n  ROUND(MAX(NVL(l.avg_cpu_usage_pct,0)),2) max_cpu_usage_pct,\n  ROUND(MAX(NVL(l.avg_cpu_wait_ms,0)),2) max_cpu_wait_ms,\n  ROUND(MAX(NVL(l.avg_cpu_ready_ms,0)),2) max_cpu_ready_ms\nFROM \n  apt_v_vmw_perform_cpu_log l, apt_v_partition p\nWHERE \n  p.partition_id IN (${vmGuests})\n  AND p.partition_id = l.partition_id\n  AND l.end_log_date  BETWEEN ${startDate} AND ${endDate}\n  AND p.collection_status != 3\n  AND p.partition_type = 'VM'\nGROUP BY \n  TRUNC(l.end_log_date,DECODE('${freeCombo2}','Minutes','MI','Hours','HH24','Days','DD','Weeks','WW','Months','MM','Quarters','Q','Years')),\n  p.partition_id, \n  p.partition_name \n)\nSELECT\n  TO_CHAR(the_date,'YYYY/MM/DD HH24:MI') the_date,\n  DECODE('${freeCombo1}',\n    'CPU Usage (GHz)',AVG(avg_cpu_usage_ghz),\n    'CPU Usage%',AVG(avg_cpu_usage_pct),\n    'CPU Wait (ms)',AVG(avg_cpu_wait_ms),\n    'CPU Ready (ms)',AVG(avg_cpu_ready_ms)\n  ) AS avg_the_metric,\n  DECODE('${freeCombo1}',\n    'CPU Usage (GHz)',MAX(max_cpu_usage_ghz),\n    'CPU Usage%',MAX(max_cpu_usage_pct),\n    'CPU Wait (ms)',MAX(max_cpu_wait_ms),\n    'CPU Ready (ms)',MAX(max_cpu_ready_ms)\n  ) AS max_the_metric\nFROM \n  c1\nGROUP BY\n  TO_CHAR(the_date,'YYYY/MM/DD HH24:MI')\nORDER BY \n  the_date"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
