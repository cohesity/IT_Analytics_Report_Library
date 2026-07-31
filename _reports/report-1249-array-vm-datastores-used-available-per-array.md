---
title: "Array VM Datastores Used & Available per Array"
report_id: 1249
rtd_name: "Array VMware Datastores Used and Available per Array.rtd"
description: "Array VM Datastores Used & Available per Array"
problem_statement: "For a given array or arrays, show me how much VMware Datastore used and free space so I can plan for future capacity"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 10/10/2018\nWITH\nVAR AS (\nSELECT \nDECODE('${freeCombo1}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT \ndl.array_name,\nCOUNT(DISTINCT dl.vmw_datastore_id) nbr_of_datastores,\nROUND(SUM(ds.tot_capacity_kb/div_by),2) tot_capacity,\nROUND(SUM((ds.tot_capacity_kb-ds.free_capacity_kb)/div_by),2) used_capacity,\nROUND(SUM(ds.free_capacity_kb/div_by),2) free_capacity\nFROM \nvar, apt_v_vmw_map_datastore_lun dl, apt_v_vmw_datastore ds\nWHERE \ndl.storage_array_id IN (${arrays})\nAND dl.vmw_datastore_id = ds.vmw_datastore_id\nGROUP BY \ndl.storage_array_id,\ndl.array_name\nORDER BY 3 DESC"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}, {"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors", "virtualization-vmware"]
category_slugs: []
---
