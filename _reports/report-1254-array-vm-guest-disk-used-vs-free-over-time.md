---
title: "Array VM Guest Disk Used vs Free Over Time"
report_id: 1254
rtd_name: "Array VM Guest Disk Used vs Free over time.rtd"
description: "Array VM Guest Disk Used vs Free Over Time"
problem_statement: "For a given array or arrays, show me how much VMware Guest disk used and free space over time, so I can project the future capacity"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 10/22/2018\nWITH \nVAR AS (\nSELECT\n'${freeCombo1}' unit,\nDECODE('${freeCombo1}', 'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by\nFROM apt_v_dual\n),\nv1 AS (\nSELECT /*+ NO_MERGE */ DISTINCT\nvf.vm_id,\nvf.storage_array_id\nFROM apt_v_vmw_vmfile vf\nWHERE\nvf.storage_array_id IN (${arrays})\n),\nt1 AS (\nSELECT /*+ NO_MERGE */\nTRUNC(log_date,DECODE('${freeCombo2}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) log_date,\ngal.vm_id,\nROUND(MAX(gal.vm_size_kb/div_by),2) max_vm_size,\nROUND(MAX(gal.total_volume_size_kb/div_by),2) max_total_volume_size,\nROUND(MAX(gal.used_volume_size_kb/div_by),2) max_used_volume_size\nFROM\napt_v_vmw_guest_allocusage_log gal, v1, var\nWHERE\ngal.vm_id = v1.vm_id \nAND gal.log_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY \nTRUNC(log_date,DECODE('${freeCombo2}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),\ngal.vm_id\nORDER BY 1,2\n)\nSELECT /*+ NO_MERGE */\nlog_date,\nCOUNT(DISTINCT vm_id) vm_count,\nSUM(max_vm_size) max_vm_size,\nSUM(max_used_volume_size) max_used_volume_size,\nSUM(max_total_volume_size) max_total_volume_size,\nSUM(max_total_volume_size)-SUM(max_used_volume_size) max_free_volume_size\nFROM t1\nGROUP BY\nlog_date\nORDER BY log_date"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
