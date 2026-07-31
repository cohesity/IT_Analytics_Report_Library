---
title: "NBU Client Exclude List CL"
report_id: 1205
rtd_name: "NBU Client Exclude List CL.rtd"
description: "NBU Client Exclude List CL"
problem_statement: "Show a list of which drives and directories are excluded from backup so I can be sure that nothing is accidently missed."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 12/13/2018\nSELECT\nx.server_id,\nx.server_name master_server,\nx.client_id,\nc.hostname client,\nx.policy_id,\np.policy_name policy,\nREPLACE(aptStringConcat(DISTINCT x.path),',','<br>') excluded_paths\nFROM\napt_v_nbu_incld_excld_path x, apt_v_server c, apt_v_nbu_policy p\nWHERE\nx.client_id IN (${hosts}) \nAND x.include_exclude = 'Exclude'\nAND x.client_id = c.server_id\nAND x.policy_id = p.policy_id\nGROUP BY\nx.server_id,\nx.server_name,\nx.client_id,\nc.hostname,\nx.policy_id,\np.policy_name"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
