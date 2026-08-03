---
title: "Data Domain System Snapshots"
report_id: 1147
rtd_name: "Data Domain System Snapshots.rtd"
description: "Data Domain System Snapshots"
problem_statement: "I need a report which lists all the Data Domain snapshots so I can be sure that my data is protected."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 08/06/2015\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo1}',\n'KB',1,'MB',(1024),'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT\nss.host_id,\nh.host_name,\nss.snapshot_name,\nss.pre_compression_kb/div_by pre_compression,\nss.created_date,\nss.retain_until_date,\nss.snapshot_status,\nss.mtree_name,\nss.last_updated\nFROM apt_v_ddm_system_snapshot ss, aps_v_host h, var\nWHERE ss.created_date BETWEEN ${startDate} AND ${endDate}\nAND ss.host_id = h.host_id\nAND ss.host_id IN (${hosts})"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}, {"slug": "backup-manager-emc-data-domain", "name": "EMC Data Domain"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors", "backup-manager-emc-data-domain"]
category_slugs: []
---
