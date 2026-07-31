---
title: "Ad Hoc Host Attribute Breakdown"
report_id: 1038
rtd_name: "Ad Hoc Host Attribute Breakdown.rtd"
description: "Ad Hoc Host Attribute Breakdown"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nWITH \nt1 AS (\nSELECT ${queryCombo1} attribute,\ncount(hs.host_id) nbr_of_hosts,\nsum(hs.allocated_capacity_gb) allocated_capacity_gb,\nsum(hs.total_nas_capacity_gb) total_nas_capacity_gb\nFROM apt_v_server_attribute sa, aps_v_host_storage hs\nWHERE hs.host_id IN (${hosts})\nAND hs.host_id = sa.host_id\nGROUP BY ${queryCombo1}\n)\nSELECT\nattribute,\nDECODE('${freeCombo1}',\n'# Hosts',nbr_of_hosts,\n'SAN Allocated Capacity',allocated_capacity_gb,\n'NAS Capacity',total_nas_capacity_gb) \nmetric\nFROM t1\nWHERE \nDECODE('${freeCombo1}',\n'# Hosts',nbr_of_hosts,\n'SAN Allocated Capacity',allocated_capacity_gb,\n'NAS Capacity',total_nas_capacity_gb) > 0"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
