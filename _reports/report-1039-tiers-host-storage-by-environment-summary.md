---
title: "Tiers Host Storage by Environment Summary"
report_id: 1039
rtd_name: "Tiers Host Storage by Environment Summary.rtd"
description: "Tiers Host Storage by Environment Summary"
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
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nSELECT\nnvl(rtd.getServerAttributeValue(cl.host_id,'Environment'),'Unassigned') environment,\ncl.policy_name,\ncount(cl.host_id) nbr_of_hosts,\nsum(cl.total_gb/1024) total_size\nFROM aps_v_chargeback_log cl\nWHERE cl.host_id in (${hosts})\nGROUP BY \nnvl(rtd.getServerAttributeValue(cl.host_id,'Environment'),'Unassigned'),\ncl.policy_name"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
