---
title: "VM Datastore Thin Provisioning Report"
report_id: 1101
rtd_name: "VM Datastore Thin Provisioning Report.rtd"
description: "An overview of thin provisioned VMWare datastores with emphasis on over subscribed.\r\nThis report it can easily be setup as an alert or used as part of an overall storage dashboard."
problem_statement: "Which datastores are at risk?\r\nAm I over subscribed?"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 06/26/2015\nWITH\nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays,\n${startDate} startDate,\nDECODE('${freeCombo1}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by\nFROM apt_v_dual\n)\nSELECT \nDISTINCT\ndu.vmw_datastore_id, \ndu.datastore_name, \ndu.total_ds_capacity_kb/div_by total_ds_capacity, \ndu.ds_used_kb/div_by ds_used, \ndu.ds_free_kb/div_by ds_free,\ndu.ds_used_kb / total_ds_capacity_kb used_pct, \ndu.ds_used_kb / total_ds_capacity_kb pct_used, \ndu.total_vmdisk_size_kb/div_by consumed , \nCASE WHEN (du.total_ds_capacity_kb-du.total_vmdisk_size_kb)< 0\nTHEN\n(du.total_ds_capacity_kb-du.total_vmdisk_size_kb)/div_by\nELSE null\nEND over_consumed,\ndu.total_prov_vmdisk_size_kb/div_by provisioned, \n(du.total_prov_vmdisk_size_kb - total_ds_capacity_kb)/div_by overprov,\n(du.total_prov_vmdisk_size_kb / total_ds_capacity_kb) overprov_pct,\n(du.total_prov_vmdisk_size_kb / total_ds_capacity_kb) pct_overprov\nFROM apt_v_vmw_datastore_usage du, apt_v_vmw_extent de, apt_v_virtual_system vs, var\nWHERE du.vmw_datastore_id = de.vmw_datastore_id\nAND de.virtual_system_id = vs.virtual_system_id \nAND vs.host_id IN (${hosts})\nAND du.total_prov_vmdisk_size_kb > 0\nORDER BY over_consumed ASC"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
