---
title: "Host Allocated Storage Per Array Includes Allocated Unknown Summary per Host"
report_id: 1115
rtd_name: "Host Allocated Storage Per Array Includes Allocated Unknown Summary per Host.rtd"
description: "Host Allocated Storage Per Array Includes Allocated Unknown Summary per Host"
problem_statement: "I need a billing feed that:\r\n1. Won't double count for clustered hosts\r\n2. Will Identify an ESX server or not\r\n3. Has the ability to show Allocated but Un-Used LUNs so my totals will match\r\n4. If the LUN can't map to a host, show me the WWN of it was last attached to so I can track it down."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/19/2013\nWITH \nVAR AS (\nSELECT\nDECODE('${freeCombo1}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by\nFROM apt_v_dual\n),\nt1 AS (--Get all the LUNs that are host sees but pick only 1 host if clustered\nSELECT sp.logical_unit_id, \nMIN(sp.host_id) a_host_id,\nCOUNT(DISTINCT sp.host_id) related_host_ids,\naptStringConcat(DISTINCT h.host_name) related_host_names\nFROM aps_v_storage_path sp, aps_v_host h\nWHERE sp.host_id IN (${hosts})\nAND sp.host_id = h.host_id (+)\nGROUP BY sp.logical_unit_id\n),\nvs AS (--Fetch all VM ESX Servers\nSELECT \nhost_id,\nvirtual_system_id\nFROM apt_v_virtual_system\nWHERE host_id IN (${hosts})\n),\nt2 AS (\nSELECT \nt1.a_host_id,\nLOWER(h.host_name) host_name,\nDECODE(vs.host_id,NULL,'N','Y') is_esx,\nt1.related_host_ids,\nlu.storage_array_id,\nlu.array_name,\nlu.logical_unit_id lun_id,\nlu.logical_unit_name lun_name,\nlu.total_capacity_kb/div_by lun_capacity,\nt1.related_host_names related_host_names\nFROM t1, aps_v_host h, aps_v_logical_unit lu,  aps_v_storage_array_attribute aa,vs, var\nWHERE t1.a_host_id = h.host_id\nAND t1.logical_unit_id = lu.logical_unit_id\nAND t1.a_host_id = vs.host_id (+)\nAND lu.storage_array_id = aa.storage_array_id\nUNION\nSELECT\nhost_id,\n'Array WWN '||sp.array_port_wwn||' - Host WWN '||sp.host_port_wwn||'Unknown' host_name,\n'N' is_esx,\n0 related_host_ids,\nlu.storage_array_id,\nlu.array_name,\nlu.logical_unit_id lun,\nlu.logical_unit_name lun_name,\nlu.total_capacity_kb/div_by lun_capacity,\nNULL related_host_names\nFROM aps_v_logical_unit lu, aps_v_storage_array sa,  \naps_v_storage_path sp, var\nWHERE lu.storage_array_id = sa.storage_array_id\nAND lu.logical_unit_id NOT IN (SELECT t1.logical_unit_id FROM t1)\nAND lu.status LIKE 'allocated%'\nAND lu.logical_unit_id = sp.logical_unit_id (+)\nORDER BY \n2,6\n)\nSELECT\nto_char(sysdate,'MM/DD/YYYY') run_date,\na_host_id,\nhost_name,\nis_esx,\nstorage_array_id,\narray_name,\nCOUNT(lun_id) luns,\nSUM(lun_capacity) lun_capacity,\nrelated_host_names\nFROM t2\nWHERE host_name NOT LIKE DECODE('${freeCombo2}','Yes','ZZZZZZZZ','No','%Unknown')\nGROUP BY\na_host_id,\nhost_name,\nis_esx,\nstorage_array_id,\narray_name,\nrelated_host_names\nORDER BY 2,5"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
