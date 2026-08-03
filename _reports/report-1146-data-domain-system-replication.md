---
title: "Data Domain System Replication"
report_id: 1146
rtd_name: "Data Domain System Replication.rtd"
description: "Data Domain System Replication"
problem_statement: "I need a report which lists all the Data Domain replication jobs that are performed so I can be sure that my data is protected at multiple sites."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 08/06/2015\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo1}',\n'KB',1,'MB',(1024),'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT\nr.host_id,\nh.host_name,\nr.context_number,\t\nr.connection_time,\n--r.source_directory,\nr.dest_directory,\nr.pre_comp_sent_kb/div_by pre_comp_sent,\nr.pre_comp_remaining_kb/div_by pre_comp_remaining,\nr.post_comp_sent_kb/div_by post_comp_sent,\nr.post_comp_received_kb/div_by post_comp_received,\nr.replication_throttle/1000 throttle_mbsec,\nr.synced_of_time,\nTO_DATE(r.synced_of_time,'MON DD, YYYY HH:MIAM') synced_of_date,\nr.state,\nr.error,\nr.last_updated-TO_DATE(r.synced_of_time,'MON DD, YYYY HH:MIAM') sync_lag,\nr.last_updated\nFROM apt_v_ddm_system_replication r, aps_v_host h, var\nWHERE r.last_updated BETWEEN ${startDate} AND ${endDate}\nAND r.host_id = h.host_id\nAND r.host_id IN (${hosts})"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}, {"slug": "backup-manager-emc-data-domain", "name": "EMC Data Domain"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors", "backup-manager-emc-data-domain"]
category_slugs: []
---
