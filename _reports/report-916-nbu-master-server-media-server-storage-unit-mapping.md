---
title: "NBU Master Server Media Server Storage Unit Mapping"
report_id: 916
rtd_name: "NBU Master Server Media Server Storage Unit Mapping.rtd"
description: "NBU Master Server Media Server Storage Unit Mapping"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "SELECT \ns.hostname master_server,\nREPLACE(aptStringConcat(DISTINCT tl.library_name),',','<br>') tape_libraries,\nREPLACE(aptStringConcat(DISTINCT m.media_server_name),',','<br>') media_servers,\nREPLACE(aptStringConcat(DISTINCT su.storage_unit_label),',','<br>') storage_units\nFROM apt_v_server s,apt_v_nbu_storage_unit su, apt_v_nbu_media_server m,apt_v_nbu_tape_library tl\nWHERE s.server_id in (${hosts})\nAND s.server_id = su.server_id\nAND su.storage_unit_id = m.storage_unit_id\nAND s.server_id = tl.server_id\nAND s.hostname = DECODE('${queryCombo1}',' ALL',s.hostname,'${queryCombo1}')\nGROUP BY s.hostname"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
