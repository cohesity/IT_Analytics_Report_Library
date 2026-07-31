---
title: "VM Guest Memory Stats Sparklines"
report_id: 1272
rtd_name: "VM Guest Memory Stats Sparklines.rtd"
description: "VM Guest Memory Stats Sparklines"
problem_statement: ""
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@veritas.com\n--Last Modified: 04/01/2020\nWITH \nc1 AS (\nSELECT\n  TRUNC(l.end_log_date,DECODE('${freeCombo1}','Minutes','MI','Hours','HH24','Days','DD','Weeks','WW','Months','MM','Quarters','Q','Years')) AS the_date,\n  p.partition_id,\n  p.partition_name,\n  ROUND(MAX(NVL(l.avg_memory_usage_kb/1024,0)/1000),2) mem_usage_gb,\n  ROUND(MAX(NVL(l.avg_memory_usage_pct,0)),2) mem_usage_pct\nFROM \n  apt_v_vmw_perform_memory_log l, apt_v_partition p\nWHERE \n  p.partition_id IN (${vmGuests})\n  AND p.partition_id = l.partition_id\n  AND l.end_log_date  BETWEEN ${startDate} AND ${endDate}\n  AND p.collection_status != 3\n  AND p.partition_type = 'VM'\nGROUP BY \n  TRUNC(l.end_log_date,DECODE('${freeCombo1}','Minutes','MI','Hours','HH24','Days','DD','Weeks','WW','Months','MM','Quarters','Q','Years')),\n  p.partition_id,\n  p.partition_name\n),\ns1 AS (--Generate Sparklines\nSELECT\n  c1.partition_id,\n  c1.partition_name,\n  rtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(mem_usage_gb,2)) ORDER BY the_date) AS StringListType),', ') AS mem_usage_gb_spk,\n  rtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(mem_usage_pct,2)) ORDER BY the_date) AS StringListType),', ') AS mem_usage_pct_spk\nFROM \n  c1\nGROUP BY \n  c1.partition_id,\n  c1.partition_name\n),\nt1 AS (\nSELECT\n  c1.partition_id,\n  MAX(c1.mem_usage_gb) AS max_mem_usage_gb,\n  MAX(c1.mem_usage_pct) AS max_mem_usage_pct,\n  AVG(c1.mem_usage_gb) AS avg_mem_usage_gb,\n  AVG(c1.mem_usage_pct) AS avg_mem_usage_pct\nFROM\n  c1\nGROUP BY \n  c1.partition_id\n),\nt2 AS (\nSELECT\n  s1.partition_id,\n  s1.partition_name,\n  s1.mem_usage_gb_spk,\n  t1.max_mem_usage_gb,\n  t1.avg_mem_usage_gb,\n  s1.mem_usage_pct_spk,\n  t1.max_mem_usage_pct,\n  t1.avg_mem_usage_pct\nFROM\n  s1, t1\nWHERE\n  s1.partition_id = t1.partition_id\nORDER BY \n  t1.max_mem_usage_gb DESC\n)\nSELECT *\nFROM t2\nWHERE\n  rownum <= ${freeCombo2}"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
