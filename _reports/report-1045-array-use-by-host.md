---
title: "Array Use by Host"
report_id: 1045
rtd_name: "Array Use by Host.rtd"
description: "Array Use by Host"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2011\nWITH t1 as (\nSELECT sa.storage_array_id, sa.array_name, sa.serial_nbr, sa.cache_kb,\nlu.array_group_id,\nhl.host_id,\nhl.host_name,\nag.raid_type,\navg(ag.allocated_capacity_gb / DECODE(ag.total_capacity_gb,0,null,ag.total_capacity_gb)) raid_loss_factor,\nsum(hl.lun_capacity_gb) sum_lun_size_gb,\ncount(DISTINCT hl.logical_unit_id) lun_count\nFROM  aps_v_storage_array sa, aps_v_host_luns hl, aps_v_logical_unit lu,aps_v_array_group ag\nWHERE sa.storage_array_id = hl.storage_array_id\nAND hl.host_id in (${hosts})\nAND hl.logical_unit_id = lu.logical_unit_id\nAND lu.array_group_id IS NOT NULL\nAND lu.array_group_id = ag.array_group_id\nAND sa.vendor_name LIKE DECODE('${freeCombo1}','All','%','%${freeCombo1}%')\nGROUP BY sa.storage_array_id, sa.array_name, sa.serial_nbr, sa.cache_kb, lu.array_group_id,hl.host_id, hl.host_name,ag.raid_type\nORDER BY sa.storage_array_id, sa.array_name ,sa.serial_nbr, sa.cache_kb, lu.array_group_id,hl.host_id, hl.host_name,ag.raid_type\n)\nSELECT\nhost_id,\nhost_name,\narray_name, serial_nbr, cache_kb/1024/1024 as cache_GB,\n(SELECT avg(capacity_kb)/1024/1024 FROM aps_v_pdev pd WHERE pd.storage_array_id = t1.storage_array_id) drive_size, \n(SELECT count(pdev_id) FROM aps_v_pdev pd WHERE pd.storage_array_id = t1.storage_array_id) drive_count, \nraid_type,\nsum_lun_size_gb*raid_loss_factor + sum_lun_size_gb assigned_size, \nsum_lun_size_gb true_usable_size, \n(SELECT sum(fsp.filesystem_used_kb)/1024/1024 FROM aps_v_file_system_path fsp WHERE fsp.host_id = t1.host_id AND is_san_disk='Y') used_size_gb,\n(SELECT sum(fsp.filesystem_capacity_kb-fsp.filesystem_used_kb)/1024/1024 FROM aps_v_file_system_path fsp WHERE fsp.host_id = t1.host_id AND is_san_disk='Y') avail_size_gb,\n(SELECT sum(fsp.filesystem_used_kb/DECODE(fsp.filesystem_capacity_kb,0,null,fsp.filesystem_capacity_kb)) FROM aps_v_file_system_path fsp WHERE fsp.host_id = t1.host_id AND is_san_disk='Y') utilization_pct\nFROM t1"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
