---
title: "Host Database Instance Tablespace Capacity"
report_id: 1222
rtd_name: "Host Database Instance Tablespace Capacity.rtd"
description: "Host Database Instance Tablespace Capacity"
problem_statement: "I need to see the database instances and tablespaces on a given set of hosts for capacity planning, and ensuring that they are being protected by my backup team."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 05/11/2017\nWITH \nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays,\n${startDate} startDate,\nDECODE('${freeCombo1}',\n'GB',1,'TB',1024,'PB',(1024*1024)) div_by,\n'${freeCombo1}' the_unit \nFROM apt_v_dual\n)\nSELECT \nhost_id,host_name,\nDECODE(di.database_vendor,'O','Oracle','Other') vendor,\ndi.db_instance_name,\ndt.tablespace_name,\ndt.total_size_gb/div_by total_size,\n(dt.total_size_gb - dt.free_size_gb)/div_by used_size,\ndt.free_size_gb/div_by free_size\nFROM aps_v_database_instance di, aps_v_database_tablespace dt, var\nWHERE di.db_instance_id = dt.db_instance_id\nAND di.host_id IN (${hosts})"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
