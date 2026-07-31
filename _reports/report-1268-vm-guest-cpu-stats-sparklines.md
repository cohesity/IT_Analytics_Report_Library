---
title: "VM Guest CPU Stats Sparklines"
report_id: 1268
rtd_name: "VM Guest CPU Stats Sparklines.rtd"
description: "VM Guest CPU Stats Sparklines"
problem_statement: "Soon"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@veritas.com\n--Last Modified: 03/25/2020\nWITH \nc1 AS (\nSELECT\n  TRUNC(l.end_log_date,DECODE('${freeCombo1}','Minutes','MI','Hours','HH24','Days','DD','Weeks','WW','Months','MM','Quarters','Q','Years')) AS the_date,\n  p.partition_id,\n  p.partition_name,\n  ROUND(MAX(NVL(l.avg_cpu_usage_mhz,0)/1000),2) cpu_usage_ghz, --MHz converted to GHz\n  ROUND(MAX(NVL(l.avg_cpu_usage_pct,0)),2) cpu_usage_pct,\n  ROUND(MAX(NVL(l.avg_cpu_wait_ms,0)),2) cpu_wait_ms,\n  ROUND(MAX(NVL(l.avg_cpu_ready_ms,0)),2) cpu_ready_ms\nFROM \n  apt_v_vmw_perform_cpu_log l, apt_v_partition p\nWHERE \n  p.partition_id IN (${vmGuests})\n  AND p.partition_id = l.partition_id\n  AND l.end_log_date  BETWEEN ${startDate} AND ${endDate}\n  AND p.collection_status != 3\n  AND p.partition_type = 'VM'\nGROUP BY \n  TRUNC(l.end_log_date,DECODE('${freeCombo1}','Minutes','MI','Hours','HH24','Days','DD','Weeks','WW','Months','MM','Quarters','Q','Years')),\n  p.partition_id,\n  p.partition_name\n),\ns1 AS (--Generate Sparklines\nSELECT\n  c1.partition_id,\n  c1.partition_name,\n  rtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(cpu_usage_ghz,2)) ORDER BY the_date) AS StringListType),', ') AS cpu_usage_ghz_spk,\n  rtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(cpu_usage_pct,2)) ORDER BY the_date) AS StringListType),', ') AS cpu_usage_pct_spk,\n  rtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(cpu_wait_ms,2)) ORDER BY the_date) AS StringListType),', ') AS cpu_wait_ms_spk,\n  rtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(cpu_ready_ms,2)) ORDER BY the_date) AS StringListType),', ') AS cpu_ready_ms_spk\nFROM \n  c1\nGROUP BY \n  c1.partition_id,\n  c1.partition_name\n),\nt1 AS (\nSELECT\n  c1.partition_id,\n  MAX(c1.cpu_usage_ghz) AS max_cpu_usage_ghz,\n  MAX(c1.cpu_usage_pct) AS max_cpu_usage_pct,\n  MAX(c1.cpu_wait_ms) AS max_cpu_wait_ms,\n  MAX(c1.cpu_ready_ms) AS max_cpu_ready_ms,\n  AVG(c1.cpu_usage_ghz) AS avg_cpu_usage_ghz,\n  AVG(c1.cpu_usage_pct) AS avg_cpu_usage_pct,\n  AVG(c1.cpu_wait_ms) AS avg_cpu_wait_ms,\n  AVG(c1.cpu_ready_ms) AS avg_cpu_ready_ms\nFROM\n  c1\nGROUP BY \n  c1.partition_id\nORDER BY \n  2 DESC\n),\nt2 AS (\nSELECT\n  s1.partition_id,\n  s1.partition_name,\n  s1.cpu_usage_ghz_spk,\n  t1.max_cpu_usage_ghz,\n  t1.avg_cpu_usage_ghz,\n  s1.cpu_usage_pct_spk,\n  t1.max_cpu_usage_pct,\n  t1.avg_cpu_usage_pct,\n  s1.cpu_wait_ms_spk,\n  t1.max_cpu_wait_ms,\n  t1.avg_cpu_wait_ms,\n  s1.cpu_ready_ms_spk,\n  t1.max_cpu_ready_ms,\n  t1.avg_cpu_ready_ms\nFROM\n  s1, t1\nWHERE\n  s1.partition_id = t1.partition_id\nORDER BY t1.max_cpu_usage_ghz DESC\n)\nSELECT \n  *\nFROM \n  t2\nWHERE \n  ROWNUM <= ${freeCombo2}\nORDER BY \n max_cpu_usage_ghz DESC"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
