---
title: "EMC VMAX Array-Pool Breakdown by Pool Used Availaible Oversubscribed"
report_id: 1030
rtd_name: "EMC VMAX Array-Pool Breakdown by Pool Used Available Oversubscribed.rtd"
description: "EMC VMAX Array-Pool Breakdown by Pool Used Availaible Oversubscribed"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 09/12/2011\n--Pie charted version \nSELECT\n'Used' the_metric,\nround(total_used_tracks_kb/1024/1024/1024,2) the_value\nFROM aps_v_emc_sym_storage_pool\nWHERE array_name||' - '||pool_name LIKE '${queryCombo1}'\nUNION\nSELECT\n'Available' the_metric,\nround((total_tracks_kb-total_used_tracks_kb)/1024/1024/1024,2) avail_tracks_tb\nFROM aps_v_emc_sym_storage_pool\nWHERE array_name||' - '||pool_name LIKE '${queryCombo1}'\nUNION\nSELECT\n'Over Subscribed' the_metric,\nCASE \n  WHEN subscribed_pct <= 100 THEN 0\n  ELSE round(((total_tracks_kb * (subscribed_pct/100))/1024/1024/1024) - (total_tracks_kb/1024/1024/1024),2) \nEND over_subscribed\nFROM aps_v_emc_sym_storage_pool\nWHERE array_name||' - '||pool_name LIKE '${queryCombo1}'"
has_explanation: false
products: [{"slug": "capacity-manager-emc-reports", "name": "EMC Reports"}]
categories: []
product_slugs: ["capacity-manager-emc-reports"]
category_slugs: []
---
