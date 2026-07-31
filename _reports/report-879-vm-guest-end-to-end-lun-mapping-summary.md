---
title: "VM Guest End To End LUN Mapping Summary"
report_id: 879
rtd_name: "VM Guest End To End LUN Mapping Summary.rtd"
description: "VM Guest End To End LUN Mapping Summary"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 06/13/2012\nSELECT\nvm_id, vm_name, \nhost_id, host_name, \nvm_host_id, vm_host_name, \nvmw_datastore_id, datastore_name, \ncount(DISTINCT file_name) vmdk_files,  \nsum(file_size/1024/1024) file_size, \naptStringConcat(DISTINCT array_name) array_names, \ncount(DISTINCT logical_unit_id) LUNs\nFROM apt_v_vmw_vmfile\nWHERE host_id IN (${hosts})\nAND logical_unit_id IS NOT NULL\nAND file_type = 'VmDisk'\nGROUP BY\nvm_id, vm_name, \nhost_id, host_name, \nvm_host_id, vm_host_name, \nvmw_datastore_id, datastore_name"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
