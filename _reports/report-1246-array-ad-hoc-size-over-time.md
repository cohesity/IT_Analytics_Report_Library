---
title: "Array Ad Hoc Size over Time"
report_id: 1246
rtd_name: "Array Ad Hoc Size over Time.rtd"
description: "Array Ad Hoc Size over Time"
problem_statement: "There are many metrics we store historically for each storage array.  I wan an easy way to plot any of those values."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 10/24/2018\nWITH \nVAR AS (\nSELECT\n'${freeCombo1}' unit,\nDECODE('${freeCombo1}','GB',1,'TB',1024,'PB',1024*1024) div_by\nFROM apt_v_dual\n),\nt1 AS (--get one entry per day per array\nSELECT \nTRUNC(log_date,DECODE('${freeCombo2}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) log_date,\nstorage_array_id,\nMAX(\nDECODE('${freeCombo3}',\n'Cache',Cache_GB,\n'Capacity',Capacity_GB,\n'Allocated',Allocated_GB,\n'Available',Available_GB,\n'Largest Free Space',Largest_Free_Space_GB,\n'Raw Capacity',Raw_Capacity_GB,\n'Raw Allocated',Raw_Allocated_GB,\n'Raw Available',Raw_Available_GB,\n'Virtual Capacity', Virtual_Capacity_GB,\n'Known Virtual Capacity',Known_Virtual_Capacity_GB,\n'License Capacity', License_Capacity_GB,\n'Usable Internal Capacity',Usable_Internal_Capacity_GB,\n'Usable External Capacity',Usable_External_Capacity_GB,\n'Virtualized Capacity',Virtualized_Capacity_GB,\n'Virtualized Capacity Thin',Virtualized_Capacity_Thin_GB,\n'Usable Used Capacity',Usable_Used_Capacity_GB,\n'Usable Free Capacity',Usable_Free_Capacity_GB,\n'LUN Capacity',LUN_Capacity_GB,\n'LUN Allocated',LUN_Allocated_GB,\n'LUN Unallocated',LUN_Unallocated_GB,\n'Thin Pool Capacity',Thin_Pool_Capacity_GB,\n'Thin Pool Allocated',Thin_Pool_Allocated_GB,\n'Thin Pool Available',Thin_Pool_Available_GB,\n'Thin Pool Subscribed',Thin_Pool_Subscribed_GB)\n) the_max_value,\nAVG(\nDECODE('${freeCombo3}',\n'Cache',Cache_GB,\n'Capacity',Capacity_GB,\n'Allocated',Allocated_GB,\n'Available',Available_GB,\n'Largest Free Space',Largest_Free_Space_GB,\n'Raw Capacity',Raw_Capacity_GB,\n'Raw Allocated',Raw_Allocated_GB,\n'Raw Available',Raw_Available_GB,\n'Virtual Capacity', Virtual_Capacity_GB,\n'Known Virtual Capacity',Known_Virtual_Capacity_GB,\n'License Capacity', License_Capacity_GB,\n'Usable Internal Capacity',Usable_Internal_Capacity_GB,\n'Usable External Capacity',Usable_External_Capacity_GB,\n'Virtualized Capacity',Virtualized_Capacity_GB,\n'Virtualized Capacity Thin',Virtualized_Capacity_Thin_GB,\n'Usable Used Capacity',Usable_Used_Capacity_GB,\n'Usable Free Capacity',Usable_Free_Capacity_GB,\n'LUN Capacity',LUN_Capacity_GB,\n'LUN Allocated',LUN_Allocated_GB,\n'LUN Unallocated',LUN_Unallocated_GB,\n'Thin Pool Capacity',Thin_Pool_Capacity_GB,\n'Thin Pool Allocated',Thin_Pool_Allocated_GB,\n'Thin Pool Available',Thin_Pool_Available_GB,\n'Thin Pool Subscribed',Thin_Pool_Subscribed_GB)\n) the_avg_value\nFROM aps_v_storage_array_log\nWHERE\nlog_date BETWEEN ${startDate} AND ${endDate}\nAND storage_array_id IN (${arrays})\nGROUP BY\nTRUNC(log_date,DECODE('${freeCombo2}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),\nstorage_array_id\n)\nSELECT\nlog_date,\nROUND(SUM(the_max_value/div_by),2) the_max_value,\nROUND(SUM(the_avg_value/div_by),2) the_avg_value\nFROM t1, var\nGROUP BY \nlog_date\nORDER BY 1"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
