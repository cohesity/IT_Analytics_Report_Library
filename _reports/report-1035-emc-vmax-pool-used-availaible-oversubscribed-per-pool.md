---
title: "EMC VMAX Pool Used Availaible Oversubscribed per Pool"
report_id: 1035
rtd_name: "EMC VMAX Pool Used Available Oversubscribed per Pool.rtd"
description: "EMC VMAX Pool Used Availaible Oversubscribed per Pool"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 09/12/2011\nWITH q1 AS (\nSELECT\narray_name,\npool_name,\nsp.dev_config raid_type,\nround(total_tracks_kb/1024/1024/1024,2) total_tracks_tb,\nround(total_used_tracks_kb/1024/1024/1024,2) used_tracks_tb,\nround((total_tracks_kb-total_used_tracks_kb)/1024/1024/1024,2) avail_tracks_tb,\nCASE\n  WHEN total_tracks_kb = 0 THEN 0\n  ELSE total_used_tracks_kb/total_tracks_kb*100\nEND pool_used_pct,\nround((total_tracks_kb * (subscribed_pct/100))/1024/1024/1024,2) subscribed_tb,  \nsubscribed_pct,\nCASE \n  WHEN subscribed_pct <= 100 THEN 0\n  ELSE round(((total_tracks_kb * (subscribed_pct/100))/1024/1024/1024) - (total_tracks_kb/1024/1024/1024),2) \nEND over_subscribed\nFROM aps_v_emc_sym_storage_pool sp\nWHERE array_name LIKE '${queryCombo1}'\n)\nSELECT\npool_name,\nsum(total_tracks_tb) total_tracks_tb,\nsum(used_tracks_tb) used_tracks_tb,\nsum(avail_tracks_tb) avail_tracks_tb,\nsum(subscribed_tb) subscribed_tb,\nsum(over_subscribed) over_subscribed\nFROM q1 \nGROUP BY pool_name"
has_explanation: false
products: [{"slug": "capacity-manager-emc-reports", "name": "EMC Reports"}]
categories: []
product_slugs: ["capacity-manager-emc-reports"]
category_slugs: []
---
