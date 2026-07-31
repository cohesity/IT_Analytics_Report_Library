---
title: "NBU Policy Count by Type"
report_id: 924
rtd_name: "NBU Policy Count by Type.rtd"
description: "NBU Policy Count by Type"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/09/2011\n--This will summarize the number of policies defined on each master server by their type.\n--The drilldown report NBU Policy List.D is required for drilldowns to work.\nSELECT\ns.server_id,\ns.hostname master_server,\n'${freeCombo1}' the_state,\nsum(DECODE(policy_type,0,1,0)) Standard,\nsum(DECODE(policy_type,4,1,0)) Oracle,\nsum(DECODE(policy_type,6,1,0)) Informix_OnBar,\nsum(DECODE(policy_type,7,1,0)) sybase,\nsum(DECODE(policy_type,8,1,0)) MS_SharePoint,\nsum(DECODE(policy_type,10,1,0)) Netware,\nsum(DECODE(policy_type,13,1,0)) MS_Windows,\nsum(DECODE(policy_type,15,1,0)) MS_SQL_Server,\nsum(DECODE(policy_type,16,1,0)) MS_Exchange_Server,\nsum(DECODE(policy_type,17,1,0)) SAP,\nsum(DECODE(policy_type,18,1,0)) DB2,\nsum(DECODE(policy_type,19,1,0)) NDMP,\nsum(DECODE(policy_type,20,1,0)) FlashBackup,\nsum(DECODE(policy_type,22,1,0)) AFS,\nsum(DECODE(policy_type,24,1,0)) DataStore,\nsum(DECODE(policy_type,25,1,0)) Lotus_Notes,\nsum(DECODE(policy_type,26,1,0)) NCR_Teradata,\nsum(DECODE(policy_type,29,1,0)) FlashBackup2,\nsum(DECODE(policy_type,30,1,0)) vault,\nsum(DECODE(policy_type,35,1,0)) Catalog\nFROM apt_v_nbu_policy np, apt_v_server s\nWHERE np.server_id IN (${hosts})\nAND np.server_id = s.server_id\nAND is_active = DECODE('${freeCombo1}','All',is_active,'Active','Y','Inactive','N')\nGROUP BY s.server_id, s.hostname, '${freeCombo1}'"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
