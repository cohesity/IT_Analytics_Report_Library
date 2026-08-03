---
title: "Host CPU Performance"
report_id: 1054
rtd_name: "Host CPU Performance.rtd"
description: "Host CPU Performance"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 12/21/2011\nSELECT \ntrunc(log_date,DECODE('${freeCombo1}','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')) the_date, \navg(system_processing_time_pct) avg_system, \navg(user_processing_time_pct) avg_user, \nmax(system_processing_time_pct) max_system\nFROM apt_v_host_cpu_log\nWHERE log_date between ${startDate} AND ${endDate}\nGROUP BY trunc(log_date,DECODE('${freeCombo1}','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year'))"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
