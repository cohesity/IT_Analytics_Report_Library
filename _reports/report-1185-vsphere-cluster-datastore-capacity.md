---
title: "vSphere Cluster Datastore Capacity"
report_id: 1185
rtd_name: "vSphere Cluster Datastore Capacity.rtd"
description: "vSphere Cluster Datastore Capacity"
problem_statement: "Show me the capacity of my datastores across all of my clusters."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 06/20/2017\nWITH \nVAR AS (\nSELECT\n'${freeCombo1}' unit,\nDECODE('${freeCombo1}', 'GB',1024*1024,'TB',1024*1024*1024,'PB',(1024*1024*1024*1024)) div_by\nFROM apt_v_dual\n),\nd1 AS (--Datastore\nSELECT DISTINCT\nvc.vmw_cluster_id,\nvc.cluster_name,\nd.vmw_datastore_id,\nd.tot_capacity_kb/div_by tot_capacity,\nd.free_capacity_kb/div_by free_capacity\nFROM apt_v_vmw_cluster vc, apt_v_virtual_system vs, apt_v_vmw_datastore d, apt_v_vmw_map_vsys_dtstore dm, var\nWHERE \nvs.host_id IN (${hosts})\nAND vs.vmw_cluster_id = vc.vmw_cluster_id\nAND vs.virtual_system_id = dm.virtual_system_id\nAND dm.vmw_datastore_id = d.vmw_datastore_id\n)\nSELECT\nvmw_cluster_id,\ncluster_name,\nCOUNT(vmw_datastore_id) nbr_of_datastores,\nSUM(tot_capacity) tot_capacity,\nSUM(free_capacity) free_capacity,\nSUM(tot_capacity - free_capacity) used_capacity,\nSUM(free_capacity)/SUM(DECODE(tot_capacity,0,null,tot_capacity))*100 used_pct,\nSUM(free_capacity)/SUM(DECODE(tot_capacity,0,null,tot_capacity)) pct_used\nFROM d1\nGROUP BY \nvmw_cluster_id,\ncluster_name\nORDER BY 8 DESC"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
