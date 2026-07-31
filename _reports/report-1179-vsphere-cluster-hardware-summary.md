---
title: "vSphere Cluster Hardware Summary"
report_id: 1179
rtd_name: "vSphere Cluster Hardware Summary.rtd"
description: "vSphere Cluster Hardware Summary"
problem_statement: "I need to see what hardware is being used for each of my vSphere Clusters for capacity\r\n planning and chargeback and hardware refresh"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 05/23/2018\nWITH \ng1 AS (\nSELECT\nvc.vmw_cluster_id,\nCOUNT(DISTINCT vs.virtual_system_id) esx_host_count,\nCOUNT(DISTINCT p.partition_id) guest_count,\nSUM(p.memory_size_kb/1024/1024) vmemory_size,\nSUM(p.nbr_cpu) nbr_vcpu\nFROM apt_v_partition p, apt_v_virtual_system vs, apt_v_vmw_cluster vc\nWHERE \nvs.host_id IN (${hosts})\nAND vc.vmw_cluster_id = vs.vmw_cluster_id\nAND vs.virtual_system_id = p.virtual_system_id\nAND p.partition_type = 'VM'\nGROUP BY\nvc.vmw_cluster_id\n),\nt1 AS (\nSELECT\nvc.vmw_cluster_id,\nvc.cluster_name,\nvh.system_vendor||' '||vh.system_model||' '||cpu_description hardware,\nCOUNT(*) hardware_count,\nSUM((vc.total_memory_kb/1024/1024) / vc.nbr_of_hosts) total_memory_gb,\nSUM((vc.total_memory_kb/1024/1024) / vc.nbr_of_hosts) / MAX(vc.nbr_of_hosts) avg_memory_per_host,\nSUM(vc.nbr_of_cpu_cores  / vc.nbr_of_hosts) nbr_of_cpu_cores\nFROM apt_v_vmw_cluster vc,apt_v_virtual_system vs, apt_v_vmw_hardware vh\nWHERE \nvs.host_id IN (${hosts})\nAND vs.vmw_cluster_id = vc.vmw_cluster_id\nAND vs.virtual_system_id = vh.virtual_system_id\nGROUP BY\nvc.vmw_cluster_id,\nvc.cluster_name,\nvh.system_vendor||' '||vh.system_model||' '||cpu_description\n),\nt2 AS (\nSELECT\nt1.vmw_cluster_id,\nt1.cluster_name,\nREPLACE(aptStringConcat(DISTINCT t1.hardware),',','<br>') hardware,\nSUM(t1.hardware_count) hardware_count,\nSUM(t1.total_memory_gb) total_memory_gb,\nMAX(avg_memory_per_host) avg_memory_per_host,\nSUM(t1.nbr_of_cpu_cores) nbr_of_cpu_cores\nFROM t1\nGROUP BY\nvmw_cluster_id,\ncluster_name\n)\nSELECT\nt2.vmw_cluster_id,\nt2.cluster_name,\nt2.hardware,\nt2.hardware_count,\nt2.total_memory_gb,\nt2.avg_memory_per_host,\nt2.nbr_of_cpu_cores,\ng1.esx_host_count,\ng1.guest_count,\ng1.nbr_vcpu,\ng1.vmemory_size,\ng1.vmemory_size/t2.total_memory_gb*100 memory_pct,\ng1.vmemory_size/t2.total_memory_gb pct_memory\nFROM g1, t2\nWHERE t2.vmw_cluster_id = g1.vmw_cluster_id (+)\nORDER BY t2.cluster_name"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
