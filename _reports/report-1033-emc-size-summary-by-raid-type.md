---
title: "EMC Size Summary by RAID Type"
report_id: 1033
rtd_name: "EMC Size Summary by RAID Type.rtd"
description: "EMC Size Summary by RAID Type"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "SELECT storage_array_id,array_name,raid_type,\nsum(total_capacity_gb/1024) total_capacity_tb,\nsum(DECODE(is_mapped,'Y',total_capacity_gb,0)/1024) mapped_capacity_tb,\nsum(DECODE(is_mapped,'N',total_capacity_gb,0)/1024) umapped_capacity_tb,\nsum(nbr_of_luns) nbr_of_luns,\nsum(DECODE(is_mapped,'Y',nbr_of_luns,0)) mapped_nbr_of_luns,\nsum(DECODE(is_mapped,'N',nbr_of_luns,0)) unmapped_nbr_of_luns\nFROM aps_v_emc_sym_logical_unit\nGROUP BY storage_array_id,array_name,raid_Type"
has_explanation: false
products: [{"slug": "capacity-manager-emc-reports", "name": "EMC Reports"}]
categories: []
product_slugs: ["capacity-manager-emc-reports"]
category_slugs: []
---
