---
title: "VM Guest NetApp SnapVault Lag Time Status"
report_id: 1017
rtd_name: "VM Guest NetApp SnapVault Lag Time Status.rtd"
description: "VM Guest NetApp SnapVault Lag Time Status"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 09/20/2011\n--Maps the VM Guests to their Datastores then displays the source and destination\n--of the filers SnapVaults.  The threshold for the lag time can be set at runtime \n--to trigger the color change of the status dot. \nWITH \nds AS (\nSELECT vm.partition_id, \n  vm.host_name,\n  ds.vmw_datastore_id, ds.datastore_name\nFROM \n  apt_v_vmw_virtual_machine vm, apt_v_vmw_datastore ds, apt_v_partition p\nWHERE vm.partition_id = p.partition_id\n  AND p.host_id IN (${hosts})\n  AND vm.vmw_datastore_id = ds.vmw_datastore_id\n  AND vm.guest_state = 'running'\n  AND vm.host_name IS NOT NULL\n)\nSELECT \n  ds.partition_id, \n  ds.host_name,\n  ss.nap_snapvault_status_id,\n  ss.mirror_timestamp, \n  DECODE(ss.summary_status,0,'blue',1,'yellow',2,'red') summary_status,\n  rtd.secsToHoursMinSecs(ss.lag_time) lag_time,\n  CASE \n    WHEN ss.lag_time/60/60 < ${freeCombo1} THEN 'green'\n    WHEN ss.lag_time/60/60 > ${freeCombo1} AND ss.lag_time/60/60 < ${freeCombo2} THEN 'yellow' \n    WHEN ss.lag_time/60/60 > ${freeCombo2} THEN 'red'\n  END lag_time_status,\n  ds.vmw_datastore_id, \n  ds.datastore_name,\n  sc.source_storage_system_id,\n  sc.source_system_name,\n  sc.source_volume_id,\n  sc.source_volume_name,\n  sc.source_qtree_id, \n  sc.source_qtree_name, \n  sc.destination_storage_system_id,\n  sc.destination_system_name,\n  sc.destination_volume_id, \n  sc.destination_volume_name \nFROM ds, aps_v_nap_snapvault_status ss, aps_v_nap_snapvault_config sc, \n  aps_v_storage_array src, aps_v_storage_array dest  \nWHERE ss.nap_snapvault_config_id       = sc.nap_snapvault_config_id\n  AND sc.source_storage_system_id      = src.storage_array_id \n  AND sc.destination_storage_system_id = dest.storage_array_id\n  AND ss.mirror_timestamp BETWEEN ${startDate} AND ${endDate}\n  AND ss.summary_status IS NOT NULL\n  AND sc.source_system_name LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\n  AND instr(sc.source_volume_name,ds.datastore_name,1,1) > 0"
has_explanation: false
products: [{"slug": "capacity-manager-netapp-reports-7-mode", "name": "NetApp Reports (7 Mode)"}]
categories: []
product_slugs: ["capacity-manager-netapp-reports-7-mode"]
category_slugs: []
---
