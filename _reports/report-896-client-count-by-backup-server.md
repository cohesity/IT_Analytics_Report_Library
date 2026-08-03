---
title: "Client Count by Backup Server"
report_id: 896
rtd_name: "Client Count by Backup Server.rtd"
description: "Client Count by Backup Server"
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
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nSELECT \nto_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'MM/DD/YY') the_date,\nserver_name,\ncount(DISTINCT client_id) client_count\nFROM apt_v_job\nWHERE client_id in (${hosts})\nAND finish_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY to_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'MM/DD/YY'),server_name\nUNION ALL\nSELECT \nto_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'MM/DD/YY') the_date,\n'~Total' server_name,\ncount(DISTINCT client_id) client_count\nFROM apt_v_job\nWHERE client_id in (${hosts})\nAND finish_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY to_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'MM/DD/YY'),'~Total'\nORDER BY 2,1"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
