---
title: "NBU Policy List by Type"
report_id: 953
rtd_name: "NBU Policy List by Type.rtd"
description: "NBU Policy List by Type"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/09/2012\n--This will display all NBU policy Information for the selected policy type\n--Note: This accepts Master Server ID's rather than Client ID's\nSELECT\ns.hostname master_server,\npolicy_name, \nis_active, \npolicy_type_name, \n(SELECT REPLACE(aptStringConcat(DISTINCT pf.pathname),',','<br />') paths\nFROM apt_v_nbu_policy_file pf WHERE pf.policy_id = np.policy_id GROUP BY pf.policy_id) directives,\nstorage_unit, \nmax_jobs_per_policy, \nmax_fragment_size, \njob_priority, \nkeyword, \nexists_in_catalog, \neffective_date, \nblock_incremental, \nbackup_copy, \nfile_restore_raw, \nperform_snapshot_backup, \nsnapshot_method, \nsnapshot_method_argument, \nperform_offhost_backup, \nuse_data_mover, \ndata_mover_type, \nuse_alternate_client, \nalternate_client_name, \nuse_virtual_machine, \nenable_instant_recovery, \ncollect_bmr_info, \ndata_classification, \nis_storage_life_policy, \ncheckpoint, \ncheckpoint_interval, \ngranular_restore_info, \ngeneration, \nnbu_server_group, \nlifecycle_policy_name, \nfollow_nfs_mount_points, \ncross_mount_points, \nclient_compress, \nclient_encrypt, \nmultiple_streams \nFROM apt_v_nbu_policy np, apt_v_server s\nWHERE np.server_id IN (${hosts})\nAND np.server_id = s.server_id\nAND is_active = DECODE('${freeCombo1}','All',is_active,'Active','Y','Inactive','N')\nAND policy_type_name = DECODE('${freeCombo2}','All',policy_type_name,'${freeCombo2}')"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
