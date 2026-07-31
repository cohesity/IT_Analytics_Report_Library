---
title: "Tier 1 Storage Breakdown by Environment"
report_id: 1057
rtd_name: "Tier 1 Storage breakdown by Environment.rtd"
description: "Tier 1 Storage breakdown by Environment"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: false
has_sql: true
sql_query: "WITH p1 AS\n(\nselect policy_name, host_id, total_gb \nFROM table (srm_rtd.listChargebackByLUNSummary(100000,\nnumberListType(),\nnumberListType(),\nnumberListType(),\nnumberListType(${serverGroups}),\n1))\n),\nt1 as (\nSELECT\nhost_id,  \nsum(total_gb) total_tiered_gb,\nsum(DECODE(policy_name,'Tier 1',total_gb,0)) total_tier_1_gb,\nsum(DECODE(policy_name,'Tier 2',total_gb,0)) total_tier_2_gb,\nsum(DECODE(policy_name,'Tier 3',total_gb,0)) total_tier_3_gb,\nsum(DECODE(policy_name,'HDP Tier',total_gb,0)) total_HDP_Tier_gb\nFROM p1\nGROUP BY host_id\n),\nt3 as (\nSELECT\nhs.host_id,\nhs.host_name,\ns.display_name,\nnvl(rtd.getServerAttributeValue(hs.host_id,'Environment'),'Other') environment,\ntotal_tiered_gb,\ntotal_tier_1_gb,\ntotal_tier_2_gb,\ntotal_tier_3_gb,\ntotal_HDP_Tier_gb,\ntotal_tiered_gb - total_san_capacity_gb allocated_but_not_used_gb,\ntotal_san_capacity_gb,\nsan_pct_used,\ntotal_nas_capacity_gb,\nnas_pct_used,\ntotal_das_capacity_gb,\ndas_pct_used\nFROM aps_v_host_storage hs,t1,apt_v_server s\nWHERE hs.host_id in (${hosts})\nAND hs.host_id = t1.host_id (+)\nAND hs.host_id = s.server_id (+)\n)\nSELECT environment,\nsum(total_tier_1_gb/1024) tier_1_tb,\nsum(total_tier_2_gb/1024) tier_2_tb,\nsum(total_tier_3_gb/1024) tier_3_tb,\nsum(total_HDP_Tier_gb/1024) hdp_tb\nFROM t3\ngroup by environment"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
