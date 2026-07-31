---
title: "HPE 3PAR LUNs with/without Compression Cost Modeling Detail"
report_id: 1241
rtd_name: "HPE 3Par LUNs with_without Compression Cost Modeling Detail.rtd"
description: "HPE 3PAR LUNs with/without Compression Cost Modeling Detail"
problem_statement: "I need the ability to model my cost savings for LUNs that have Compression enabled and optionally disable LUNs that have Compression enabled but are not getting any benefit. I also need to model the performance impact of the overhead involved in Compression, especially of LUNs that are not compressing well."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified 09/20/2018\nWITH \np1 AS (\nSELECT \n logical_unit_id,\n MAX(total_io) max_total_io_sample,\n MAX(read_io_response_time) max_read_io_response_sample,\n MAX(write_io_response_time) max_write_io_response_sample\n FROM aps_v_lun_perform_log \n WHERE \n log_date >= sysdate-2 \n AND storage_array_id IN (${arrays})\nGROUP BY\n logical_unit_id \nORDER BY \n 2 DESC\n),\nt1 AS (\nSELECT \nh3p_storage_system_id,\nsystem_name,\nuser_dsp_name,\nlogical_unit_id,\nlogical_unit_name,\n(NVL(tier1_user_kb,0)+NVL(tier2_user_kb,0)+NVL(tier3_user_kb,0))/1024/1024 t1t2t3_user_gb,\nCEIL(DECODE(dedup_ratio,NULL,1,0,1,dedup_ratio))||':1' dedup_ratio,\nCEIL(DECODE(dedup_ratio,NULL,1,0,1,dedup_ratio)) dedup_ratio_num,\nCEIL(DECODE(compression_ratio,NULL,1,0,1,compression_ratio))||':1' compression_ratio,\nCEIL(DECODE(compression_ratio,NULL,1,0,1,compression_ratio)) compression_ratio_num,\nCEIL(DECODE(compaction_ratio,NULL,1,0,1,compaction_ratio))||':1' compaction_ratio,\nCEIL(DECODE(compaction_ratio,NULL,1,0,1,compaction_ratio)) compaction_ratio_num,\ntotal_capacity_gb,\nconsumable_admin_gb,\nconsumable_copy_gb,\nconsumable_user_gb,\nused_snapshot_admin_space_gb,\nused_snapshot_data_space_gb,\nused_user_space_gb,\nis_compression_enabled,\nis_dedup_enabled\nFROM\naps_v_h3p_logical_unit\nWHERE \nh3p_storage_system_id IN (${arrays})\nAND NVL(is_compression_enabled,'No') LIKE DECODE('${freeCombo1}','All','%','${freeCombo1}')\nAND CEIL(DECODE(compression_ratio,NULL,1,0,1,compression_ratio))||':1' LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\n)\nSELECT\nt1.h3p_storage_system_id storage_array_id,\nt1.system_name,\nt1.user_dsp_name,\nt1.logical_unit_id,\nt1.logical_unit_name,\nt1.is_compression_enabled,\nt1.compression_ratio,\nNVL(p1.max_total_io_sample,0) max_total_io_sample,\nNVL(p1.max_read_io_response_sample,0) max_read_io_response_sample,\nNVL(p1.max_write_io_response_sample,0) max_write_io_response_sample,\nt1.used_user_space_gb,\nused_user_space_gb * compression_ratio_num AS actual_size_needed_gb,\n(t1.used_user_space_gb * t1.compression_ratio_num) - t1.used_user_space_gb AS actual_savings_gb,\n((t1.used_user_space_gb * t1.compression_ratio_num) - t1.used_user_space_gb) * ${freeText1} AS actual_savings_money\nFROM t1, p1\nWHERE \nt1.logical_unit_id = p1.logical_unit_id (+)\nAND h3p_storage_system_id IN (${arrays})\nAND NVL(p1.max_read_io_response_sample,0) >= ${freeText2}\nAND NVL(p1.max_write_io_response_sample,0) >= ${freeText3}"
has_explanation: false
products: [{"slug": "capacity-manager-hpe-3par", "name": "HPE 3PAR"}]
categories: []
product_slugs: ["capacity-manager-hpe-3par"]
category_slugs: []
---
