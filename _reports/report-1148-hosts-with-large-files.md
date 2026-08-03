---
title: "Hosts with Large Files"
report_id: 1148
rtd_name: "Hosts with Large Files.rtd"
description: "Hosts with Large Files"
problem_statement: "I want to see hosts that have the most large files on them so I can chargeback at a premium."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 06/02/2015\nWITH\nVAR AS (\nSELECT\nDECODE('${freeCombo1}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT \nh.host_name,\nDECODE(c.context_type,'S','Share','V','Volume',c.context_type) context_type,\nc.context_name,\nfs.nbr_of_files,\nfs.size_kb/div_by total_size,\nb.bucket_type,\nb.bucket_unit,\nb.start_number,\nb.end_number,\nb.description\nFROM apt_v_afa_file_size fs, aps_v_host h, apt_v_afa_bucket b, apt_v_afa_context c, var\nWHERE fs.host_id IN (${hosts})\nAND fs.host_id = h.host_id\nAND fs.bucket_id = b.bucket_id\nAND fs.context_id = c.context_id\nAND b.description LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}') \nAND fs.nbr_of_files > 0\nORDER BY 5 DESC"
has_explanation: false
products: [{"slug": "file-analytics-general", "name": "General"}]
categories: []
product_slugs: ["file-analytics-general"]
category_slugs: []
---
