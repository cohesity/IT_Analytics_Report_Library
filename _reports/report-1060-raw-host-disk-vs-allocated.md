---
title: "Raw Host Disk vs Allocated"
report_id: 1060
rtd_name: "Raw Host Disk vs Allocated.rtd"
description: "Raw Host Disk vs Allocated"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Updated: 05/30/2012\nWITH \nt1 as (-- add up the size of all the disks\nSELECT host_id,\ncount(distinct disk_id) nbr_of_disks,\nsum(size_kb/1024/1024) disk_size_gb\nFROM aps_v_host_disk\nWHERE host_id IN (${hosts})\nGROUP BY host_id\n)\nSELECT \nhs.host_id, hs.host_name, t1.nbr_of_disks, t1.disk_size_gb, hs.seen_by_host_gb,hs.allocated_capacity_gb\nFROM aps_v_host_storage hs, t1\nWHERE t1.host_id = hs.host_id"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
