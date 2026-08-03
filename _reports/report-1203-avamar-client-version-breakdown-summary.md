---
title: "Avamar Client Version Breakdown Summary"
report_id: 1203
rtd_name: "Avamar Client Version Breakdown Summary.rtd"
description: "Avamar Client Version Breakdown Summary"
problem_statement: "Displays a summarized view of the number of clients per version of Avamar.  Useful for planning for timing of upgrades and knowing how many clients are out of compliance."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 06/11/2018\nWITH \nvar AS (\nSELECT '${freeText1}' the_version FROM apt_v_dual\n),\nt1 AS (\nSELECT\nac.client_id,\nac.agent_version,\nSUBSTR(ac.agent_version,1,3) short_version\nFROM apt_v_avm_clients ac, var\nWHERE \nac.client_id IN (${hosts})\nAND ac.backup_date BETWEEN ${startDate} AND ${endDate}\nAND agent_version NOT LIKE '%unKnown%'\nAND agent_version NOT LIKE '%Unknown%'\nAND agent_version IS NOT NULL\n)\nSELECT\nDECODE('${freeCombo1}','Normalized',short_version,'Detailed',agent_version) version_name,\nCOUNT(*) version_count\nFROM t1\nGROUP BY \nDECODE('${freeCombo1}','Normalized',short_version,'Detailed',agent_version)\nORDER BY 2 DESC"
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
