---
title: "Failed or No Backup in 3 days"
report_id: 907
rtd_name: "Failed or No Backup in 3 days.rtd"
description: "Failed or No Backup in 3 days"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--failed or no backup for last 3 days\nWITH \nt_3 as (\n  SELECT client_id, min(summary_status) min_status\n  FROM apt_v_job\n  WHERE \n  start_date BETWEEN TRUNC(SYSDATE-3) AND TRUNC(SYSDATE-2)\n  AND client_id IN (${hosts})\n  GROUP BY client_id\n),\nt_2 as (\n  SELECT client_id, min(summary_status) min_status\n  FROM apt_v_job\n  WHERE \n  start_date BETWEEN TRUNC(SYSDATE-2) AND TRUNC(SYSDATE-1)\n  AND client_id IN (${hosts})\n  GROUP BY client_id\n),\nt_1 as (\n  SELECT client_id, min(summary_status) min_status\n  FROM apt_v_job\n  WHERE \n  start_date BETWEEN TRUNC(SYSDATE-1) AND SYSDATE\n  AND client_id IN (${hosts})\n  GROUP BY client_id\n),\nts as (\n  SELECT s.server_id,s.display_name, \n  DECODE(t_3.min_status,2,'1',null,'0') three_days_ago,\n  DECODE(t_2.min_status,2,'1',null,'0') two_days_ago,\n  DECODE(t_1.min_status,2,'1',null,'0') Last_Night\n  FROM  t_3, t_2, t_1, apt_v_server s\n  WHERE s.server_id IN (${hosts})\n  AND s.server_id=t_3.client_id (+)\n  AND s.server_id=t_2.client_id (+) \n  AND s.server_id=t_1.client_id (+)\n)\nSELECT \n'<a href=\"#\" onclick=\"drilldown(''../report/drillDown.mvc?systemName=displayServerDetail&amp;serverId='||ts.server_id||''', this, '''' );\">'||ts.display_name||'</a>' Client,\n  DECODE ((ts.three_days_ago+ts.two_days_ago+ts.Last_Night),\n           0,'No backup for 3 days',\n           2,'2 Failed backups in last 3 days',\n           3,'Failed backups 3 days in a row',\n           'No backup at all'\n         ) status\n  FROM ts\n  WHERE (ts.three_days_ago+ts.two_days_ago+ts.Last_Night) IS NOT NULL\n  ORDER BY Upper(ts.display_name)"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
