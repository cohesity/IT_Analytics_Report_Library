---
title: "Avamar Clients With The Most New Data"
report_id: 1195
rtd_name: "Avamar Clients With The Most New Data.rtd"
description: "Avamar Clients With The Most New Data"
problem_statement: ""
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 03/20/2018\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo2}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\nt1 AS (\nSELECT\nserver_name,\nclient_name,\ngroup_name,\nCOUNT(*) nbr_of_jobs,\nMAX(Scanned_kb/div_by) max_scanned,\nSUM(new_kb/div_by) AS new_data\nFROM apt_v_avm_activities,var\nWHERE \nclient_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nAND group_name <> 'none'\nGROUP BY \nserver_name, \nclient_name, \ngroup_name\nORDER BY  \nSUM(new_kb) DESC\n),\nt2 AS (\nSELECT\nserver_name,\nclient_name,\nREPLACE(aptStringConcat(DISTINCT group_name),',','<br>') the_groups,\nCOUNT(nbr_of_jobs) nbr_of_jobs,\nMAX(max_scanned) max_scanned,\nSUM(new_data) AS new_data\nFROM t1\nGROUP BY\nserver_name,\nclient_name\nORDER BY\nnew_data DESC\n)\nSELECT * \nFROM t2\nWHERE ROWNUM <= ${freeCombo1} "
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
