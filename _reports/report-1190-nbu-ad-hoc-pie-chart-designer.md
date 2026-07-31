---
title: "NBU Ad Hoc Pie Chart Designer"
report_id: 1190
rtd_name: "NBU Ad Hoc Pie Chart Designer.rtd"
description: "NBU Ad Hoc Pie Chart Designer"
problem_statement: ""
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@veritas.com\n--Last Modified: 08/22/2019\n-- Report by: Client,Master Server,Media Server,Storage Unit,Policy,Policy Type,Job Type,Schedule,Schedule Type,Try Count\n-- On: Job Size(GB),Client Count,File Count,Job Count,Successful Jobs,Partial Jobs,Failed Jobs,MB/sec,Duration(Min)\n-- Group By: Day,Week,Month,Quarter,Year\n--\n--\nWITH t1 as (\nSELECT\nNVL(DECODE('${freeCombo1}',\n'Client',client_host_name,\n'Master Server',master_host_name,\n'Media Server',media_host_name,\n'Storage Unit',storage_unit_label,\n'Policy',policy_name,\n'Policy Type',policy_type_name,\n'Job Type',job_type_name,\n'Schedule',schedule_name,\n'Schedule Type',schedule_type_name,\n'Try Count',try_count),'None') unit,  \ntrunc(sum(kilobytes/1024/1024)) job_size_gb,\ncount(DISTINCT client_id) client_count,\nsum(nbr_of_files) file_count,\ncount(DISTINCT job_id) job_count,\nsum(DECODE(summary_status,0,1)) successful_jobs,\nsum(DECODE(summary_status,1,1)) partial_jobs,\nsum(DECODE(summary_status,2,1)) failed_jobs,\navg(mbytes_sec) mbytes_sec,\navg(duration_secs/60) duration_min\nFROM apt_v_nbu_job_detail\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND client_id in (${hosts})\nGROUP BY\nNVL(DECODE('${freeCombo1}',\n'Client',client_host_name,\n'Master Server',master_host_name,\n'Media Server',media_host_name,\n'Storage Unit',storage_unit_label,\n'Policy',policy_name,\n'Policy Type',policy_type_name,\n'Job Type',job_type_name,\n'Schedule',schedule_name,\n'Schedule Type',schedule_type_name,\n'Try Count',try_count),'None')\n),\nt2 AS (\nSELECT\nnvl(unit,'Unknown') unit,\nDECODE('${freeCombo2}',\n'Job Size(GB)',job_size_gb,\n'Client Count',client_count,\n'File Count',file_count,\n'Job Count',job_count,\n'Successful Jobs',successful_jobs,\n'Partial Jobs',partial_jobs,\n'Failed Jobs',failed_jobs,\n'MB/sec',mbytes_sec,\n'Duration(Min)',duration_min\n) the_metric\nFROM t1 \nORDER BY 2 DESC\n)\nSELECT\nunit,the_metric\nFROM t2\nWHERE ROWNUM <= ${freeCombo3}"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
