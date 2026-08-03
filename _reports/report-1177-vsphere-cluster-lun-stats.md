---
title: "vSphere Cluster LUN stats"
report_id: 1177
rtd_name: "VM Cluster LUN Stats.rtd"
description: "Shows the performance Metrics of LUNS in VM Clusters"
problem_statement: "I have several VM clusters attached to various storage arrays.  I need to know which clusters are using them most IO on the LUNs that are provisioned to them."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 11/07/2016\nWITH \nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays, \n${startDate} startDate, \n'${freeCombo1}' unit,\nDECODE('${freeCombo1}', 'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual \n),\nt1 AS (\nSELECT\nvc.vmw_cluster_id,\nvc.cluster_name,\nvs.virtual_system_id,\nsp.logical_unit_id\nFROM apt_v_vmw_cluster vc, apt_v_virtual_system vs, aps_v_storage_path sp\nWHERE vc.vmw_cluster_id = vs.vmw_cluster_id\nAND vs.host_id = sp.host_id\nAND vs.host_id IN (${hosts})\n),\nt2 AS ( --Unique LUNs per Cluster\nSELECT\nDISTINCT\nvmw_cluster_id,\ncluster_name,\nlogical_unit_id\nFROM t1\n),\nl1 AS (--Get all the LUNs\nSELECT\nt2.vmw_cluster_id,\nt2.cluster_name,\nt2.logical_unit_id,\nlu.storage_array_id,\nlu.array_name,\nlu.logical_unit_name,\nlu.total_capacity_kb\nFROM t2, aps_v_logical_unit lu\nWHERE t2.logical_unit_id = lu.logical_unit_id\n),\np1 AS (--Get the performance stats\nSELECT\nt2.logical_unit_id,\nSUM(pl.kbytes_read) read,\nSUM(pl.kbytes_written) written,\nSUM(pl.total_io) total_io,\nAVG(pl.read_io_response_time) avg_read_io_response_time,\nMAX(pl.read_io_response_time) max_read_io_response_time,\nAVG(pl.write_io_response_time) avg_write_io_response_time,\nMAX(pl.write_io_response_time) max_write_io_response_time\nFROM t2, aps_v_lun_perform_log pl\nWHERE t2.logical_unit_id = pl.logical_unit_id\nAND log_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\nt2.logical_unit_id\n)\nSELECT\nl1.vmw_cluster_id,\nl1.cluster_name,\nl1.storage_array_id,\nl1.array_name,\nCOUNT(l1.logical_unit_id) nbr_of_luns,\naptStringConcat(DISTINCT l1.logical_unit_id) logical_unit_ids,\nSUM(l1.total_capacity_kb/div_by) lun_capacity,\nSUM(p1.read/div_by) read,\nSUM(p1.written/div_by) written,\nSUM(p1.total_io/div_by) total_io,\nAVG(p1.avg_read_io_response_time) avg_read_io_response_time,\nMAX(p1.max_read_io_response_time) max_read_io_response_time,\nAVG(p1.avg_write_io_response_time) avg_write_io_response_time,\nMAX(p1.max_write_io_response_time) max_write_io_response_time\nFROM l1, p1, var\nWHERE l1.logical_unit_id = p1.logical_unit_id(+) \nGROUP BY\nl1.vmw_cluster_id,\nl1.cluster_name,\nl1.storage_array_id,\nl1.array_name\n--Uncomment to show only ones with perf data collection\n--HAVING SUM(p1.total_io/div_by) > 0\nORDER BY l1.cluster_name"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
