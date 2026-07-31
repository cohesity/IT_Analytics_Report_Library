---
title: "Array Full Disclosure"
report_id: 1250
rtd_name: "Array Full Disclosure.rtd"
description: "Array Full Disclosure"
problem_statement: "I just a heterogeneous list of all if the information about all of my arrays"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 10/23/2018\nWITH \nVAR AS (\nSELECT\n'${freeCombo1}' unit,\nDECODE('${freeCombo1}', 'GB',1024*1024,'TB',1024*1024*1024,'PB',(1024*1024*1024*1024)) div_by\nFROM apt_v_dual\n)\nSELECT\nstorage_array_id,\nvendor_name,\narray_name,\narray_family,\narray_type,\ndomain_id,\ndomain_name,\nroot_group_id,\nobject_id,\nproduct_name,\nserial_nbr,\ndevice_manager_id,\nip_address,\nagent_version,\ncontroller_version,\ncache_kb/div_by cache,\nis_active,\nis_rm_enabled,\ncreation_date,\nlast_updated,\nnbr_allocated_luns,\nnbr_of_luns,\nnbr_array_ports,\nnbr_hosts,\nnbr_of_fc_ports,\nnbr_of_iscsi_ports,\nnbr_of_ethernet_ports,\nnbr_of_physical_disks,\nnbr_of_array_groups,\nnbr_of_storage_pools,\nnbr_of_thin_pools,\nthin_pool_subscribed_pct,\nraw_capacity_kb/div_by raw_capacity,\nraw_allocated_kb/div_by raw_allocated,\nraw_available_kb/div_by raw_available,\ncapacity_kb/div_by capacity,\nallocated_kb/div_by allocated,\nother_allocated_kb/div_by other_allocated,\navailable_kb/div_by available,\nlargest_free_space_kb/div_by largest_free_space,\narray_group_capacity_kb/div_by array_group_capacity,\narray_group_allocated_kb/div_by array_group_allocated,\narray_group_available_kb/div_by array_group_available,\npool_capacity_kb/div_by pool_capacity,\npool_allocated_kb/div_by pool_allocated,\npool_available_kb/div_by pool_available,\nthin_pool_capacity_kb/div_by thin_pool_capacity,\nthin_pool_allocated_kb/div_by thin_pool_allocated,\nthin_pool_available_kb/div_by thin_pool_available,\nthin_pool_subscribed_kb/div_by thin_pool_subscribed,\nusable_internal_capacity_kb/div_by usable_internal_capacity,\nusable_external_capacity_kb/div_by usable_external_capacity,\nusable_used_capacity_kb/div_by usable_used_capacity,\nusable_free_capacity_kb/div_by usable_free_capacity,\nvirtualized_capacity_kb/div_by virtualized_capacity,\nvirtualized_capacity_thin_kb/div_by virtualized_capacity_thin,\nreplication_capacity_kb/div_by replication_capacity,\nestimated_used_kb/div_by estimated_used,\nlun_allocated_kb/div_by lun_allocated,\nlun_capacity_kb/div_by lun_capacity \nFROM aps_v_storage_array sa, var\nWHERE storage_array_id IN (${arrays})"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
