---
title: "Networker Ad Hoc Report Designer"
report_id: 885
rtd_name: "Legato Ad Hoc Report Designer.rtd"
description: "Legato Ad Hoc Report Designer"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "-- Author: rich.rose@aptare.com\n-- Last Updated: 09/22/2011\n-- Produces many different kinds of reports based on Legato Jobs\n--\n--\n-- Report on: Job Size(GB),Client Count,File Count,Job Count,Successful Jobs,Partial Jobs,Failed Jobs,MB/sec,Duration(Min)\n-- by: Legato Server,Client,Client Resource,Saveset,Saveset Group,Job Type,Schedule,Directive,File Paths,Client Version,Networker Version,Retention Period,Retention Period Type,Browse Period,Browse Period Type\n-- per: Day,Week,Month,Quarter,Year\nWITH t1 as (\nSELECT trunc(lj.start_date,DECODE('${freeCombo3}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')) the_date, \nDECODE('${freeCombo2}',\n'Legato Server', lj.server_name,\n'Client', lj.client_name,\n'Client Resource', lj.client_resource_name,\n'Saveset', lj.saveset_name,\n'Saveset Group', lj.saveset_group_name,\n'Job Type', lj.job_type_name,\n'Schedule', cr.schedule_name,\n'Directive', cr.directive_name,\n'File Paths', cr.file_paths,\n'Client Version', cr.client_software_version,\n'Networker Version', cr.networker_version,\n'Retention Period', cr.retention_period_name,\n'Retention Period Type', cr.retention_period_type,\n'Browse Period', cr.browse_period_name,\n'Browse Period Type', cr.browse_period_type) unit,  \ntrunc(sum(lj.kilobytes/1024/1024)) job_size_gb,\ncount(DISTINCT lj.client_id) client_count,\nsum(lj.nbr_of_files) file_count,\ncount(DISTINCT lj.job_id) job_count,\nsum(DECODE(lj.summary_status,0,1)) successful_jobs,\nsum(DECODE(lj.summary_status,1,1)) partial_jobs,\nsum(DECODE(lj.summary_status,2,1)) failed_jobs,\navg(j.mbytes_sec) mbytes_sec,\navg(j.duration_secs/60) duration_min\nFROM apt_v_job j, apt_v_leg_job lj, apt_v_leg_client_resource cr\nWHERE lj.start_date BETWEEN ${startDate} AND ${endDate}\nAND lj.client_id in (${hosts})\nAND lj.job_id = j.job_id\nAND lj.client_resource_id = cr.client_resource_id\nGROUP BY trunc(lj.start_date,DECODE('${freeCombo3}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),\nDECODE('${freeCombo2}',\n'Legato Server',lj.server_name,\n'Client',lj.client_name,\n'Client Resource',lj.client_resource_name,\n'Saveset',lj.saveset_name,\n'Saveset Group',lj.saveset_group_name,\n'Job Type',lj.job_type_name,\n'Schedule',cr.schedule_name,\n'Directive',cr.directive_name,\n'File Paths',cr.file_paths,\n'Client Version',cr.client_software_version,\n'Networker Version',cr.networker_version,\n'Retention Period',cr.retention_period_name,\n'Retention Period Type',cr.retention_period_type,\n'Browse Period',cr.browse_period_name,\n'Browse Period Type',cr.browse_period_type)\n) \nSELECT to_char(the_date,'MM/DD/YY') the_date,\nnvl(unit,'Unknown') unit,\nDECODE('${freeCombo1}',\n'Job Size(GB)',job_size_gb,\n'Client Count',client_count,\n'File Count',file_count,\n'Job Count',job_count,\n'Successful Jobs',successful_jobs,\n'Partial Jobs',partial_jobs,\n'Failed Jobs',failed_jobs,\n'MB/sec',mbytes_sec,\n'Duration(Min)',duration_min\n) the_metric\nFROM t1 \nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-emc-networker-legato", "name": "EMC NetWorker (Legato)"}]
categories: []
product_slugs: ["backup-manager-emc-networker-legato"]
category_slugs: []
---
