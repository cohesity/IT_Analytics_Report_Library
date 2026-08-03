---
title: "Host Filesystem Reclaimation Candidates"
report_id: 1048
rtd_name: "Host Filesystem Reclaimation Candidates.rtd"
description: "Host Filesystem Reclaimation Candidates"
problem_statement: "I'm thinking about taking advantage of over subscribing on my pools but I need to know which hosts would be the best candidates for this.  I'm looking for hosts that have available capacity and are not fluctuating much over the past 3 months."
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 03/01/2012\n--Used to determine which filesystems are not fluctuating much and have available capacity\nSELECT DISTINCT \nf.host_id,\nf.host_name, \nf.mount_point, \nf.file_system_name,\nf.storage_type, \nf.volume_group_name,\nf.filesystem_capacity_kb/1024/1024 filesystem_capacity_gb,\nf.filesystem_used_kb/1024/1024 filesystem_used_gb,\n(f.filesystem_capacity_kb-f.filesystem_used_kb)/1024/1024 filesystem_available_gb,\n(f.filesystem_capacity_kb-f.filesystem_used_kb)/f.filesystem_capacity_kb*100 available_pct,\nround(nvl(((f.filesystem_capacity_kb-f.filesystem_used_kb)-(fs.capacity_90day_min-fs.used_90day_min))/(f.filesystem_capacity_kb-f.filesystem_used_kb)*100,0),2) avail_90day_delta_min,\nround(nvl(((f.filesystem_capacity_kb-f.filesystem_used_kb)-(fs.capacity_90day_max-fs.used_90day_max))/(f.filesystem_capacity_kb-f.filesystem_used_kb)*100,0),2) avail_90day_delta_max,\nround(nvl(((f.filesystem_capacity_kb-f.filesystem_used_kb)-(fs.capacity_90day_avg-fs.used_90day_avg))/(f.filesystem_capacity_kb-f.filesystem_used_kb)*100,0),2) avail_90day_delta_avg,\nnvl((fs.capacity_90day_min-fs.used_90day_min)/1024/1024,0) avail_90day_min,\nnvl((fs.capacity_90day_max-fs.used_90day_max)/1024/1024,0) avail_90day_max,\nnvl((fs.capacity_90day_avg-fs.used_90day_avg)/1024/1024,0) avail_90day_avg\nFROM aps_v_file_system_path f, aps_v_file_system_stat fs\nWHERE f.host_id IN (${hosts})\nAND f.filesystem_id=fs.filesystem_id(+)\nAND f.storage_type LIKE DECODE('${freeCombo1}','SAN','S','DAS','D','All','%')\nAND f.filesystem_capacity_kb > 0\nAND (f.filesystem_capacity_kb-f.filesystem_used_kb)/f.filesystem_capacity_kb*100 >= (${freeCombo2})\nAND nvl((f.filesystem_used_kb-fs.used_90day_avg)/f.filesystem_used_kb*100,0) <= (${freeCombo3})\nAND (f.filesystem_capacity_kb-f.filesystem_used_kb)/1024/1024 >= (${freeText1})\nORDER BY f.host_name, f.file_system_name"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
