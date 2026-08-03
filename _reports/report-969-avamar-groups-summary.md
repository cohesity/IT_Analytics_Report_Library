---
title: "Avamar Groups Summary"
report_id: 969
rtd_name: "Avamar Groups Summary.rtd"
description: "Avamar Groups Summary"
problem_statement: "I need to see a summary of how my Groups are configured in Avamar"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 01/07/2019\nWITH \ngc AS (\nSELECT \nac.master_server_id, \nagm.avm_group_id, \nCOUNT(agm.avm_group_id) client_count \nFROM \napt_v_avm_group_members agm, apt_v_avm_clients ac\nWHERE \nagm.client_id = ac.client_id \nAND ac.client_id IN (${hosts})\nGROUP BY \nac.master_server_id, \nagm.avm_group_id\n) \nSELECT\ngc.master_server_id,\navg.gsan_system_id, \navg.gsan_system_name, \navg.group_name, \ngc.client_count,\navg.avm_group_id, \navg.avm_domain_id, \navg.dataset_id, \navd.dataset_name,\navg.retention_policy_id, \navrp.retention_policy_name, \navg.schedule_id, \navs.schedule_name,\navg.created_date, \navg.modified_date, \navg.priority,\navg.is_enabled, \navg.is_failed_stop,  \navg.is_read_only, \navg.is_run_once, \navg.is_skip_next, \navg.retry_count,\navg.target_dpn, \navg.timeout_min\nFROM apt_v_avm_groups avg, apt_v_avm_datasets avd, apt_v_avm_schedules avs, apt_v_avm_retention_policies avrp, gc\nWHERE avg.dataset_id = avd.dataset_id\nAND avg.schedule_id = avs.schedule_id\nAND avg.retention_policy_id = avrp.retention_policy_id\nAND avg.avm_group_id = gc.avm_group_id (+)"
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
