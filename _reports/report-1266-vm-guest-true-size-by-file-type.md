---
title: "VM Guest True Size by File Type"
report_id: 1266
rtd_name: "VM Guest True Size by File Type.rtd"
description: "VM Guest True Size By File Type"
problem_statement: "I need to chargeback for the amount of storage a VM Guest is using however the amount if disk it's using is only part of what it is actually using.  There are log files and snapshots and other associated files that comprise it's true size.  I need a report that accounts for that."
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 02/13/2020\nWITH\nVAR AS (\nSELECT\nDECODE('${freeCombo1}', 'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual \n)\nSELECT\nvs.host_id AS virtual_system_host_id,\nvs.virtual_system_id,\nvs.virtual_system_name,\nvf.partition_id,\nvf.vm_id,\nvf.vm_name,\nvf.host_id AS vm_guest_host_id,\nvf.host_name AS vm_guest_host_name,\nSUM(vf.file_size/div_by) total_vm_size,\nSUM(DECODE(vf.file_type,'VmDisk',vf.file_size/div_by,0)) VmDisk,\nSUM(DECODE(vf.file_type,'VmSuspendState',vf.file_size/div_by,0)) VmSuspendState,\nSUM(DECODE(vf.file_type,'VmSwapFile',vf.file_size/div_by,0)) VmSwapFile,\n(SUM(DECODE(vf.file_type,'VmSnapshot',vf.file_size/div_by,0)) +\nSUM(DECODE(vf.file_type,'VmSnapshotMetaData',vf.file_size/div_by,0))) VmSnapshot,\nSUM(DECODE(vf.file_type,'FolderFile',vf.file_size/div_by,0)) FolderFile,\n(SUM(DECODE(vf.file_type,'VmConfigFile',vf.file_size/div_by,0)) +\nSUM(DECODE(vf.file_type,'VmConfigTeam',vf.file_size/div_by,0))) VmConfig,\nSUM(DECODE(vf.file_type,'VmLog',vf.file_size/div_by,0)) VmLog,\nSUM(DECODE(vf.file_type,'VmNvram',vf.file_size/div_by,0)) VmNvram,\nSUM(DECODE(vf.file_type,'Other',vf.file_size/div_by,0)) Other\nFROM \n  apt_v_virtual_system vs, apt_v_vmw_vmfile vf, var\nWHERE \n  vf.virtual_system_id = vs.virtual_system_id\n  AND vs.host_id IN (${hosts})\nGROUP BY\n  vs.host_id,\n  vs.virtual_system_id,\n  vs.virtual_system_name,\n  vf.partition_id,\n  vf.vm_id,\n  vf.vm_name,\n  vf.host_id,\n  vf.host_name"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
