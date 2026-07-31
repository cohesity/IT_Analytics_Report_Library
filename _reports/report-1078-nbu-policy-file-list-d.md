---
title: "NBU Policy File List.D"
report_id: 1078
rtd_name: "NBU Policy File List.D.rtd"
description: "NBU Policy File List"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/09/2012\n--Drilldown: systemName = NBUPolicyList.D This will not run standalone!\n--This will display all NBU policy Information for the_master_server and the_policy_type\nSELECT\ns.hostname master_server,\npolicy_id,policy_name, \nis_active, \npolicy_type_name, \n(SELECT REPLACE(aptStringConcat(DISTINCT pf.pathname),',','<br />') paths\nFROM apt_v_nbu_policy_file pf WHERE pf.policy_id = np.policy_id GROUP BY pf.policy_id) directives,\nstorage_unit, \nmax_jobs_per_policy, \nmax_fragment_size, \njob_priority, \nkeyword, \nexists_in_catalog, \neffective_date, \nblock_incremental, \nbackup_copy, \nfile_restore_raw, \nperform_snapshot_backup, \nsnapshot_method, \nsnapshot_method_argument, \nperform_offhost_backup, \nuse_data_mover, \ndata_mover_type, \nuse_alternate_client, \nalternate_client_name, \nuse_virtual_machine, \nenable_instant_recovery, \ncollect_bmr_info, \ndata_classification, \nis_storage_life_policy, \ncheckpoint, \ncheckpoint_interval, \ngranular_restore_info, \ngeneration, \nnbu_server_group, \nlifecycle_policy_name, \nfollow_nfs_mount_points, \ncross_mount_points, \nclient_compress, \nclient_encrypt, \nmultiple_streams\nFROM apt_v_nbu_policy np, apt_v_server s\nWHERE policy_type = '${the_policy_type}'\nAND np.server_id = ${the_server_id}\nAND np.is_active = DECODE('${the_state}','All',np.is_active,'Active','Y','Inactive','N')\nAND np.server_id = s.server_id\nORDER BY 2"
has_explanation: false
products: []
categories: []
product_slugs: []
category_slugs: []
---
