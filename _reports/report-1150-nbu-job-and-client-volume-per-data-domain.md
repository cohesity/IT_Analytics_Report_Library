---
title: "NBU Job and Client Volume per Data Domain"
report_id: 1150
rtd_name: "NBU Job and Client Volume per DataDomain.rtd"
description: "NBU Job and Client Volume per Data Domain"
problem_statement: "I need to be able to see how much data is data is being written to each of my Data Domain storage units and how much of that is expiring, so I can manage the usage by ensuring no long term data is being saved."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 08/06/2015\nWITH \nvar AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays,\nDECODE('${freeCombo1}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\nddsu AS (\nSELECT\nnsu.server_id,\nnsu.master_internal master_server,\nnsu.storage_unit_id,\nnsu.storage_unit_label,\nnsu.disk_pool_id,\nndv.disk_volume_id,\nndv.disk_volume_name,\nddsu.host_id data_domain_host_id,\ndds.hostname data_domain_name\nFROM \napt_v_nbu_storage_unit nsu,\napt_v_nbu_disk_volume ndv, \napt_v_ddm_logical_strg_unit ddsu,\napt_v_server dds\nWHERE nsu.disk_pool_id = ndv.disk_pool_id\nAND ndv.external_link_id = ddsu.logical_storage_unit_id\nAND ddsu.host_id = dds.server_id\nAND nsu.server_id IN (${hosts})\nAND nsu.master_internal LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\n)\nSELECT\nd.server_id,\nd.master_server,\nd.storage_unit_id,\nd.storage_unit_label,\nd.data_domain_host_id,\nd.data_domain_name,\nCOUNT(DISTINCT client_id) clients,\nSUM(kilobytes/div_by) total_written,\nROUND(SUM(CASE WHEN expiration_date BETWEEN sysdate AND sysdate+30 THEN kilobytes END /div_by),2) less_than_30,\nROUND(SUM(CASE WHEN expiration_date BETWEEN sysdate+30 AND sysdate+60 THEN kilobytes END /div_by),2) bt_30_and_90,\nROUND(SUM(CASE WHEN expiration_date BETWEEN sysdate+60 AND sysdate+90 THEN kilobytes END /div_by),2) bt_60_and_90,\nROUND(SUM(CASE WHEN expiration_date > sysdate+90 THEN kilobytes END /div_by),2) over_90,\nROUND(SUM(CASE WHEN expiration_date < sysdate THEN kilobytes END/div_by),2) expired\nFROM ddsu d, apt_v_nbu_job j, var\nWHERE\nj.client_id IN (${hosts})\nAND j.server_id = d.server_id\nAND j.storage_unit_id = d.storage_unit_id\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND expiration_date IS NOT NULL\nGROUP BY \nd.server_id,\nd.master_server,\nd.storage_unit_id,\nd.storage_unit_label,\nd.data_domain_host_id,\nd.data_domain_name"
has_explanation: false
products: [{"slug": "backup-manager-emc-data-domain", "name": "EMC Data Domain"}, {"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-emc-data-domain", "backup-manager-veritas-netbackup"]
category_slugs: []
---
