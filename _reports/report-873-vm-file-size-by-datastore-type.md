---
title: "VM File Size by Datastore/Type"
report_id: 873
rtd_name: "VM File Size by Datastore Type.rtd"
description: "VM File Size by Datastore Type"
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
sql_query: "SELECT file_type, datastore_name, sum(file_size/1024/1024) size_gb \nFROM apt_v_vmw_vmfile\nGROUP BY file_type, datastore_name"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
