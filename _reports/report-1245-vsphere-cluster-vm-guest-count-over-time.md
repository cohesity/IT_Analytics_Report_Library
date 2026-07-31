---
title: "vSphere Cluster VM Guest Count over Time"
report_id: 1245
rtd_name: "vSphere Cluster VM Guest Count over Time.rtd"
description: "vSphere Cluster VM Guest Count over Time"
problem_statement: "For any given cluster in my environment I want to see the growth rate in number of active VM Guests and the number of ESX servers."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 10/23/2018\nWITH \nt1 AS (\nSELECT DISTINCT\nTRUNC(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) sort_order,\nTO_CHAR(TRUNC(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY') log_date,\nvs.virtual_system_id,\nTRUNC(AVG(nbr_of_active_vms)) nbr_of_active_vms\nFROM apt_v_vmw_cluster vc, apt_v_virtual_system vs, apt_v_virtual_system_log vsl\nWHERE \nvc.vmw_cluster_id = vs.vmw_cluster_id\nAND vs.virtual_system_id = vsl.virtual_system_id\nAND vsl.log_date BETWEEN ${startDate} AND ${endDate}\nAND vs.data_center_name||' - '||vc.cluster_name LIKE '${queryCombo1}'\nGROUP BY\nTRUNC(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),\nTO_CHAR(TRUNC(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY'),\nvs.virtual_system_id\n)\nSELECT\nsort_order,\nlog_date,\nCOUNT(virtual_system_id) nbr_virtual_systems,\nSUM(nbr_of_active_vms) nbr_of_active_vms\nFROM \nt1\nGROUP BY\nsort_order,\nlog_date\nORDER BY \nsort_order ASC"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
