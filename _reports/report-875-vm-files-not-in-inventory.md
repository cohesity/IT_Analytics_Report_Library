---
title: "VM Files Not in Inventory"
report_id: 875
rtd_name: "VM Files Not in Inventory.rtd"
description: "VM Files Not in Inventory"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "SELECT vmw_datastore_id, datastore_name, file_path,file_name, file_size/1024/1024 file_size_gb, last_updated\nFROM apt_v_vmw_vmfile_not_inventory\nWHERE datastore_name LIKE DECODE('${queryCombo1}','All','%','${queryCombo1}')\nORDER BY file_size DESC"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
