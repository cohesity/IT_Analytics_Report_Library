---
title: "HDS DP LUN Perspective Storage"
report_id: 1071
rtd_name: "HDS DP LUN Perspective Storage.rtd"
description: "HDS DP LUN Perspective Storage"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--This takes a pipe separated list of array names and pool numbers as wildcards NOTE: Use * for all \n--EXAMPLE Array(s): USP_12|USP_13 Pool: 1|2|3|4\n--or Array(s): USP_12 Pool(s):*\n--or Array(s):* Pool(s):*\nWITH \nl1 as (--Get all the distinct LUNS\nSELECT DISTINCT\nhlu.array_name,\nhlu.logical_unit_id,\nhlu.logical_unit_name,\nlu.status,\nlu.total_capacity_gb,\nhlu.consumed_capacity_gb\nFROM aps_v_hds_logical_unit hlu, aps_v_logical_unit lu\nWHERE lu.logical_unit_id = hlu.logical_unit_id \nAND hlu.dp_type = 0\nAND REGEXP_LIKE(hlu.array_name,'${freeText1}', 'i')\nAND REGEXP_LIKE(hlu.dp_pool_id,'${freeText2}', 'i')\n),\nh1 as (\nSELECT \nhlu.array_name,\nhlu.logical_unit_id,\nhlu.logical_unit_name,\nsp.total_capacity_gb,\nhlu.consumed_capacity_gb,\ncount(DISTINCT sp.host_storage_domain) nbr_of_hosts,\naptStringConcat(DISTINCT sp.host_storage_domain) hosts\nFROM aps_v_storage_path sp, aps_v_hds_logical_unit hlu\nWHERE sp.logical_unit_id = hlu.logical_unit_id (+)\nAND REGEXP_LIKE(hlu.array_name,'${freeText1}', 'i')\nAND REGEXP_LIKE(hlu.dp_pool_id,'${freeText2}', 'i')\nAND hlu.dp_type = 0\nGROUP BY\nhlu.array_name,\nhlu.logical_unit_id,\nhlu.logical_unit_name,\nsp.total_capacity_gb,\nhlu.consumed_capacity_gb\n)\nSELECT\nl1.array_name,\nl1.logical_unit_name,\nl1.status,\nl1.total_capacity_gb,\nl1.consumed_capacity_gb,\n(l1.consumed_capacity_gb/(l1.total_capacity_gb+.0001))*100 pct_consumed,\n(l1.consumed_capacity_gb/(l1.total_capacity_gb+.0001)) pct_consumed_bar,\nh1.nbr_of_hosts,\nCASE WHEN h1.nbr_of_hosts > 1\nTHEN SUBSTR(h1.hosts, 1 ,INSTR(h1.hosts, ',', 1, 1)-1) \nELSE h1.hosts\nEND hosts,\nhosts all_hosts\nFROM l1,h1\nWHERE \nl1.logical_unit_id = h1.logical_unit_id(+)\nORDER BY 1,2"
has_explanation: false
products: [{"slug": "capacity-manager-hds-reports", "name": "HDS Reports"}]
categories: []
product_slugs: ["capacity-manager-hds-reports"]
category_slugs: []
---
