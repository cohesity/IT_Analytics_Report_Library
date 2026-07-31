---
title: "NBU Policy Clients"
report_id: 938
rtd_name: "NBU Policy Clients.rtd"
description: "NBU Policy Clients"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nSELECT \ns.hostname master_server,\npc.policy_id,\npc.policy_name, \np.is_active,\nstorage_unit,\nvp.volume_pool_name,\nREPLACE(aptStringConcat(DISTINCT pc.client_name),',','<br />') clients,\nREPLACE(aptStringConcat(DISTINCT pf.pathname),',','<br />') paths\nFROM apt_v_nbu_policy_client pc, apt_v_nbu_policy_file pf, apt_v_nbu_policy p, apt_v_server s,\napt_v_nbu_volume_pool vp\nWHERE \np.policy_id = pc.policy_id\nAND pc.policy_id = pf.policy_id\nAND p.server_id = s.server_id\nAND p.volume_pool_id = vp.volume_pool_id (+)\nGROUP BY s.hostname,\npc.policy_id,\npc.policy_name, \np.is_active,\nstorage_unit,\nvp.volume_pool_name\nORDER BY 2"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
