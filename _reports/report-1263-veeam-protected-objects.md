---
title: "Veeam Protected Objects"
report_id: 1263
rtd_name: "Veeam Protected Objects.rtd"
description: "Veeam Protected Objects"
problem_statement: ""
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "SELECT\ns.server_type_name,\npo.server_id,\t\npo.server_name,\npo.server_instance_id,\t\npo.server_instance_name,\npo.object_type,\t\npo.policy_id,\t\npo.policy_name,\t\npo.object_name,\t\npo.protected_object_identifier,\npo.host_id,\npo.host_name,\t\npo.object_path_name,\t\npo.is_excluded,\t\npo.creation_date,\t\npo.last_updated\nFROM apt_v_dp_protected_object po, apt_v_server s\nWHERE \npo.server_id IN (${hosts})\nAND po.server_id = s.server_id\nAND UPPER(s.server_type_name) LIKE '%VEEAM%'\nAND po.last_updated BETWEEN ${startDate} AND ${endDate}"
has_explanation: false
products: [{"slug": "backup-manager-veeam", "name": "Veeam"}]
categories: []
product_slugs: ["backup-manager-veeam"]
category_slugs: []
---
