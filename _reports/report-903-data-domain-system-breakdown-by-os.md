---
title: "Data Domain System Breakdown by OS"
report_id: 903
rtd_name: "Data Domain System Breakdown by OS.rtd"
description: "Data Domain System Breakdown by OS"
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
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nSELECT os_version, count(ds.host_id) host_count\nFROM apt_v_server s, apt_v_ddm_system ds, apt_v_ddm_enclosure de\nWHERE s.server_id = ds.host_id\nAND ds.host_id = de.host_id\nAND s.server_id IN (${hosts})\nAND de.model_number LIKE DECODE('${queryCombo1}','All','%','${queryCombo1}')\nGROUP BY os_version"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}, {"slug": "backup-manager-emc-data-domain", "name": "EMC Data Domain"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors", "backup-manager-emc-data-domain"]
category_slugs: []
---
