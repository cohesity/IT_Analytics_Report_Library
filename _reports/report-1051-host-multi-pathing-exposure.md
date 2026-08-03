---
title: "Host Multi-Pathing Exposure"
report_id: 1051
rtd_name: "Host Multi Pathing Exposure.rtd"
description: "Host Multi Pathing Exposure"
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
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nWITH q1 as (\nSELECT distinct hs.HOST_ID,\n  hs.SOFTWARE_NAME,\n  hs.SOFTWARE_VERSION\nFROM aps_v_host_software hs\nWHERE host_id IN (${hosts})\nAND UPPER(software_type) like '%MULTI%'\n),\nq2 as (\nSELECT host_id,\naptStringConcat(software_name||' - ' ||software_version) mps\nFROM q1 \nGROUP by host_id,software_name\n),\n\nq3 as (\nSELECT host_id,COUNT(distinct host_port_wwn) nbr_of_paths\nFROM aps_v_storage_path\nWHERE host_id IN (${hosts})\nAND host_id is not NULL\nGROUP by host_id\n)\nSELECT \nCASE WHEN nbr_of_paths > 1 AND mps IS NOT NULL THEN 'green'\nELSE 'red'\nEND status,\nq3.host_id,s.hostname,nbr_of_paths,mps\nFROM q2,q3,apt_v_server s\nWHERE q3.host_id=q2.host_id(+)\nand q3.host_id=s.server_id"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
