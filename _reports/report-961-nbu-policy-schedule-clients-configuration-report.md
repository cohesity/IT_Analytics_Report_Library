---
title: "NBU Policy Schedule Clients Configuration Report"
report_id: 961
rtd_name: "NBU Policy Schedule Clients Configuration Report.rtd"
description: "NBU Policy Schedule Clients Configuration Report"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/09/2012\nSELECT \ns.hostname master_server,\npc.policy_id,\npc.policy_name, \np.policy_type_name,\np.is_active,\np.storage_unit,\nvp.volume_pool_name,\nsc.schedule_id,\nsc.schedule_name schedule_name,\nDECODE(sc.selection_type,1,'Frequency Based',2,'Calendar Based') selection_type,\nDECODE(sc.mon_start,null,null,sc.mon_start||' - '||sc.mon_end||'<br/>')||\nDECODE(sc.tue_start,null,null,sc.tue_start||' - '||sc.tue_end||'<br/>')||\nDECODE(sc.wed_start,null,null,sc.wed_start||' - '||sc.wed_end||'<br/>')||\nDECODE(sc.thu_start,null,null,sc.thu_start||' - '||sc.thu_end||'<br/>')||\nDECODE(sc.fri_start,null,null,sc.fri_start||' - '||sc.fri_end||'<br/>')||\nDECODE(sc.sat_start,null,null,sc.sat_start||' - '||sc.sat_end||'<br/>')||\nDECODE(sc.sun_start,null,null,sc.sun_start||' - '||sc.sun_end||'<br/>') cal_days,\nDECODE(\nsc.frequency,3600,'Every Hour',\n7200,'Every 2 Hours',\n64800,'Every 18 Hours',\n72000,'Every 20 Hours',\n82800,'Every 23 Hours',\n86400,'Every Day',\n345600,'Every 4 Days',\n604800,'Every 7 Days',\n21168000,'Every 245 Days',\nNULL,'Calendar') frequency,\nDECODE(sc.schedule_type,\n0,'Full Backup',\n1,'Cumulative Incremantal',\n2,'Application Backup',\n4,'Differential Incremental',\n5,'Archive') backup_type,\nDECODE(sc.retention_days,\n9999,'Never Expires',\n-1,'Expires Immediately',\nsc.retention_days||' Days') Retain_Data_For,\nREPLACE(aptStringConcat(DISTINCT pc.client_name),',','<br />') clients,\nREPLACE(aptStringConcat(DISTINCT pf.pathname),',','<br />') paths\nFROM apt_v_nbu_policy_client pc, apt_v_nbu_policy_file pf, apt_v_nbu_policy p, apt_v_server s,\napt_v_nbu_volume_pool vp, apt_v_nbu_schedule sc\nWHERE \npc.client_id IN (${hosts})\nAND p.policy_id = sc.policy_id \nAND p.policy_id = pc.policy_id\nAND pc.policy_id = pf.policy_id\nAND p.server_id = s.server_id\nAND p.is_active = DECODE('${freeCombo1}','All',p.is_active,'Active','Y','Inactive','N')\nAND p.policy_type_name = DECODE('${freeCombo2}','All',p.policy_type_name,'${freeCombo2}')\nAND p.volume_pool_id = vp.volume_pool_id (+)\nGROUP BY s.hostname,\npc.policy_id,\npc.policy_name,\np.policy_type_name, \np.is_active,\nstorage_unit,\nvp.volume_pool_name,\nsc.schedule_id,\nsc.schedule_name,\nDECODE(sc.selection_type,1,'Frequency Based',2,'Calendar Based'),\nDECODE(sc.mon_start,null,null,sc.mon_start||' - '||sc.mon_end||'<br/>')||\nDECODE(sc.tue_start,null,null,sc.tue_start||' - '||sc.tue_end||'<br/>')||\nDECODE(sc.wed_start,null,null,sc.wed_start||' - '||sc.wed_end||'<br/>')||\nDECODE(sc.thu_start,null,null,sc.thu_start||' - '||sc.thu_end||'<br/>')||\nDECODE(sc.fri_start,null,null,sc.fri_start||' - '||sc.fri_end||'<br/>')||\nDECODE(sc.sat_start,null,null,sc.sat_start||' - '||sc.sat_end||'<br/>')||\nDECODE(sc.sun_start,null,null,sc.sun_start||' - '||sc.sun_end||'<br/>'),\nsc.frequency,\nDECODE(\nsc.frequency,3600,'Every Hour',\n7200,'Every 2 Hours',\n64800,'Every 18 Hours',\n72000,'Every 20 Hours',\n82800,'Every 23 Hours',\n86400,'Every Day',\n345600,'Every 4 Days',\n604800,'Every 7 Days',\n21168000,'Every 245 Days',\nNULL,'Calendar'),\nDECODE(sc.schedule_type,\n0,'Full Backup',\n1,'Cumulative Incremantal',\n2,'Application Backup',\n4,'Differential Incremental',\n5,'Archive'),\nDECODE(sc.retention_days,\n9999,'Never Expires',\n-1,'Expires Immediately',\nsc.retention_days||' Days')\nORDER BY 2"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
