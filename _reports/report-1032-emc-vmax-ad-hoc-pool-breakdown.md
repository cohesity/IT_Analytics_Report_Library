---
title: "EMC VMAX Ad Hoc Pool Breakdown"
report_id: 1032
rtd_name: "EMC VMAX Ad Hoc Pool Breakdown.rtd"
description: ""
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 08/23/2011\n--EMC VMAX Pool subscription by Total,Used,Available,Subscribed,Over Subscribed\nWITH q1 AS (\nSELECT\npool_name,\nsp.dev_config raid_type,\nround(total_tracks_kb/1024/1024/1024,2) total_tracks,\nround(total_used_tracks_kb/1024/1024/1024,2) used_tracks,\nround((total_tracks_kb-total_used_tracks_kb)/1024/1024/1024,2) avail_tracks,\nround((total_tracks_kb * (subscribed_pct/100))/1024/1024/1024,2) subscribed,  \nCASE \n  WHEN subscribed_pct <= 100 THEN 0\n  ELSE ((total_tracks_kb * (subscribed_pct/100))/1024/1024/1024) - (total_tracks_kb/1024/1024/1024) \nEND over_subscribed\nFROM aps_v_emc_sym_storage_pool sp\nWHERE  \narray_name = '${queryCombo1}'\nAND array_name is not null\n)\nSELECT\npool_name,\nDECODE('${freeCombo1}',\n'Total Capacity',total_tracks,\n'Used Capacity',used_tracks,\n'Available Capacity',avail_tracks,\n'Amount Subscribed',subscribed,\n'Amount Over Subscribed',over_subscribed\n) metric\nFROM q1"
has_explanation: false
products: [{"slug": "capacity-manager-emc-reports", "name": "EMC Reports"}]
categories: []
product_slugs: ["capacity-manager-emc-reports"]
category_slugs: []
---
