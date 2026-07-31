---
title: "NBU Ad Hoc Report Designer"
report_id: 957
rtd_name: "NBU Ad Hoc Report Designer.rtd"
description: "NBU Ad Hoc Report Designer"
problem_statement: ""
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 11/26/2018\n--Report by: Client,Master Server,Media Server,Storage Unit,Policy,Policy Type,Job Type,Schedule,Schedule Type,Try Count\n--On: Job Size(GB),Client Count,File Count,Job Count,Successful Jobs,Partial Jobs,Failed Jobs,MB/sec,Duration(Min)\n--Group By: Day,Week,Month,Quarter,Year\n--\nWITH t1 AS (\nSELECT to_char(trunc(start_date,DECODE('${freeCombo3}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'MM/DD/YY') the_date, \nNVL(DECODE('${freeCombo2}',\n'Client',client_host_name,\n'Master Server',master_host_name,\n'Media Server',media_host_name,\n'Storage Unit',storage_unit_label,\n'Policy',policy_name,\n'Policy Type',policy_type_name,\n'Job Type',job_type_name,\n'Schedule',schedule_name,\n'Schedule Type',schedule_type_name,\n'Try Count',try_count),'None') unit,  \nTRUNC(SUM(kilobytes/1024/1024)) job_size_gb,\nCOUNT(DISTINCT client_id) client_count,\nSUM(nbr_of_files) file_count,\nCOUNT(DISTINCT job_id) job_count,\nSUM(DECODE(summary_status,0,1)) successful_jobs,\nSUM(DECODE(summary_status,1,1)) partial_jobs,\nSUM(DECODE(summary_status,2,1)) failed_jobs,\nAVG(mbytes_sec) mbytes_sec,\nAVG(duration_secs/60) duration_min\nFROM \napt_v_nbu_job_detail\nWHERE \nTRUNC(start_date,DECODE('${freeCombo3}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')) BETWEEN ${startDate} AND trunc(${endDate},DECODE('${freeCombo3}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year'))\nAND client_id in (${hosts})\nGROUP BY \nto_char(trunc(start_date,DECODE('${freeCombo3}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'MM/DD/YY'),\nNVL(DECODE('${freeCombo2}',\n'Client',client_host_name,\n'Master Server',master_host_name,\n'Media Server',media_host_name,\n'Storage Unit',storage_unit_label,\n'Policy',policy_name,\n'Policy Type',policy_type_name,\n'Job Type',job_type_name,\n'Schedule',schedule_name,\n'Schedule Type',schedule_type_name,\n'Try Count',try_count),'None')\n)\nSELECT the_date,\nNVL(unit,'Unknown') unit,\nDECODE('${freeCombo1}',\n'Job Size(GB)',job_size_gb,\n'Client Count',client_count,\n'File Count',file_count,\n'Job Count',job_count,\n'Successful Jobs',successful_jobs,\n'Partial Jobs',partial_jobs,\n'Failed Jobs',failed_jobs,\n'MB/sec',mbytes_sec,\n'Duration(Min)',duration_min\n) the_metric\nFROM \nt1 \nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
