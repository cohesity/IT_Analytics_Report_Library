---
title: "TSM Node Occupancy"
report_id: 983
rtd_name: "TSM Node Occupancy.rtd"
description: "TSM Node Occupancy"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--tsm_node_occupancy_htm.sql\n--Select: Server Groups and Client Scope\n--Format: Table\nWITH \nf1 AS (\nSELECT n.node_id, n.client_id, f.filespace_id\n    FROM apt_v_tsm_node n,\n         apt_v_tsm_filespace f\n    WHERE n.client_id IN (${hosts})\n      AND n.node_id    = f.node_id\n),\nsp AS (\nSELECT f1.client_id, f1.node_id, SUM(p.stg_pool_phy_kbytes) sum_kbytes\n    FROM f1, apt_v_tsm_stgpool_contents p\n    WHERE f1.client_id    = p.client_id\n      AND f1.filespace_id = p.filespace_id\n    GROUP BY f1.client_id, f1.node_id\n),\nvo AS (\nSELECT f1.client_id, f1.node_id, COUNT(UNIQUE v.volume_id) count_volumes\n    FROM f1, apt_v_tsm_volume_contents v\n    WHERE f1.client_id    = v.client_id\n      AND f1.filespace_id = v.filespace_id\n      AND v.volume_type   = 'T'\n    GROUP BY f1.client_id, f1.node_id         \n)    \nSELECT i.instance_name, s.hostname tcp_name, n.node_name, \n       sp.sum_kbytes/1024/1024 sum_GB, vo.count_volumes\n    FROM sp, vo,\n         apt_v_tsm_node n,\n         apt_v_server s,\n         apt_v_server_instance i\n    WHERE sp.client_id  = s.server_id\n      AND sp.client_id  = vo.client_id\n      AND sp.node_id    = vo.node_id\n      AND sp.node_id    = n.node_id\n      AND n.server_instance_id = i.server_instance_id\n    ORDER BY Upper(i.instance_name), Upper(s.hostname), Upper(n.node_name)     "
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
