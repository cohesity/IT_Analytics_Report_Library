---
title: "Veeam Backup Repository Report"
report_id: 1262
rtd_name: "Veeam Backup Repository Report.rtd"
description: "Veeam Backup Repository Report"
problem_statement: ""
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 12/13/2018\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo1}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT \n(CASE \nWHEN r.parent_storage_resource_id IS NULL THEN r.storage_resource_id \nELSE r.parent_storage_resource_id \nEND) AS srId, \nr.server_name, \nr.storage_resource_type,\n(CASE \nWHEN r.parent_storage_resource_name IS NULL THEN r.storage_resource_name \nELSE r.parent_storage_resource_name \nEND) AS Name,\n(CASE \nWHEN r.parent_storage_resource_name IS NOT NULL THEN r.storage_resource_name \nEND) AS Extent, r.description, \nr.total_capacity_kb/div_by AS  total_capacity, \nr.used_capacity_kb/div_by AS  used_capacity\nFROM apt_v_dp_storage_resource r, var\nWHERE r.product_type = 200700 \nAND r.storage_resource_type <> 'Server' \nAND r.server_id IN (${hosts})"
has_explanation: false
products: [{"slug": "backup-manager-veeam", "name": "Veeam"}]
categories: []
product_slugs: ["backup-manager-veeam"]
category_slugs: []
---
