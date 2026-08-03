---
title: "NBU Job Size Over Time Breakdown by Policy Type"
report_id: 1276
rtd_name: "NBU Job Size Over Time Breakdown by Policy Type.rtd"
description: "NBU Job Size Over Time Breakdown by Policy Type"
problem_statement: "I need to know which policies are writing the most"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--rich.rose@vertias.com\n--Last Modified: 03/16/2022\nWITH \nvar AS (\nSELECT\n  DECODE('${freeCombo2}',\n    'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM\n  apt_v_dual\n)\nSELECT\n  TO_CHAR(TRUNC(start_date,DECODE('${freeCombo1}',\n    'Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'YYYY/MM/DD') AS the_date,\n  policy_type_name,\n    ROUND(SUM(kilobytes/var.div_by),2) AS job_size\nFROM\n  apt_v_nbu_job_detail,\n  var\nWHERE\n  client_id IN (${hosts})\n  AND start_date BETWEEN ${startDate} AND ${endDate}\n  AND job_type <> 105 -- Do not include Restores\nGROUP BY\n  TO_CHAR(TRUNC(start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')),'YYYY/MM/DD'),\n  policy_type_name\nORDER BY\n  1,3 DESC"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
