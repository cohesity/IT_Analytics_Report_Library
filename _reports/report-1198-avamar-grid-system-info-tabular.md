---
title: "Avamar Grid System Info Tabular"
report_id: 1198
rtd_name: "Avamar Grid System Info Tabular.rtd"
description: "Avamar Grid System Info Tabular"
problem_statement: "See a list of all of my Avamar instances"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 04/03/2018\nWITH \nvar AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays,\nDECODE('${freeCombo1}',\n'KB',1,'MB',(1024),'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\nn1 AS (--Get the nodes and their capacities\nSELECT\nn.master_server_id,\nCOUNT(DISTINCT n.node_id) nodes,\nREPLACE(aptStringConcat(DISTINCT version),',','<br>') versions,\nSUM(n.total_capacity_kb/div_by) nodes_total_capacity,\nSUM((n.total_capacity_kb-n.used_capacity_kb)/div_by) nodes_free_capacity,\nSUM(n.used_capacity_kb/div_by) nodes_used_capacity\nFROM apt_v_avm_node n, var, apt_v_server s\nWHERE\nn.master_server_id IN (${hosts})\nAND s.server_id = n.master_server_id\nGROUP BY \nn.master_server_id\n),\ndp AS (--Data Protected according to Avamar\nSELECT\nds.master_server_id,\nMAX(ds.data_protected_kb) data_protected_kb\nFROM apt_v_avm_dpn_statistics ds, apt_v_server s\nWHERE \nds.master_server_id IN (${hosts})\nAND s.server_id = master_server_id\nGROUP BY master_server_id\n),\nt2 AS (--Get the highest value for each client/plugin combination\nSELECT \naa.server_id, \naa.client_id,\naa.plugin_id,\nMAX(aa.scanned_kb) scanned_kb\nFROM apt_v_avm_activities aa, var, apt_v_server s\nWHERE\naa.server_id IN (${hosts}) \nAND aa.scanned_kb > 0\nAND aa.expiration_date > sysdate\nAND s.server_id = aa.server_id\nGROUP BY \naa.server_id,\nclient_id,\nplugin_id\n),\nt3 AS (--Add them up and this should be the \"Front End \" size of each client on the grid\nSELECT \nt2.server_id master_server_id,\nCOUNT(DISTINCT client_id) clients,\nSUM(t2.scanned_kb) scanned_kb\nFROM t2\nGROUP BY \nt2.server_id\n)\nSELECT \nms.axion_system_id,\nms.gsan_system_name, \nms.gsan_system_id, \nms.master_server_id, \nms.hfs_address,\nms.local_hfs_address, \nms.hfs_port, \nms.mcs_port, \nms.gsan_run_level, \nDECODE(ms.gsan_run_level,'up','green','degraded','yellow','red') run_level_dot,\nt3.clients,\nt3.scanned_kb/div_by scanned,\ndp.data_protected_kb/div_by data_protected,\nROUND((dp.data_protected_kb / used_capacity_kb),1)||':1' dedup_ratio,\n((ms.total_capacity_kb - ms.used_capacity_kb)*(dp.data_protected_kb / ms.used_capacity_kb))/div_by est_available_capacity,\nms.total_capacity_kb/var.div_by total_capacity,\n(ms.total_capacity_kb - ms.used_capacity_kb)/div_by available_capacity,\nms.used_capacity_kb/var.div_by used_capacity,  \n(ms.used_capacity_kb/DECODE(ms.total_capacity_kb,0,null,ms.total_capacity_kb)) used_pct,\n(ms.used_capacity_kb/DECODE(ms.total_capacity_kb,0,null,ms.total_capacity_kb))*100 pct_used,\nms.protected_bytes_quota, \nms.license_expiration_date, \nms.time_since_server_init, \nrtd.secsToHoursMinSecs(ms.time_since_server_init) time_since_server_init_hrs, \nms.last_updated_in_avm, \nms.last_checkpoint, \nms.last_validated_checkpoint,\nn1.nodes,\nn1.versions,\nn1.nodes_total_capacity,\nn1.nodes_used_capacity, \nn1.nodes_free_capacity\nFROM apt_v_avm_axion_system ms, var, n1, dp, t3, apt_v_server s\nWHERE \nms.master_server_id IN (${hosts})\nAND s.server_id = ms.master_server_id\nAND ms.master_server_id = n1.master_server_id\nAND ms.master_server_id = dp.master_server_id(+)\nAND ms.master_server_id = t3.master_server_id(+)"
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
