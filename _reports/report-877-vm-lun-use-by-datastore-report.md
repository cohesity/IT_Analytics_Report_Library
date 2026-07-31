---
title: "VM LUN Use by Datastore Report"
report_id: 877
rtd_name: "VM LUN Use by Datastore Report.rtd"
description: "VM LUN Use by Datastore Report"
problem_statement: "I want to choose a datastore and see the vm files and the LUNS that contain those files so I can troubleshoot performance issues."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 10/10/2018\n--Minimum version required: 10.2.0\nSELECT \nvm_host_id, \nvm_host_name, \nvmw_datastore_id, \ndatastore_name,\nstorage_array_id, \narray_name,  \nlogical_unit_id, \nlogical_unit_name,\nfile_name, \nSUM(file_size/1024) file_size\nFROM \napt_v_vmw_vmfile\nWHERE\nvmw_datastore_id IN (${datastores})\nAND storage_array_id IS NOT NULL\nGROUP BY\nvm_host_id, \nvm_host_name, \nvmw_datastore_id, \ndatastore_name,\nstorage_array_id, \narray_name,  \nlogical_unit_id, \nlogical_unit_name,\nfile_name\nORDER BY vm_host_name"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
