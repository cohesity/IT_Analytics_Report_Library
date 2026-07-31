---
title: "Host Count by Array"
report_id: 1050
rtd_name: "Host Count by Array.rtd"
description: "Host Count by Array"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nSELECT nvl(${freeCombo1},'Unknown') metric, count(DISTINCT host_id) host_count\nFROM aps_v_host_luns hl, aps_v_storage_array\nWHERE \nhl.storage_array_id = aps_v_storage_array.storage_array_id\nAND host_id IN (${hosts})\nGROUP BY nvl(${freeCombo1},'Unknown')"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
