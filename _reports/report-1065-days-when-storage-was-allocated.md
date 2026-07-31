---
title: "Days When Storage was Allocated"
report_id: 1065
rtd_name: "Days When Storage was Allocated.rtd"
description: "Days When Storage was Allocated"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 02/15/2012\nWITH \nt1 AS (\nSELECT\nto_number(to_char(log_date,'YYYYMMDD')) the_date,\nstorage_array_id,\nmax(allocated_gb) allocated_gb\nFROM aps_v_storage_array_log\nWHERE log_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY to_number(to_char(log_date,'YYYYMMDD')),\nstorage_array_id\n),\nt2 AS (\nSELECT\nto_number(to_char(log_date,'YYYYMMDD')) the_date,\nstorage_array_id,\nmax(allocated_gb) allocated_gb\nFROM aps_v_storage_array_log\nWHERE log_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY to_number(to_char(log_date,'YYYYMMDD')),\nstorage_array_id\n)\nSELECT \nt1.storage_array_id,\nsa.array_name,\nto_date(t2.the_date,'YYYYMMDD') the_date,\nt1.allocated_gb t1_allocated_gb,\nt2.allocated_gb t2_allocated_gb,\nt2.allocated_gb-t1.allocated_gb alloc_de_alloc\nFROM t1,t2, aps_v_storage_array sa\nWHERE t1.storage_array_id = sa.storage_array_id\nAND t1.storage_array_id=t2.storage_array_id \nAND t1.the_date = t2.the_date+1\nAND t2.allocated_gb-t1.allocated_gb <> 0\nORDER BY 3"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
