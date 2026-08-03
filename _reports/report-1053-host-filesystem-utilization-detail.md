---
title: "Host Filesystem Utilization Detail"
report_id: 1053
rtd_name: "Host Filesystem Utilization Detail.rtd"
description: "Host Filesystem Utilization Detail"
problem_statement: ""
author: "rich.rose@aptare.com\r\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 02/14/2012\nWITH \nt1 AS (\nSELECT DISTINCT\nfsp.host_id,\nfsp.host_name,\nDECODE(fsp.is_san_disk,'Y','SAN','N','DAS') disk_type,\nfsp.file_system_type,\nfsp.mount_point,\nfsp.filesystem_capacity_kb/1024/1024 filesystem_capacity_gb,\nfsp.filesystem_used_kb/1024/1024 filesystem_used_gb,\ntrunc(DECODE(fsp.filesystem_used_kb,0,null,fsp.filesystem_used_kb)/fsp.filesystem_capacity_kb*100) used_pct\nFROM aps_v_file_system_path fsp\nWHERE \nfsp.mount_point IS NOT NULL\nAND fsp.host_id in (${hosts})\nUNION ALL\nSELECT DISTINCT\nfs.host_id,\nfs.host_name,\n'NAS' disk_type,\nfs.file_system_type,\nfs.mount_point,\nfs.capacity_kb/1024/1024 filesystem_capacity_gb,\nfs.used_kb/1024/1024 filesystem_used_gb,\ntrunc(DECODE(fs.used_kb,0,null,fs.used_kb)/fs.capacity_kb*100) used_pct\nFROM aps_v_file_system fs\nWHERE \nfs.mount_point IS NOT NULL\nAND fs.host_id in (${hosts})\nAND fs.file_system_type LIKE 'nfs%'\n)\nSELECT host_id,\nhost_name,\ndisk_type,\nfile_system_type,\nmount_point,\nfilesystem_capacity_gb,\nfilesystem_used_gb,\nfilesystem_capacity_gb-filesystem_used_gb filesystem_free_gb,\nused_pct/100 pct_used,\nused_pct\nFROM t1\nWHERE used_pct >= ${freeCombo1}\nAND disk_type LIKE DECODE('${freeCombo2}','SAN','SAN','DAS','DAS','NAS','NAS','All','%')\nORDER BY host_name, mount_point"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
