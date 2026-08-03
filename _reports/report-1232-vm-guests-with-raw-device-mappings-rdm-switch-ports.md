---
title: "VM Guests with Raw Device Mappings (RDM) & Switch Ports"
report_id: 1232
rtd_name: "VM Guests with Raw Device Mappings (RDM) & Switch Ports.rtd"
description: "VM Guests with Raw Device Mappings (RDM) & Switch Ports"
problem_statement: "I need to know which VM Guests have RDM's in case we need to migrate them to another array.  Additionally I need to know which SAN switches they are attached to in case there is  problem, I can quickly identify where to look and what will be impacted."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/13/2018\nWITH\nVAR AS (\nSELECT\nDECODE('${freeCombo1}', 'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual \n),\nsw AS (\nSELECT\nt.target_storage_array_id storage_array_id,\naptStringConcat(DISTINCT sw.switch_id) switch_ids,\naptStringConcat(DISTINCT sw.element_name) switches\nFROM aps_v_swi_topology t, aps_v_swi_switch sw\nWHERE\nt.source_switch_id = sw.switch_id \nAND t.target_storage_array_id IS NOT NULL\nGROUP BY t.target_storage_array_id\n)\nSELECT\nvf.host_id,vf.host_name,\nvd.partition_id, vd.partition_name,\nvd.virtual_system_id, vd.virtual_system_name,\nvd.vmw_datastore_id, vd.datastore_name,\nvd.disk_label,\nvd.rdisk_lun_name,\nvd.is_thin_provisioned,\nvd.file_path,\nvd.file_name,\nvf.file_size/div_by file_size,\nvf.storage_array_id, vf.array_name,\nvf.logical_unit_id, vf.logical_unit_name,\nsw.switch_ids,\nREPLACE(sw.switches,',','<br>') switches\nFROM apt_v_vmw_virtual_disk vd, apt_v_vmw_vmfile vf, sw, var\nWHERE\nvd.disk_type = 'RDISK'\nAND vd.vmw_datastore_id = vf.vmw_datastore_id\nAND vd.partition_id = vf.partition_id\nAND vd.file_name = vf.file_name\nAND vf.file_type = 'VmDisk'\nAND vf.storage_array_id = sw.storage_array_id (+)\nAND vf.partition_id IN (${vmGuests})"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}, {"slug": "fabric-manager-general", "name": "General"}, {"slug": "fabric-manager-brocade", "name": "Brocade"}, {"slug": "fabric-manager-cisco", "name": "Cisco"}]
categories: []
product_slugs: ["virtualization-vmware", "fabric-manager-general", "fabric-manager-brocade", "fabric-manager-cisco"]
category_slugs: []
---
