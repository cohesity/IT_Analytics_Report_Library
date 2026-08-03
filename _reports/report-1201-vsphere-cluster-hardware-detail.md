---
title: "vSphere Cluster Hardware Detail"
report_id: 1201
rtd_name: "vSphere Cluster Hardware Detail.rtd"
description: "vSphere Cluster Hardware Detail"
problem_statement: ""
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 05/08/2018\nSELECT\nvc.vmw_cluster_id,\nvc.cluster_name,\nvh.virtual_system_id,\nvh.virtual_system_name,\nvh.system_vendor||' '||vh.system_model||' '||vh.cpu_description hardware,\nDECODE(vh.cpu_vendor,'amd','AMD','intel','Intel',vh.cpu_vendor) cpu_vendor,\nvh.cpu_speed_mhz/1000 cpu_ghz,\nvh.cpu_package_num,\nvc.nbr_of_cpu_cores/vc.nbr_of_hosts nbr_cpu_cores,\n(vc.total_memory_kb/1024/1024)/vc.nbr_of_hosts total_memory\nFROM apt_v_vmw_cluster vc,apt_v_virtual_system vs, apt_v_vmw_hardware vh\nWHERE vs.host_id IN (${hosts})\nAND vs.vmw_cluster_id = vc.vmw_cluster_id\nAND vs.virtual_system_id = vh.virtual_system_id"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
