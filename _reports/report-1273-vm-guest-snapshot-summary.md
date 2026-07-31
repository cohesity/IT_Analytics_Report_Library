---
title: "VM Guest Snapshot Summary"
report_id: 1273
rtd_name: "VM Guest Snapshot Summary.rtd"
description: "VM Guest Snapshot Summary"
problem_statement: "I need to see Snapshots of VM's and how old they are"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@veritas.com\n--Last Updated: 05/11/2020\nWITH \nVAR AS (\nSELECT\n  ROUND((${endDate} - ${startDate}),2) nbrOfDays,\n  ${startDate} startDate,\n  DECODE('${freeCombo1}',\n  'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by,\n  '${freeCombo1}' the_unit \nFROM \n  apt_v_dual\n),\nt1 AS (\nSELECT \n  vs.virtual_system_id AS vm_host_id,\n  vs.virtual_system_name AS vm_host_name,\n  pt.partition_id AS vm_id,\n  pt.partition_name AS vm_name,\n  h.host_id,\n  h.display_name AS host_name,\n  ds.vmw_datastore_id,\n  ds.datastore_name,\n  df.file_name,\n  st.full_snapshot_name||' ('||st.short_snapshot_name||')' AS snapshot_name,\n  df.size_kb/div_by AS df_size,\n  st.create_date,\n  (sysdate - create_date) AS age\nFROM \n  var,\n  apt_v_vmw_vmsnapshot_tree st,\n  apt_v_vmw_map_snapshot_file mp,\n  apt_v_vmw_datastore_file df,\n  apt_v_vmw_datastore ds,\n  apt_v_virtual_system vs,\n  apt_v_partition pt,\n  aps_v_host h\nWHERE \n  pt.host_id IN (${hosts})\n  AND pt.host_id = h.host_id\n  AND pt.partition_id= st.partition_id\n  AND st.vmw_snapshot_id= mp.vmw_snapshot_id\n  AND mp.vmw_datastore_file_id= df.vmw_datastore_file_id\n  AND df.vmw_datastore_id = ds.vmw_datastore_id\n  AND st.virtual_system_id = vs.virtual_system_id\n  AND vs.collection_status != 3\n  AND st.create_date BETWEEN ${startDate} AND ${endDate}\nORDER BY \n  df.file_name, st.create_date\n)\nSELECT \n  vm_host_id,\n  vm_host_name,\n  vm_id,\n  vm_name,\n  host_id,\n  host_name,\n  vmw_datastore_id,\n  datastore_name,\n  REPLACE(aptStringConcat(file_name),',','<br>') files,\n  snapshot_name,\n  SUM(df_size) AS df_size,\n  create_date,\n  age\nFROM \n  t1\nGROUP BY\n  vm_host_id,\n  vm_host_name,\n  vm_id,\n  vm_name,\n  host_id,\n  host_name,\n  vmw_datastore_id,\n  datastore_name,\n  snapshot_name,\n  create_date,\n  age\nORDER BY \n  UPPER(vm_name)"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
