---
title: "NBU Client Version Comparison"
report_id: 1131
rtd_name: "NBU Client Version Comparison w_Last Backup.rtd"
description: "NBU Client Version Comparison"
problem_statement: "I need a report will help identify and ensure that all clients are running on the latest or highest possible version of the NetBackup client agent."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 06/21/2018\nWITH \nlb AS (--Last backup\nSELECT\nlb.client_id,\nMAX(lb.finish_date) last_backup\nFROM apt_v_last_nbu_backup lb\nWHERE\nlb.client_id IN (${hosts})\nAND lb.finish_date > sysdate -7\nGROUP BY lb.client_id\n)\nSELECT\npc.server_id,\ns.hostname,\ncd.client_id,\npc.client_name,\ncd.version,\ncd.patch_level,\ncd.platform,\ncd.installation_path,\nREPLACE(aptStringConcat(DISTINCT pc.policy_name||DECODE(pc.is_active,'Y','','N','*')),',','<br>') policies,\nMAX(cd.last_updated) last_updated,\nMAX(lb.last_backup) last_backup\nFROM apt_v_nbu_client_detail cd, apt_v_nbu_policy_client pc, apt_v_server s, lb\nWHERE \ncd.client_id IN (${hosts})\nAND pc.client_id IN (${hosts})\nAND cd.client_id = pc.client_id (+)\nAND pc.server_id = s.server_id\nAND pc.client_id = lb.client_id (+)\nAND pc.is_active LIKE DECODE('${freeCombo1}','All','%','Active','Y','Inactive','N')\nAND REGEXP_LIKE(pc.policy_name,'${freeText1}')\nGROUP BY\npc.server_id,\ns.hostname,\ncd.client_id,\npc.client_name,\ncd.version,\ncd.patch_level,\ncd.platform,\ncd.installation_path"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
