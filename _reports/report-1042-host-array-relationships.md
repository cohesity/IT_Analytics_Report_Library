---
title: "Host Array Relationships"
report_id: 1042
rtd_name: "Host Array Relationships.rtd"
description: "Host Array Relationships"
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
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nWITH \nt1 AS (\nSELECT\nDISTINCT\nlh.host_id,\nlu.storage_array_id,\nlu.logical_unit_id,\nlu.total_capacity_gb\nFROM aps_v_lun_hosts lh, aps_v_logical_unit lu\nWHERE lh.logical_unit_id = lu.logical_unit_id\nAND host_id IN (${hosts})\n),\nt2 AS (\nSELECT\nnvl(rtd.getObjectAttributeValue(t1.storage_array_id,'Site','A'),'Other') Site,\nt1.host_id,\nh.host_name,\nt1.storage_array_id,\nsa.array_name,\nsa.array_family,\nsa.capacity_gb array_capacity_gb,\ncount(t1.logical_unit_id) nbr_of_luns,\nsum(t1.total_capacity_gb) total_capacity_gb\nFROM t1, aps_v_host h, aps_v_storage_array sa\nWHERE t1.host_id = h.host_id\nAND t1.storage_array_id = sa.storage_array_id\nGROUP BY \nnvl(rtd.getObjectAttributeValue(t1.storage_array_id,'Site','A'),'Other'),\nt1.host_id,\nh.host_name,\nt1.storage_array_id,\nsa.array_name,\nsa.array_family,\nsa.capacity_gb\n)\nSELECT\nsite,\nhost_id,\nhost_name,\nnbr_of_luns,\ntotal_capacity_gb,\ntotal_capacity_gb/array_capacity_gb*100 pct_of_array,\nstorage_array_id,\narray_name,\narray_family\nFROM t2"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
