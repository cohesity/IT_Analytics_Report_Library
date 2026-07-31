---
title: "Array VM Guest Size & Counts per Array"
report_id: 1248
rtd_name: "Array VM Guest Size & Counts per Array.rtd"
description: "Array VM Guest Size & Counts per Array"
problem_statement: "For any given array or arrays, I nwant to see how many VM Guests are on them and what their usage is"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author rich.rose@aptare.com\n--Last Updated: 10/18/2018\nWITH \nVAR AS (\nSELECT\n'${freeCombo1}' unit,\nDECODE('${freeCombo1}', 'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by\nFROM apt_v_dual\n),\nt1 AS (\nSELECT\nvf.vm_id, vf.vm_name, \nvf.host_id, vf.host_name, \nvf.vm_host_id, vf.vm_host_name, vf.vm_status,\nvf.vmw_datastore_id, vf.datastore_name, \nvf.file_name, \nvf.file_path, \nvf.file_type, \nROUND(vf.file_size/div_by,2) file_size, \nvf.storage_array_id, vf.array_name, \nvf.logical_unit_id, vf.logical_unit_name, \nvf.last_updated\nFROM var, apt_v_vmw_vmfile vf \nWHERE\nvf.storage_array_id IN (${arrays})\nAND vf.logical_unit_id IS NOT NULL\n)\nSELECT\narray_name,\nCOUNT(DISTINCT vm_id) nbr_of_guests,\nCOUNT(DISTINCT vmw_datastore_id) nbr_of_datastores,\nSUM(CASE WHEN file_type = 'VmDisk' THEN file_size ELSE 0 END) vmdk_size,\nSUM(CASE WHEN file_type = 'VmDisk' THEN 0 ELSE file_size END) other_size\nFROM t1\nGROUP BY\narray_name\nORDER BY 4 DESC"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}, {"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors", "virtualization-vmware"]
category_slugs: []
---
