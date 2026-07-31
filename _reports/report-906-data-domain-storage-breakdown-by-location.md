---
title: "Data Domain Storage Breakdown by Location"
report_id: 906
rtd_name: "Data Domain Storage Breakdown by Location.rtd"
description: "Data Domain Storage Breakdown by Location"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 12/14/2011\n--FS Size,Pre Comp,FS Used, Avg Compression,Cleanable,Est Available\nWITH \nt1 AS (\nSELECT\ns.server_id,\ns.hostname,\ns.location,\ns.ip_address,\nde.model_number,\nds.serial_number,\ns.os_version,\nsum(dfs.filesystem_size_kb/1024/1024/1024) filesystem_size_tb,\nsum(dfs.pre_comp_size_kb/1024/1024/1024) pre_comp_size_tb,\nsum(dfs.filesystem_used_kb/1024/1024/1024) filesystem_used_tb,\nsum(dfs.filesystem_cleanable_kb/1024/1024/1024) filesystem_cleanable_tb\nFROM apt_v_server s, apt_v_ddm_system ds, apt_v_ddm_enclosure de, apt_v_ddm_file_system dfs\nWHERE ds.host_id = s.server_id\nAND ds.host_id = de.host_id\nAND ds.host_id = dfs.host_id\nAND de.enclosure_id = 1\nGROUP BY\ns.server_id,\ns.hostname,\ns.location,\ns.ip_address,\nde.model_number,\nds.serial_number,\ns.os_version\n),\nt2 AS(\nSELECT\nlocation,\nround(sum(filesystem_size_tb),2) filesystem_size_tb,\nround(sum(pre_comp_size_tb),2) pre_comp_size_tb,\nround(sum(filesystem_used_tb),2) filesystem_used_tb,\nround(avg((pre_comp_size_tb/filesystem_used_tb)),2) avg_comp_ratio,\nround(sum(filesystem_cleanable_tb),2) filesystem_cleanable_tb,\nround(sum((filesystem_size_tb-filesystem_used_tb)*(pre_comp_size_tb/filesystem_used_tb)),2) est_available\nFROM t1\nGROUP BY location\n)\nSELECT\nlocation,\nDECODE('${freeCombo1}',\n'FS Size',filesystem_size_tb,\n'Pre Comp',pre_comp_size_tb,\n'FS Used',filesystem_used_tb, \n'Avg Compression',avg_comp_ratio,\n'Cleanable',filesystem_cleanable_tb,\n'Est Available',est_available\n) metric\nFROM t2\nORDER BY 2"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}, {"slug": "backup-manager-emc-data-domain", "name": "EMC Data Domain"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors", "backup-manager-emc-data-domain"]
category_slugs: []
---
