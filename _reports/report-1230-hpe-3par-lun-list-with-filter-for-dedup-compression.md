---
title: "HPE 3PAR LUN List with Filter for DeDup & Compression"
report_id: 1230
rtd_name: "HPE 3PAR LUN List with Filter for DeDup & Compression.rtd"
description: "HPE 3PAR LUN List with Filter for DeDup & Compression"
problem_statement: "I need a list of LUNs with complete details so I can determine how to configure DeDup and Compression."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified 09/20/2018\nSELECT \nh3p_storage_system_id,\nsystem_name,\ntier1_dsp_name,\ntier2_dsp_name,\ntier3_dsp_name,\nsnap_dsp_name,\nuser_dsp_name,\nlogical_unit_id,\nlogical_unit_name,\n(NVL(tier1_user_kb,0)+NVL(tier2_user_kb,0)+NVL(tier3_user_kb,0))/1024/1024 t1t2t3_user_gb,\nis_compression_enabled,\nis_dedup_enabled,\n--\nROUND(NVL(dedup_ratio,1),1) dedup_ratio_num,\nROUND(NVL(dedup_ratio,1),1)||':1' dedup_ratio,\nCEIL(DECODE(dedup_ratio,NULL,1,0,1,dedup_ratio))||':1' dedup_ratio_norm,\n--\nROUND(NVL(compression_ratio,1),1) compression_ratio_num,\nROUND(NVL(compression_ratio,1),1)||':1' compression_ratio,\nCEIL(DECODE(compression_ratio,NULL,1,0,1,compression_ratio))||':1' compression_ratio_norm,\n--\nROUND(NVL(compaction_ratio,1),1) compaction_ratio_num,\nROUND(NVL(compaction_ratio,1),1)||':1' compaction_ratio,\nCEIL(DECODE(compaction_ratio,NULL,1,0,1,compaction_ratio))||':1' compaction_ratio_norm,\n--\ntotal_capacity_gb,\n--\nraw_admin_gb,\nraw_copy_gb,\nraw_user_gb,\nraw_blocks_gb,\n--\nconsumable_admin_gb,\nconsumable_copy_gb,\nconsumable_user_gb,\n--\nused_snapshot_admin_space_gb,\nused_snapshot_data_space_gb,\nused_user_space_gb,\n--\ntier1_admin_kb/1024/1024 tier1_admin,\ntier2_admin_kb/1024/1024 tier2_admin,\ntier3_admin_kb/1024/1024 tier3_admin,\n--\ntier1_snapshot_kb/1024/1024 tier1_snapshot,\ntier2_snapshot_kb/1024/1024 tier2_snapshot,\ntier3_snapshot_kb/1024/1024 tier3_snapshot,\n--\ntier1_user_kb/1024/1024 tier1_user,\ntier2_user_kb/1024/1024 tier2_user,\ntier3_user_kb/1024/1024 tier3_user,\n--\ndate_created,\nmaster_node,\nbackup_node1,\nbackup_node2,\nlun_policy,\npreferred_availability,\ncurrent_availability,\nexport_state,\ndisk_device_type,\n--\nsnap_space_allocation_warning,\nsnap_space_allocation_limit,\nuser_space_allocation_warning,\nuser_space_allocation_limit,\n--\nlun_domain,\nset_size,\nset_data,\nexpiration_time,\nretention_time,\nlun_operational_status||' - '||lun_other_operational_status lun_operational_status,\nvolume_type,\nlun_access,\nis_underlying_redundancy,\ndata_redundancy,\npackage_redundancy,\nname_format,\nname_space,\nis_thinly_provisioned,\ndevice_nbr,\nobject_id,\nusr_array_group_id,\nsnp_array_group_id,\nvcopy_base_logical_unit_id,\n--\ntier1_array_group_id,\ntier2_array_group_id,\ntier3_array_group_id,\n--\ntier1_new_admin_kb/1024/1024 tier1_new_admin,\ntier2_new_admin_kb/1024/1024 tier2_new_admin,\ntier3_new_admin_kb/1024/1024 tier3_new_admin,\n--\ntier1_new_snapshot_kb/1024/1024 tier1_new_snapshot,\ntier2_new_snapshot_kb/1024/1024 tier2_new_snapshot,\ntier3_new_snapshot_kb/1024/1024 tier3_new_snapshot,\n--\ntier1_new_user_kb/1024/1024 tier1_new_user,\ntier2_new_user_kb/1024/1024 tier2_new_user,\ntier3_new_user_kb/1024/1024 tier3_new_user,\n--compaction_ratio_str,\n--compression_ratio_str,\n--dedup_ratio_str,\nlast_updated\nFROM\naps_v_h3p_logical_unit\nWHERE \nh3p_storage_system_id IN (${arrays})\nAND CEIL(DECODE(dedup_ratio,NULL,1,0,1,dedup_ratio))||':1' LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\nAND CEIL(DECODE(compression_ratio,NULL,1,0,1,compression_ratio))||':1' LIKE DECODE('${queryCombo2}',' All','%','${queryCombo2}')\nAND is_dedup_enabled LIKE DECODE('${freeCombo1}','All','%','${freeCombo1}')\nAND is_compression_enabled LIKE DECODE('${freeCombo2}','All','%','${freeCombo2}')"
has_explanation: false
products: [{"slug": "capacity-manager-hpe-3par", "name": "HPE 3PAR"}]
categories: []
product_slugs: ["capacity-manager-hpe-3par"]
category_slugs: []
---
