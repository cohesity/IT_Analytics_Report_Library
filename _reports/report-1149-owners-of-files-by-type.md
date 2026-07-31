---
title: "Owners of files by Type"
report_id: 1149
rtd_name: "Owners of files by Type.rtd"
description: "Owners of Files by Type  Searchable by Share & Owner"
problem_statement: "For \"Shame Back\" purposes, I need to pull a report which shows how much space is taken up by non-business related personal files like music and movie files."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 08/07/2015\nWITH\nVAR AS (\nSELECT\nDECODE('${freeCombo1}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT \nh.host_name,\nDECODE(x.context_type,'S','Share','V','Volume',x.context_type) context_type,\nx.context_name,\noc.owner,\nc.category_name,\nc.file_extension,\noc.total_files,\noc.total_size_kb/div_by total_size\nFROM apt_v_afa_owner_category oc, apt_v_afa_category c, aps_v_host h, apt_v_afa_context x,var\nWHERE oc.afa_category_id = c.afa_category_id\nAND oc.host_id IN (${hosts})\nAND oc.host_id = h.host_id\nAND oc.total_files > 0\nAND oc.context_id = x.context_id\nAND REGEXP_LIKE(x.context_name,'${freeText1}')\nAND REGEXP_LIKE(oc.owner,'${freeText2}')\nAND c.category_name LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\nORDER BY oc.total_size_kb DESC"
has_explanation: false
products: [{"slug": "file-analytics-general", "name": "General"}]
categories: []
product_slugs: ["file-analytics-general"]
category_slugs: []
---
