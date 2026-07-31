---
title: "Array Port Intelligent Provisioning"
report_id: 1159
rtd_name: "Array Port Intelligent Provisioning.rtd"
description: "Array Port Intelligent Provisioning"
problem_statement: "I need to know which port I should use to assign my next group of hosts to.   It would be great if I could see in one report, the number of hosts that are already assigned to that port, the IO that has gone through that port in the past 7 days and the number of LUNs and amount of storage that is currently allocated to that port."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 01/20/2019\nWITH \nt1 AS (--Host and LUN counts\nSELECT\nap.storage_array_id,\nap.port_id,\nap.nickname,\nap.wwn,\nCOUNT(DISTINCT sp.host_id) hosts,\nCOUNT(DISTINCT sp.logical_unit_id) luns\nFROM\naps_v_array_port ap,  aps_v_storage_path sp\nWHERE \nap.storage_array_id IN (${arrays})\nAND ap.port_id = sp.array_port_id\nAND UPPER(ap.port_role) = 'TARGET'\nGROUP BY\nap.storage_array_id,\nap.port_id,\nap.nickname,\nap.wwn\n),\nt2 AS (--Get all the Distinct LUNs\nSELECT\nDISTINCT\nap.storage_array_id,\nap.port_id,\nsp.logical_unit_id,\nsp.total_capacity_gb\nFROM\naps_v_array_port ap,  aps_v_storage_path sp, t1\nWHERE \nap.storage_array_id IN (${arrays})\nAND ap.port_id = t1.port_id\nAND UPPER(ap.port_role) = 'TARGET'\nAND ap.port_id = sp.array_port_id\n),\nt3 AS (--Add Up the Capacity\nSELECT\nt2.storage_array_id,\nt2.port_id,\nSUM(t2.total_capacity_gb/1024) total_capacity_tb\nFROM t2\nGROUP BY\nt2.storage_array_id,\nt2.port_id\n),\nt4 AS (--Get the storage I/O\nSELECT\nl.port_id,\nMAX(l.kbytes_transferred/1024/1024) gb_transferred\nFROM aps_v_array_port_stats_log l, t1\nWHERE\nl.log_date >= sysdate -7\nAND l.port_id = t1.port_id\nGROUP BY\nl.port_id\n),\nt5 AS (\nSELECT\nt1.storage_array_id,\nsa.array_name,\nsa.vendor_name,\nt1.port_id,\nt1.nickname,\nt1.wwn,\nt1.hosts,\nDENSE_RANK() OVER (ORDER BY NVL(hosts,0) DESC) dr_hosts,\nt1.luns,\nDENSE_RANK() OVER (ORDER BY NVL(luns,0) DESC) dr_luns,\nt3.total_capacity_tb,\nDENSE_RANK() OVER (ORDER BY NVL(total_capacity_tb,0) DESC) dr_total_capacity_tb,\nNVL(t4.gb_transferred,0) gb_transferred,\nDENSE_RANK() OVER (ORDER BY NVL(gb_transferred,0) DESC) dr_gb_transferred\nFROM\naps_v_storage_array sa, t1, t3, t4\nWHERE\nt1.port_id = t3.port_id\nAND t1.port_id = t4.port_id (+)\nAND t1.storage_array_id = sa.storage_array_id\n)\nSELECT\nstorage_array_id,\narray_name,\nvendor_name,\nport_id,\nnickname,\nwwn,\ngb_transferred,\ndr_gb_transferred,\nCASE WHEN dr_gb_transferred = 1 THEN 'red' WHEN dr_gb_transferred = 2 THEN 'yellow' WHEN dr_gb_transferred = 3 THEN 'green' WHEN dr_gb_transferred = 4 THEN 'blue' ELSE 'white' END transferred_dot,\nhosts,\ndr_hosts,\nCASE WHEN dr_hosts = 1 THEN 'red' WHEN dr_hosts = 2 THEN 'yellow' WHEN dr_hosts = 3 THEN 'green'  WHEN dr_hosts = 4 THEN 'blue' ELSE 'white' END hosts_dot,\nluns,\ndr_luns,\nCASE WHEN dr_luns = 1 THEN 'red' WHEN dr_luns = 2 THEN 'yellow' WHEN dr_luns = 3 THEN 'green' WHEN dr_luns = 4 THEN 'blue' ELSE 'white' END luns_dot,\ntotal_capacity_tb,\ndr_total_capacity_tb,\nCASE WHEN dr_total_capacity_tb = 1 THEN 'red' WHEN dr_total_capacity_tb = 2 THEN 'yellow' WHEN dr_total_capacity_tb = 3 THEN 'green' WHEN dr_total_capacity_tb = 4 THEN 'blue' ELSE 'white' END capacity_dot,\n'Ranks '||\nCASE WHEN gb_transferred > 0 THEN dr_gb_transferred||DECODE(dr_gb_transferred,1,'st',2,'nd',3,'rd','th')||' in I/O, ' ELSE '' END ||\nCASE WHEN hosts > 0 THEN dr_hosts||DECODE(dr_hosts,1,'st',2,'nd',3,'rd','th')||' in #Hosts, ' ELSE '' END\n||dr_luns||DECODE(dr_luns,1,'st',2,'nd',3,'rd','th')||' in #LUNs, '\n||dr_total_capacity_tb||DECODE(dr_total_capacity_tb,1,'st',2,'nd',3,'rd','th')||' in Capacity'\nmessage\nFROM t5\nORDER BY gb_transferred DESC"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
