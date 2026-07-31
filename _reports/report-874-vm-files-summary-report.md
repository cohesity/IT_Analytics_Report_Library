---
title: "VM Files Summary Report"
report_id: 874
rtd_name: "VM Files Summary Report.rtd"
description: "VM Files Summary Report"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 05/25/2012\n--Minimum version required 8.2.0\n--Mimics the canned report VM Files Summary \n--Designed be used as a basis for other reports\nSELECT \nfile_name, \nfile_path,\nvmw_datastore_id, \ndatastore_name,\nvm_host_id, \nvm_host_name, \nvm_id, \nvm_name, \nhost_id, \nhost_name, \nvm_status,\nfile_type, \nfile_size/1024 file_size, \nlogical_unit_id, \nlogical_unit_name,\nstorage_array_id, \narray_name,  \nlast_updated \nFROM \napt_v_vmw_vmfile\nWHERE\nhost_id IN (${hosts})\nAND storage_array_id IS NOT NULL"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
