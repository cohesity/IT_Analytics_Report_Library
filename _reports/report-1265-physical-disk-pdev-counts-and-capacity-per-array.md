---
title: "Physical Disk (PDEV) Counts and Capacity per Array"
report_id: 1265
rtd_name: "Physical Disk (PDEV) Counts and Capacity per Array.rtd"
description: "Physical Disk (PDEV) Counts and Capacity per Array"
problem_statement: ""
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 01/20/2019\nWITH \nVAR AS (\nSELECT \n'${freeCombo1}' unit,\nDECODE('${freeCombo1}', 'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by\nFROM apt_v_dual\n)\nSELECT\nsa.storage_array_id,\nsa.array_name,\nsa.array_family,\nSUM(DECODE(pd.disk_type,'FC',1,0)) fc_count,\nSUM(DECODE(pd.disk_type,'FC',pd.capacity_kb/div_by,0)) fc_capacity,\nSUM(DECODE(pd.disk_type,'EFD',1,0)) efd_count,\nSUM(DECODE(pd.disk_type,'EFD',pd.capacity_kb/div_by,0)) efd_capacity,\nSUM(DECODE(pd.disk_type,'LUN',1,0)) lun_count,\nSUM(DECODE(pd.disk_type,'LUN',pd.capacity_kb/div_by,0)) lun_capacity,\nSUM(DECODE(pd.disk_type,'SAS',1,0)) sas_count,\nSUM(DECODE(pd.disk_type,'SAS',pd.capacity_kb/div_by,0)) sas_capacity,\nSUM(DECODE(pd.disk_type,'SSD',1,0)) ssd_count,\nSUM(DECODE(pd.disk_type,'SSD',pd.capacity_kb/div_by,0)) ssd_capacity,\nSUM(DECODE(pd.disk_type,'BSAS',1,0)) bsas_count,\nSUM(DECODE(pd.disk_type,'BSAS',pd.capacity_kb/div_by,0)) bsas_capacity,\nSUM(DECODE(pd.disk_type,'SATA',1,0)) sata_count,\nSUM(DECODE(pd.disk_type,'SATA',pd.capacity_kb/div_by,0)) sata_capacity,\nSUM(DECODE(pd.disk_type,'NL SAS',1,0)) nlsas_count,\nSUM(DECODE(pd.disk_type,'NL SAS',pd.capacity_kb/div_by,0)) nlsas_capacity,\nSUM(DECODE(pd.disk_type,'Unknown',1,0)) unknown_count,\nSUM(DECODE(pd.disk_type,'Unknown',pd.capacity_kb/div_by,0)) unknown_capacity,\nSUM(DECODE(pd.disk_type,'SATA SSD',1,0)) satassd_count,\nSUM(DECODE(pd.disk_type,'SATA SSD',pd.capacity_kb/div_by,0)) satassd_capacity\nFROM aps_v_pdev pd, aps_v_storage_array sa, var\nWHERE \nsa.storage_array_id IN (${arrays})\nAND sa.storage_array_id = pd.storage_array_id\nGROUP BY \nsa.storage_array_id,\nsa.array_name,\nsa.array_family"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
