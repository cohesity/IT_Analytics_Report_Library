---
title: "Data Domain System Info by Site Detail"
report_id: 1141
rtd_name: "Data Domain System Info by Site Detail.rtd"
description: "Data Domain System Info by Site Detail"
problem_statement: "I need an overview of all of my Data Domains so I can compare software versions and capacity usage across all of my sites."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 07/09/2015\nWITH \nvar AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays,\nDECODE('${freeCombo1}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\nt1 AS (\nSELECT\ns.server_id,\ns.hostname,\ns.location,\ns.ip_address,\nde.model_number,\nds.serial_number,\ns.os_version,\nSUM(dfs.filesystem_size_kb/div_by) filesystem_size,\nSUM(dfs.pre_comp_size_kb/div_by) pre_comp_size,\nSUM(dfs.filesystem_used_kb/div_by) filesystem_used,\nSUM(dfs.filesystem_cleanable_kb/div_by) filesystem_cleanable\nFROM apt_v_server s, apt_v_ddm_system ds, apt_v_ddm_enclosure de, apt_v_ddm_file_system dfs, var\nWHERE ds.host_id IN (${hosts}) \nAND ds.host_id = s.server_id\nAND ds.host_id = de.host_id\nAND ds.host_id = dfs.host_id\nAND de.enclosure_id = 1\nGROUP BY\ns.server_id,\ns.hostname,\ns.location,\ns.ip_address,\nde.model_number,\nds.serial_number,\ns.os_version\n)\nSELECT\nserver_id,\nhostname,\nlocation,\nip_address,\nmodel_number,\nserial_number,\nREPLACE(os_version,'Data Domain OS','') os_version,\nfilesystem_size,\npre_comp_size,\nfilesystem_used,\nROUND((pre_comp_size/filesystem_used),0) comp_ratio,\nfilesystem_cleanable,\n(filesystem_size-filesystem_used)*(pre_comp_size/filesystem_used) est_available,\n(filesystem_used/filesystem_size)*100 pct_used,\n(filesystem_used/filesystem_size) used_pct\nFROM t1\nORDER BY 2"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}, {"slug": "backup-manager-emc-data-domain", "name": "EMC Data Domain"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors", "backup-manager-emc-data-domain"]
category_slugs: []
---
