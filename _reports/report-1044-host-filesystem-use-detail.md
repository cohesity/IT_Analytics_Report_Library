---
title: "Host Filesystem Use Detail"
report_id: 1044
rtd_name: "Host Filesystem Use Detail.rtd"
description: "Host Filesystem Use Detail"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 03/05/2011\nWITH \nt1 AS (\nSELECT\nhost_id,host_name,\n'DAS' storage_type,\nfilesystem_capacity_kb/1024/1024 capacity_gb,\nfilesystem_used_kb/1024/1024 used_gb\nFROM aps_v_file_system_path\nWHERE mount_point IS NOT NULL\nAND host_id IN (${hosts})\nAND storage_type = 'D'\nUNION ALL\nSELECT\nhost_id,host_name,\n'SAN' storage_type,\nfilesystem_capacity_kb/1024/1024 capacity_gb,\nfilesystem_used_kb/1024/1024 used_gb\nFROM aps_v_file_system_path\nWHERE mount_point IS NOT NULL\nAND host_id IN (${hosts})\nAND storage_type = 'S'\nUNION ALL\nSELECT DISTINCT\nfs.host_id,fs.host_name,\n'NAS' storage_type,\nfs.capacity_kb/1024/1024 capacity_gb,\nfs.used_kb/1024/1024 used_gb\nFROM aps_v_file_system fs\nWHERE \nfs.mount_point IS NOT NULL\nAND fs.host_id in (${hosts})\nAND fs.file_system_type LIKE 'nfs%'\n),\nt2 AS (\nSELECT\nhost_id,host_name,\nSUM(DECODE(storage_type,'DAS',capacity_gb,0)) das_capacity,\nSUM(DECODE(storage_type,'DAS',used_gb,0)) das_used,\nSUM(DECODE(storage_type,'SAN',capacity_gb,0)) san_capacity,\nSUM(DECODE(storage_type,'SAN',used_gb,0)) san_used,\nSUM(DECODE(storage_type,'NAS',capacity_gb,0)) nas_capacity,\nSUM(DECODE(storage_type,'NAS',used_gb,0)) nas_used\nFROM t1\nGROUP BY host_id,host_name\n)\nSELECT \nhost_id,host_name,\ndas_capacity,\ndas_used,\n(das_capacity - das_used) das_free,\nDECODE(das_used,0,null,das_used)/das_capacity*100 das_used_pct,\nDECODE(das_used,0,null,das_used)/das_capacity das_pct,\nsan_capacity,\nsan_used,\n(san_capacity - san_used) san_free,\nDECODE(san_used,0,null,san_used)/san_capacity*100 san_used_pct,\nDECODE(san_used,0,null,san_used)/san_capacity san_pct,\nnas_capacity,\nnas_used,\n(nas_capacity - nas_used) nas_free,\nDECODE(nas_used,0,null,nas_used)/nas_capacity*100 nas_used_pct,\nDECODE(nas_used,0,null,nas_used)/nas_capacity nas_pct\nFROM t2"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
