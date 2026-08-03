---
title: "Host Process Summary"
report_id: 1220
rtd_name: "Host Process Summary.rtd"
description: "Host Process Summary"
problem_statement: "I to see which processes (applications) are running on hosts in order to spot potential over comsumption of CPU resources. Additionally, certain hosts need to need to be running certain applications like anti-virus of backup clients, etc.  I need to ensure these process are running on a give set of hosts."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 06/19/2018\nWITH\nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays, \n${startDate} startDate, \nDECODE('${freeCombo1}', 'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual \n)\nSELECT\nserver_id,\nexternal_name,\nprocess_name,\nprocess_owner,\nCOUNT(*) nbr_of_samples,\nAVG(virtual_memory_size_kb/div_by) avg_memory,\nMAX(virtual_memory_size_kb/div_by) max_memory,\nAVG(cpu_usage_pct) avg_cpu_pct,\nMAX(cpu_usage_pct) max_cpu_pct,\nMAX(log_date) last_poll\nFROM apt_v_host_process_log l, var\nWHERE server_id IN (${hosts})\nAND log_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nserver_id,\nexternal_name,\nprocess_name,\nprocess_owner"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
