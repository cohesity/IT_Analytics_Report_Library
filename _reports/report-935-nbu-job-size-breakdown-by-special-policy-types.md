---
title: "NBU Job Size Breakdown by Special Policy Types"
report_id: 935
rtd_name: "NBU Job Size Breakdown by Special Policy Types.rtd"
description: "NBU Job Size Breakdown by Special Policy Types"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 10/27/2012\n--Breakdown by Special Policy Types: Oracle,NDMP,MS-Exchange Server,MS-SQL\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo2}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT\nto_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'YYYY/MM/DD') the_date,\nROUND(SUM(DECODE(policy_type_name,'NDMP',kilobytes/var.div_by,0)),2) NDMP,\nROUND(SUM(DECODE(policy_type_name,'Oracle',kilobytes/var.div_by,0)),2) Oracle,\nROUND(SUM(DECODE(policy_type_name,'MS-SQL',kilobytes/var.div_by,0)),2) MS_SQL,\nROUND(SUM(DECODE(policy_type_name,'MS-Exchange Server',kilobytes/var.div_by,0)),2) MS_Exchange_Server,\nROUND(SUM(CASE WHEN policy_type_name NOT IN ('NDMP','Oracle','MS-SQL','MS-Exchange Server') THEN kilobytes/var.div_by ELSE 0 END),2) all_others\nFROM apt_v_nbu_job_detail, var\nWHERE client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY to_char(trunc(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'YYYY/MM/DD')\nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
