---
title: "Storage Use For Clusters"
report_id: 1047
rtd_name: "Storage Use For Clusters.rtd"
description: "Storage Use For Clusters"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nWITH t1 AS (\nSELECT DISTINCT logical_unit_id, host_id\nFROM aps_v_storage_path\nWHERE host_id IN (${hosts})         \n),\nt2 as (\nSELECT logical_unit_id,count(distinct host_id) host_count,\nmin(host_id) a_host_in_the_cluster \nfrom t1\ngroup by logical_unit_id\nhaving count(distinct host_id) > 1\n),\nt3 as (\nSelect DISTINCT a_host_in_the_cluster,host_count from t2\n)\nSELECT t3.host_count,hs.* \nFROM aps_v_host_storage hs, t3\nWHERE t3.a_host_in_the_cluster = hs.host_id"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
