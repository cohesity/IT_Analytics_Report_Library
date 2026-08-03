---
title: "Host Probe CPU Performance Sparklines"
report_id: 1274
rtd_name: "Host Probe CPU Performance Sparklines.rtd"
description: "Host Probe CPU Performance Sparklines"
problem_statement: "For each CPU on a host display MAX(), AVG() and sparklines for Idle, Wait, Nice,User, and System times"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 05/13/2020\nWITH \ncpu AS (--Gather stats for each cpu\nSELECT \n  server_id,\n  cpu_nbr,\n  TRUNC(log_date,DECODE('${freeCombo1}',\n    'Minute','MI',\n    'Hour','HH24',\n    'Day','DD',\n    'Week','WW',\n    'Month','MM',\n    'Quarter','Q',\n    'Year','YYYY')\n  ) AS the_date, \n  MAX(idle_time_pct) AS idle_time_pct,\n  MAX(wait_time_pct) AS wait_time_pct,\n  MAX(nice_priority_time_pct) AS nice_priority_time_pct,\n  MAX(steal_time_pct) AS steal_time_pct,\n  MAX(user_processing_time_pct) AS user_processing_time_pct, \n  MAX(system_processing_time_pct) AS system_processing_time_pct\nFROM \n  apt_v_host_cpu_log cl\nWHERE\n  server_id IN (${hosts})\n  AND log_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY \n  server_id,\n  external_name,\n  cpu_nbr,\n  TRUNC(log_date,DECODE('${freeCombo1}',\n    'Minute','MI',\n    'Hour','HH24',\n    'Day','DD',\n    'Week','WW',\n    'Month','MM',\n    'Quarter','Q',\n    'Year','YYYY')\n  )\nORDER BY \n  3,4\n),\ns1 AS (--Generate Sparklines\nSELECT\n  server_id,\n  cpu_nbr,\n  rtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(idle_time_pct,2)) ORDER BY the_date) AS StringListType),', ') AS idle_time_pct_spk,\n  rtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(wait_time_pct,2)) ORDER BY the_date) AS StringListType),', ') AS wait_time_pct_spk,\n  rtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(nice_priority_time_pct,2)) ORDER BY the_date) AS StringListType),', ') AS nice_priority_time_pct_spk,\n  rtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(steal_time_pct,2)) ORDER BY the_date) AS StringListType),', ') AS steal_time_pct_spk,\n  rtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(user_processing_time_pct,2)) ORDER BY the_date) AS StringListType),', ') AS user_processing_time_pct_spk,\n  rtd.collectString(CAST(COLLECT(TO_CHAR(ROUND(system_processing_time_pct,2)) ORDER BY the_date) AS StringListType),', ') AS system_processing_time_pct_spk\nFROM \n  cpu\nGROUP BY \n  server_id,\n  cpu_nbr\n),\nm1 AS (--get MAX() and AVG() for each\nSELECT\n  server_id,\n  cpu_nbr,\n  MAX(idle_time_pct) AS max_idle_time_pct,\n  MAX(wait_time_pct) AS max_wait_time_pct,\n  MAX(nice_priority_time_pct) AS max_nice_priority_time_pct,\n  MAX(steal_time_pct) AS max_steal_time_pct,\n  MAX(user_processing_time_pct) AS max_user_processing_time_pct, \n  MAX(system_processing_time_pct) AS max_system_processing_time_pct,\n  AVG(idle_time_pct) AS avg_idle_time_pct,\n  AVG(wait_time_pct) AS avg_wait_time_pct,\n  AVG(nice_priority_time_pct) AS avg_nice_priority_time_pct,\n  AVG(steal_time_pct) AS avg_steal_time_pct,\n  AVG(user_processing_time_pct) AS avg_user_processing_time_pct, \n  AVG(system_processing_time_pct) AS avg_system_processing_time_pct\nFROM \n  cpu\nGROUP BY \n  server_id,\n  cpu_nbr\n)\nSELECT\n  s1.server_id,\n  s.display_name,\n  s1.cpu_nbr,\n  s1.idle_time_pct_spk,\n  m1.max_idle_time_pct,\n  m1.avg_idle_time_pct,\n  s1.wait_time_pct_spk,\n  m1.max_wait_time_pct,\n  m1.avg_wait_time_pct,\n  s1.nice_priority_time_pct_spk,\n  m1.max_nice_priority_time_pct,\n  m1.avg_nice_priority_time_pct,\n  s1.steal_time_pct_spk,\n  m1.max_steal_time_pct,\n  m1.avg_steal_time_pct,\n  s1.user_processing_time_pct_spk,\n  m1.max_user_processing_time_pct,\n  m1.avg_user_processing_time_pct,\n  s1.system_processing_time_pct_spk,\n  m1.max_system_processing_time_pct,\n  m1.avg_system_processing_time_pct\nFROM\n  s1, m1, apt_v_server s\nWHERE\n  s1.server_id = m1.server_id\n  AND s1.cpu_nbr = m1.cpu_nbr\n  AND s1.server_id = s.server_id\nORDER BY\n  UPPER(s.display_name), s1.cpu_nbr"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
