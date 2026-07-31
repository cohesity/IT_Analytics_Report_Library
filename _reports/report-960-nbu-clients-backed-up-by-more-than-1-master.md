---
title: "NBU Clients Backed up by More than 1 Master"
report_id: 960
rtd_name: "NBU Clients Backed up by More than 1 Master.rtd"
description: "NBU Clients Backed up by More than 1 Master"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Athor: rich.rose@aptare.com\n--Last Modified: 06/05/2012\nSELECT\nclient_id,client_host_name,\ncount(DISTINCT server_id) server_id_count,\nsum(kilobytes/1024/1024) actual_gb,\nsum(kilobytes/1024/1024)/2 wasted_gb,\naptStringConcat(DISTINCT master_host_name) master_servers\nFROM apt_v_nbu_job \nWHERE \nclient_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nAND client_host_name <> 'NONE'\nGROUP BY \nclient_id,client_host_name\nHAVING\ncount(DISTINCT server_id) > 1"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
