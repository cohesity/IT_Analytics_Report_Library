---
title: "NBU Ultimate Client Status After Retries"
report_id: 911
rtd_name: "NBU Ultimate Client Status After Retries.rtd"
description: "NBU Ultimate Client Status After Retries"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 05/03/2012\nSELECT u.job_id,\nu.nbu_job_id,\nu.client_id,\nc.hostname client,\nu.server_id,\ns.hostname master_server,\nu.schedule_id, \nns.policy_id,\np.policy_name,\nns.schedule_name schedule,\nu.start_date, u.finish_date,\nu.kilobytes/1024/1024 size_gb, \nDECODE(u.overall_status,0,'green',1,'yellow',2,'white',3,'white',4,'red') status_dot,\nDECODE(u.overall_status,0,'Successful',1,'Partial',2,'Queued',3,'Running',4,'Failed') overall_status,\nu.vendor_status, \nu.orig_vendor_status,\nDECODE(was_restarted,0,'No',1,'Yes') was_restarted,  \nu.file_pathlist\nFROM TABLE(nbu_rtd.listJobSummaryAfterRestart(\n${startDate}, \n${endDate},\n100000,\n${spHosts}, \nnull,\nnull,\nnull) ) u, apt_v_server s, apt_v_server c, apt_v_nbu_schedule ns, apt_v_nbu_policy p\nWHERE s.server_id = u.server_id\nAND c.server_id = u.client_id\nAND u.schedule_id = ns.schedule_id (+)\nAND ns.policy_id = p.policy_id (+)\nAND overall_status > DECODE('${freeCombo1}','No',0,'Yes',-1)\nAND overall_status > DECODE('${freeCombo2}','No',1,'Yes',0)\nORDER BY u.start_date"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
