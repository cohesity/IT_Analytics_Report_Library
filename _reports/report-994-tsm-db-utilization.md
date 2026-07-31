---
title: "TSM DB Utilization"
report_id: 994
rtd_name: "TSM DB Utilization.rtd"
description: "TSM DB Utilization"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "WITH \ns1 AS (        \nSELECT i.server_instance_id, i.instance_name, d.avail_space_mbytes, d.capacity_mbytes,\n               (d.page_size_bytes/(1024*1024) * d.used_pages) / (d.capacity_mbytes+.001) * 100 pct_utilized\n    FROM apt_v_tsm_database d,  apt_v_server_instance i\n    WHERE d.server_id  IN (${hosts})\n      AND d.server_instance_id = i.server_instance_id\n    ),\ns2 AS (\nSELECT l.server_instance_id, MAX((l.page_size_bytes/(1024*1024) * l.used_pages) / (l.capacity_mbytes+.001) * 100) max_pct_used\n    FROM apt_v_tsm_database_log l, s1\n    WHERE l.server_instance_id = s1.server_instance_id\n      AND l.log_date BETWEEN ${startDate} AND ${endDate}\n    GROUP BY l.server_instance_id\n)\nSELECT s1.instance_name,\n   s1.avail_space_mbytes/1024 avail_space_gbytes,\n   s1.capacity_mbytes/1024 capacity_gbytes,\n   s1.pct_utilized,\n   s2.max_pct_used\n   FROM s1, s2\n   WHERE s1.server_instance_id = s2.server_instance_id"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
