---
title: "TSM Ad Hoc Report Designer"
report_id: 996
rtd_name: "TSM Ad Hoc Report Designer.rtd"
description: "TSM Ad Hoc Report Designer"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 09/22/2011\n--Report On: Job Size(GB),Client Count,File Count,Job Count,Successful Jobs,Partial Jobs,Failed Jobs,MB/sec,Duration(Min),Data Transfer(Min),Media Wait(Min),Idle(Min),Failed Objects,Examined Objects\n--by: TSM Instance,TSM Server,Client,Node,Backup Type,Media type,Domain, Schedule,Storage Pool,Storage Pool Type,Device Class\n--per: Day,Week,Month,Quarter,Year\n--\n--\nWITH t1 AS (\nSELECT trunc(tj.start_date,DECODE('${freeCombo3}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')) the_date, \nDECODE('${freeCombo2}',\n'TSM Instance', tj.instance_name,\n'TSM Server', tj.server_name,\n'Client', tj.client_name,\n'Node', tj.node_name,\n'Backup Type', tj.job_type_name,\n'Media type', tj.media_type,\n'Domain', tj.domain_name,\n'Schedule', tj.schedule_name,\n'Storage Pool', sp.storage_pool_name,\n'Storage Pool Type', sp.storage_pool_type,\n'Device Class', sp.storage_pool_name) unit,  \ntrunc(sum(tj.kilobytes/1024/1024)) job_size_gb,\ncount(DISTINCT tj.client_id) client_count,\nsum(tj.nbr_of_files) file_count,\ncount(DISTINCT tj.job_id) job_count,\nsum(DECODE(tj.summary_status,0,1)) successful_jobs,\nsum(DECODE(tj.summary_status,1,1)) partial_jobs,\nsum(DECODE(tj.summary_status,2,1)) failed_jobs,\navg(tj.mbytes_sec) mbytes_sec,\nsum(tj.duration_secs/60) duration_min,\nsum(tj.data_transfer_secs/60) data_transfer_min,\nsum(tj.media_wait_secs/60) media_wait_min, \nsum(tj.idle_secs/60) idle_min, \nsum(tj.nbr_failed_objects) nbr_failed_objects, \nsum(tj.nbr_examined_objects) nbr_examined_objects\nFROM apt_v_tsm_job tj, apt_v_tsm_storage_pool sp\nWHERE tj.start_date BETWEEN ${startDate} AND ${endDate}\nAND tj.client_id IN (${hosts})\nAND tj.storage_pool_id = sp.storage_pool_id (+)\nGROUP BY trunc(tj.start_date,DECODE('${freeCombo3}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),\nDECODE('${freeCombo2}',\n'TSM Instance', tj.instance_name,\n'TSM Server', tj.server_name,\n'Client', tj.client_name,\n'Node', tj.node_name,\n'Backup Type',tj.job_type_name,\n'Media type', tj.media_type,\n'Domain',tj.domain_name,\n'Schedule',tj.schedule_name,\n'Storage Pool',sp.storage_pool_name,\n'Storage Pool Type',sp.storage_pool_type,\n'Device Class',sp.storage_pool_name)\n) \nSELECT to_char(the_date,'MM/DD/YY') the_date,\nnvl(unit,'Unknown') unit,\nDECODE('${freeCombo1}',\n'Job Size(GB)', job_size_gb,\n'Client Count', client_count,\n'File Count', file_count,\n'Job Count', job_count,\n'Successful Jobs', successful_jobs,\n'Partial Jobs', partial_jobs,\n'Failed Jobs', failed_jobs,\n'MB/sec', mbytes_sec,\n'Duration(Min)', duration_min,\n'Data Transfer(Min)', data_transfer_min,\n'Media Wait(Min)', media_wait_min, \n'Idle(Min)', idle_min, \n'Failed Objects', nbr_failed_objects, \n'Examined Objects', nbr_examined_objects) the_metric\nFROM t1 \nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
