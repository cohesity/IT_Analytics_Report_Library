---
title: "EMC VMAX Pool List"
report_id: 1119
rtd_name: "EMC VMAX Pool List.rtd"
description: "EMC VMAX Pool List"
problem_statement: "I have global storage environment with several EMC VMAX's in different data centers.  I need a report that shows me all all of them in a single pane of glass so I can see which are over-provisioned."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 02/03/2015\n--SELECT ' All' array_name, 'All' array_name FROM apt_v_dual UNION SELECT DISTINCT array_name, array_name FROM aps_v_emc_sym_storage_pool \nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo1}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT\narray_name,\npool_name,\nsp.dev_config raid_type,\nROUND(total_tracks_kb/div_by,2) total_tracks,\nROUND(total_used_tracks_kb/div_by,2) used_tracks,\nROUND((total_tracks_kb-total_used_tracks_kb)/div_by,2) avail_tracks,\nCASE\n  WHEN total_tracks_kb = 0 THEN 0\n  ELSE ROUND(total_used_tracks_kb/total_tracks_kb,2)\nEND pool_used_pct,\nCASE\n  WHEN total_tracks_kb = 0 THEN 0\n  ELSE ROUND(total_used_tracks_kb/total_tracks_kb*100,2)\nEND pct_pool_used,\nROUND(((total_tracks_kb/div_by) * (subscribed_pct/100)),2) subscribed,  \nsubscribed_pct/100 subscribed_pct,\nsubscribed_pct pct_subscribed,\nCASE \n  WHEN subscribed_pct <= 100 THEN 0\n  ELSE ((total_tracks_kb * (subscribed_pct/100))/1024/1024/1024) - (total_tracks_kb/1024/1024/1024) \nEND over_subscribed,\nCASE \n  WHEN subscribed_pct <= 100 THEN 0\n  ELSE ABS((100-subscribed_pct)/100) \nEND over_subscribed_pct,\nCASE \n  WHEN subscribed_pct <= 100 THEN 0\n  ELSE ABS((100-subscribed_pct)) \nEND pct_over_subscribed\nFROM aps_v_emc_sym_storage_pool sp, var\nWHERE  \narray_name LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\nAND array_name is not null"
has_explanation: false
products: [{"slug": "capacity-manager-emc-reports", "name": "EMC Reports"}]
categories: []
product_slugs: ["capacity-manager-emc-reports"]
category_slugs: []
---
