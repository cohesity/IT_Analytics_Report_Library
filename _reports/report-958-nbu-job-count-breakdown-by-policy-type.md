---
title: "NBU Job Count Breakdown by Policy Type"
report_id: 958
rtd_name: "NBU Job Count Breakdown by Policy Type.rtd"
description: "NBU Job Count Breakdown by Policy Type"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 12/06/2012\nSELECT\nto_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'MM/DD/YY') the_date,\nROUND(SUM(DECODE(policy_type_name,'Standard',1,0)),2) Standard,\nROUND(SUM(DECODE(policy_type_name,'MS-Windows',1,0)),2) MS_Windows,\nROUND(SUM(DECODE(policy_type_name,'Oracle',1,0)),2) Oracle,\nROUND(SUM(DECODE(policy_type_name,'NDMP',1,0)),2) NDMP,\nROUND(SUM(DECODE(policy_type_name,'MS-Sharepoint',1,0)),2) MS_Sharepoint,\nROUND(SUM(DECODE(policy_type_name,'MS-SQL',1,0)),2) MS_SQL,\nROUND(SUM(DECODE(policy_type_name,'MS-Exchange Server',1,0)),2) MS_Exchange_Server,\nROUND(SUM(DECODE(policy_type_name,'FlashBackup',1,0)),2) FlashBackup,\nROUND(SUM(DECODE(policy_type_name,'Vault',1,0)),2) Vault\nFROM apt_v_nbu_job_detail\nWHERE client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY to_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'MM/DD/YY')"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
