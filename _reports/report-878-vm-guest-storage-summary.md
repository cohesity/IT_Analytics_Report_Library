---
title: "VM Guest Storage Summary"
report_id: 878
rtd_name: "VM Guest Storage Summary.rtd"
description: "VM Guest Storage Summary"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 09/14/2011\nWITH t1 as (\nSELECT\npp.partition_id, \nvd.vm_guest_name,\nvd.virtual_system_id,\nvd.virtual_system_name,\nvd.host_id,\nvd.host_name guest_host,\npp.os,\nsum(vd.capacity_gb) cap_seen_by_host,\nsum(vd.capacity_gb) host_fs_capacity,\nsum(vd.used_space_gb) host_fs_used,\nsum(vd.free_space_gb) host_free_gb\nFROM apt_v_vmw_vmguest_disk vd, apt_v_vmw_partition_profile pp\nWHERE host_id IN (${hosts}) \nAND vd.partition_id = pp.partition_id\nGROUP BY \npp.partition_id,\nvd.vm_guest_name,\nvd.virtual_system_id,\nvd.virtual_system_name,\nvd.host_id,\nvd.host_name,\npp.os\n),\nrd AS (\nSELECT \nvd.partition_id,\nsum(pd.capacity_kb/1024/1024) rdisk_capacity_gb\nFROM apt_v_vmw_physical_disk pd, apt_v_vmw_virtual_disk vd\nWHERE vd.disk_type = 'RDISK'\nAND pd.canonical_name  = NVL(SUBSTR (vd.rdisk_lun_name, 1,INSTR (vd.rdisk_lun_name, ':', 1, 3) - 1),vd.rdisk_lun_name)\nGROUP BY vd.partition_id\n)\nSELECT \nt1.virtual_system_id,\nt1.virtual_system_name,\nt1.partition_id, \nt1.vm_guest_name,\nt1.host_id,\nt1.guest_host,\nCASE \nWHEN upper(t1.os) LIKE '%WINDOWS%' THEN 'Windows'\nWHEN upper(t1.os) LIKE '%LINUX%' THEN 'Linux'\nWHEN upper(t1.os) LIKE '%VMNIX-X86%' THEN 'ESX'\nWHEN upper(t1.os) LIKE '%AIX%' THEN 'AIX'\nWHEN upper(t1.os) LIKE '%SOLARIS%' THEN 'Solaris'\nELSE os\nEND os_shortname,\ncap_seen_by_host,\nhost_fs_capacity,\nhost_fs_used,\nhost_free_gb,\nrd.rdisk_capacity_gb raw_fs_capacity\nFROM t1, rd\nWHERE \nt1.partition_id = rd.partition_id (+)\nAND '${freeCombo1}' IN \n  CASE \n    WHEN '${freeCombo1}' NOT IN ('All') THEN\n      CASE\n        WHEN upper(t1.os) LIKE '%WINDOWS%' THEN 'Windows'\n        WHEN upper(t1.os) LIKE '%LINUX%' THEN 'Linux'\n        WHEN upper(t1.os) LIKE '%VMNIX-X86%' THEN 'ESX'\n        WHEN upper(t1.os) LIKE '%AIX%' THEN 'AIX'\n      END\n   ELSE 'All'\n END"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
