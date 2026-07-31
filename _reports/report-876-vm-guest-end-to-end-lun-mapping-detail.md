---
title: "VM Guest End To End LUN Mapping Detail"
report_id: 876
rtd_name: "VM Guest End To End LUN Mapping Detail.rtd"
description: "VM Guest End To End LUN Mapping Detail"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author rich.rose@aptare.com\n--Last Updated: 06/13/2012\nSELECT\nvm_id, vm_name, \nhost_id, host_name, \nvm_host_id, vm_host_name, vm_status,\nvmw_datastore_id, datastore_name, \nfile_name, file_path, \nfile_type, \nfile_size/1024/1024 file_size, \nstorage_array_id, array_name, \nlogical_unit_id, logical_unit_name, \nlast_updated\nFROM apt_v_vmw_vmfile\nWHERE host_id IN (${hosts})\nAND logical_unit_id IS NOT NULL\nAND file_type = 'VmDisk'"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
