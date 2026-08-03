---
title: "Compare backup statistics across 3 different backup servers"
report_id: 1137
rtd_name: "3 Backup Server Comparison.rtd"
description: "Compare backup statistics across 3 different backup servers"
problem_statement: "I have multiple backup servers and I need an easy way to compare what is being done by each one."
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
sql_query: "WITH \nt1 AS (\nSELECT\nto_char(trunc(start_date,DECODE('${freeCombo2}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY') the_date,\nto_char(trunc(start_date,DECODE('${freeCombo2}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDD') sort_order,\nserver_name entity,\ntrunc(SUM(kilobytes/1024/1024)) job_size_gb,\nCOUNT(DISTINCT client_id) client_count,\nSUM(nbr_of_files) file_count,\nCOUNT(DISTINCT job_id) job_count,\nSUM(DECODE(summary_status,0,1)) successful_jobs,\nSUM(DECODE(summary_status,1,1)) partial_jobs,\nSUM(DECODE(summary_status,2,1)) failed_jobs,\nAVG(mbytes_sec) mbytes_sec,\nAVG(duration_secs/60) duration_min\nFROM apt_v_job\nWHERE \nserver_name IN ('${queryCombo1}','${queryCombo2}','${queryCombo3}')\nAND start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nto_char(trunc(start_date,DECODE('${freeCombo2}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY'),\nto_char(trunc(start_date,DECODE('${freeCombo2}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDD'),\nserver_name\n),\nt2 AS (\nSELECT\nthe_date,\nsort_order,\nentity,\nDECODE('${freeCombo1}',\n'Job Size(GB)',job_size_gb,\n'Client Count',client_COUNT,\n'File Count',file_COUNT,\n'Job Count',job_COUNT,\n'Successful Jobs',successful_jobs,\n'Partial Jobs',partial_jobs,\n'Failed Jobs',failed_jobs,\n'MB/sec',mbytes_sec,\n'Duration(Min)',duration_MIN\n) metric\nFROM t1\n),\nt3 AS (\nSELECT\nthe_date,\nsort_order,\nSUM(DECODE(entity,'${queryCombo1}',metric,0)) metric1,\nSUM(DECODE(entity,'${queryCombo2}',metric,0)) metric2,\nSUM(DECODE(entity,'${queryCombo3}',metric,0)) metric3\nFROM t2\nGROUP BY \nthe_date,\nsort_order\n)\nSELECT\nthe_date,\nsort_order,\n'${freeCombo1}' report_on,\n'${queryCombo1}' entity1,\nmetric1,\n'${queryCombo2}' entity2,\nmetric2,\n'${queryCombo3}' entity3,\nmetric3\nFROM t3\nORDER BY sort_order"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
