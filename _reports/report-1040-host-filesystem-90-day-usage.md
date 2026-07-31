---
title: "Host Filesystem 90 Day Usage"
report_id: 1040
rtd_name: "Host Filesystem 90 Day Usage.rtd"
description: "Host Filesystem 90 Day Usage"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 03/01/2012\n--Used to determine which filesystems are fluctuating the most over their  \n--90 day average usage.\nSELECT DISTINCT \nf.host_id,\nf.host_name, \nf.mount_point, \nf.file_system_name,\nf.storage_type, \nf.volume_group_name,\nf.filesystem_capacity_kb/1024/1024 filesystem_capacity_gb,\nf.filesystem_used_kb/1024/1024 filesystem_used_gb,\n(f.filesystem_capacity_kb-f.filesystem_used_kb)/1024/1024 filesystem_available_gb,\nround((f.filesystem_used_kb-fs.used_90day_avg)/f.filesystem_used_kb*100,2) used_90day_delta_avg,\nround((f.filesystem_used_kb-fs.used_90day_max)/f.filesystem_used_kb*100,2) used_90day_delta_max,\nfs.capacity_90day_avg/1024/1024 capacity_90day_avg,\nfs.capacity_90day_max/1024/1024 capacity_90day_max,\nfs.capacity_90day_min/1024/1024 capacity_90day_min,\nfs.used_90day_avg/1024/1024 used_90day_avg,\nfs.used_90day_max/1024/1024 used_90day_max,\nfs.used_90day_min/1024/1024 used_90day_min\nFROM aps_v_file_system_path f, aps_v_file_system_stat fs\nWHERE f.host_id IN (${hosts})\nAND f.filesystem_id=fs.filesystem_id\nAND f.storage_type LIKE DECODE('${freeCombo1}','SAN','S','DAS','D','All','%')\nORDER BY f.host_name, f.file_system_name"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
