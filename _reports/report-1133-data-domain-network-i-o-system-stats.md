---
title: "Data Domain Network I/O System Stats"
report_id: 1133
rtd_name: "Data Domain Network I_O System Stats.rtd"
description: "Data Domain Network I/O System Stats"
problem_statement: "I need to see the short term and long term trends of the network I/O of my Data Domain to help in troubleshooting, load balancing, finding bottlenecks and provide information to affect future purchases."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 12/10/2014\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo2}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT\nto_char(trunc(collection_time,DECODE('${freeCombo1}','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY HH24') the_date,\nto_char(trunc(collection_time,DECODE('${freeCombo1}','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24') sort_order,\nROUND(MAX(cpu_avg_pct_busy),2) cpu_avg_pct_busy,\nROUND(MAX(cpu_max_pct_busy),2) cpu_max_pct_busy,\nROUND(SUM(disk_read_kb/div_by),2) disk_read,\nROUND(SUM(disk_written_kb/div_by),2) disk_written,\nROUND(MAX(disk_pct_busy),2) disk_pct_busy,\nROUND(MAX(nfs_proc_pct_busy),2) nfs_proc_pct_busy,\nROUND(SUM(net_kb_in/div_by),2) net_in,\nROUND(SUM(net_kb_out/div_by),2) net_out,\nROUND(SUM(replication_kb/div_by),2) replication\nFROM apt_v_ddm_system_log sl, aps_v_host h, var\nWHERE collection_time BETWEEN ${startDate} AND ${endDate}\nAND sl.host_id = h.host_id\nAND h.host_name = '${queryCombo1}'\nGROUP BY\nto_char(trunc(collection_time,DECODE('${freeCombo1}','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY HH24'),\nto_char(trunc(collection_time,DECODE('${freeCombo1}','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24')"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}, {"slug": "backup-manager-emc-data-domain", "name": "EMC Data Domain"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors", "backup-manager-emc-data-domain"]
category_slugs: []
---
