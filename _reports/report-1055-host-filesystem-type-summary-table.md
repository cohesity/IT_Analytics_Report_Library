---
title: "Host Filesystem Type Summary Table"
report_id: 1055
rtd_name: "Host Filesystem Type Summary Table.rtd"
description: "Host Filesystem Type Summary Table"
problem_statement: ""
author: "rich.rose@aptare.com\r\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 04/05/2012\n--Total Capacity,Amount Used,Available Capacity,Used %\nWITH t1 AS (\nSELECT \nfile_system_type,host_name,\ncount(filesystem_id) nbr_of_file_systems,\nsum(capacity_kb/1024/1024) capacity_gb,\nsum(used_kb/1024/1024) used_gb,\nsum(capacity_kb/1024/1024) - sum(used_kb/1024/1024) available_gb,\nsum(used_kb/1024/1024)/sum(capacity_kb/1024/1024)*100 used_pct,\nsum(used_kb/1024/1024)/sum(capacity_kb/1024/1024) pct_used\nFROM aps_v_file_system\nWHERE host_id IN (${hosts})\nAND capacity_kb > 0\nGROUP BY\nfile_system_type,host_name\nORDER BY 1\n)SELECT\nnvl(file_system_type,'Other') file_system_type,\nhost_name,\nDECODE('${freeCombo1}',\n'Total Capacity',capacity_gb,\n'Available Capacity',available_gb,\n'Amount Used',used_gb,\n'Used %',used_pct) metric\nFROM t1"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
