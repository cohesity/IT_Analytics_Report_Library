---
title: "TSM Active Sessions Summary"
report_id: 1007
rtd_name: "TSM Active Sessions Summary.rtd"
description: "TSM Active Sessions Summary"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 10/03/2011\nWITH\nvar AS (\nSELECT \nDECODE('${freeCombo1}','30min',.5,'45min',.75,'1hr',1,'2hrs',2,'3hrs',3,'4hrs',4) avg_wait_threshold,\nDECODE('${freeCombo2}','1hr',1,'2hrs',2,'4hrs',4,'6hrs',6,'8hrs',8,'10hrs',10,'12hrs',12) max_wait_threshold,\n'${freeCombo1}' avg_wait_threshold_name,\n'${freeCombo2}' max_wait_threshold_name\nFROM apt_v_dual\n), \nq1 AS (\nSELECT\ntn.instance_name,\ncount(ts.node_session_id) session_count,\nsum(ts.kilobytes_recd/1024/1024) gb_rx,\nsum(ts.kilobytes_send/1024/1024) gb_tx,\navg(ts.wait_time_secs) avg_wait_time_secs,\nmax(ts.wait_time_secs) max_wait_time_secs,\navg(ts.wait_time_secs/60/60) avg_wait_time_hrs,\nmax(ts.wait_time_secs/60/60) max_wait_time_hrs,\ncount(ts.node_id) node_count\nFROM apt_v_tsm_session ts, apt_v_tsm_node tn, apt_v_server_instance si\nWHERE ts.start_date BETWEEN ${startDate} AND ${endDate}\nAND ts.node_id = tn.node_id (+)\nAND ts.is_active = 'Y'\nAND ts.job_id IS NULL\nAND tn.server_instance_id = si.server_instance_id\nAND si.server_id IN (${hosts})\nGROUP BY tn.instance_name\n)\nSELECT\nround(avg_wait_time_hrs,2) avg_wait_time_hrs,\nCASE WHEN avg_wait_time_hrs >= var.avg_wait_threshold THEN 'red'\nELSE 'green'\nEND avg_wait_dot,\nround(max_wait_time_hrs,2) max_wait_time_hrs,\nCASE WHEN max_wait_time_hrs >= var.max_wait_threshold THEN 'red'\nELSE 'green'\nEND max_wait_dot,\ninstance_name,\nsession_count,\ngb_rx,\ngb_tx,\nrtd.secsToHoursMinSecs(avg_wait_time_secs) avg_wait_time,\nrtd.secsToHoursMinSecs(max_wait_time_secs) max_wait_time,\nnode_count,\nvar.avg_wait_threshold_name,\nvar.max_wait_threshold_name\nFROM q1,var\nORDER BY 3 DESC"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
