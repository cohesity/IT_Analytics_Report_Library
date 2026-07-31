---
title: "NBU Appliance Disk Pool Summary"
report_id: 1145
rtd_name: "NBU Appliance Disk Pool Summary.rtd"
description: "Summary the disk pools on appliances like Puredisk, Advanced Disk, DataDomain"
problem_statement: "I need a report that shows me an overview of all my NBU disk pools and what their capacity is."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 03/25/2020\nWITH\nvar AS (\nSELECT\nDECODE('${freeCombo1}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\nt1 AS (\nSELECT \n  dp.management_server_id,\n  h.display_name master_server,\n  dp.disk_type,\n  COUNT(dp.disk_volume_name) disk_volume_count,\n  aptStringConcat(DISTINCT dp.disk_volume_name) disk_volumes,\n  COUNT(DISTINCT dp.disk_pool_id) disk_pool_count,\n  aptStringConcat(DISTINCT dp.disk_pool_name) disk_pools,\n  COUNT(DISTINCT e.host_id) media_server_count, \n  aptStringConcat(DISTINCT e.display_name) media_servers,\n  COUNT(DISTINCT dp.storage_unit_id) storage_unit_count, \n  aptStringConcat(DISTINCT dp.storage_unit_label) storage_units,\n  MAX(dp.total_capacity_kb/div_by) total_capacity,\n  MAX(dp.free_space_kb/div_by) free_space\nFROM \n  apt_v_nbu_disk_pool dp, aps_v_host h, aps_v_host e, apt_v_nbu_strgunit_mediasrvr sm, var\nWHERE\n  dp.management_server_id = h.host_id\n  AND h.host_id IN (${hosts})\n  AND sm.storage_unit_id = dp.storage_unit_id\n  AND sm.media_server_id = e.host_id\n  AND dp.total_capacity_kb > 0\nGROUP BY\n  dp.management_server_id,\n  h.display_name,\n  dp.disk_type\n)\nSELECT\n  management_server_id,\n  master_server,\n  disk_type,\n  disk_volume_count,\n  REPLACE(disk_volumes,',','<br>') disk_volumes,\n  disk_pool_count,\n  REPLACE(disk_pools,',','<br>') disk_pools,\n  media_server_count,\n  REPLACE(media_servers,',','<br>') media_servers,\n  storage_unit_count,\n  REPLACE(storage_units,',','<br>') storage_units,\n  total_capacity,\n  free_space,\n  (total_capacity - free_space) used,\n  (total_capacity - free_space)/total_capacity*100 pct_used,\n  (total_capacity - free_space)/total_capacity used_pct\nFROM \n  t1\nORDER BY \n  15 DESC"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
