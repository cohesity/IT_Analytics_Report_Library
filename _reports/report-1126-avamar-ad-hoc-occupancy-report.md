---
title: "Avamar Ad Hoc Occupancy Report"
report_id: 1126
rtd_name: "Avamar Ad Hoc Occupancy Report.rtd"
description: "Avamar Ad Hoc Occupancy Report"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 07/10/2012\nSELECT \nDECODE('${freeCombo1}',\n'Client',client_name,\n'Avamar Server',server_name,\n'Job Type',job_type_name) unit,\nSUM(modified_sent_kb)/1024/1024 total_unexpired_data,\nSUM(CASE WHEN expiration_date BETWEEN sysdate AND sysdate+30 THEN modified_sent_kb END)/1024/1024 less_than_30,\nSUM(CASE WHEN expiration_date BETWEEN sysdate+30 AND sysdate+90 THEN modified_sent_kb END)/1024/1024 bt_30_and_90,\nSUM(CASE WHEN expiration_date BETWEEN sysdate+90 AND sysdate+365.25 THEN modified_sent_kb END)/1024/1024 bt_90_and_1yr,\nSUM(CASE WHEN expiration_date BETWEEN sysdate+365.25 AND sysdate+1825 THEN modified_sent_kb END)/1024/1024 bt_1_and_5yrs,\nSUM(CASE WHEN expiration_date > sysdate+1825 THEN modified_sent_kb END)/1024/1024 over_5yrs\nFROM apt_v_avm_activities\nWHERE client_id IN (${hosts})\nAND expiration_date > sysdate\nAND DECODE('${freeCombo1}',\n'Client',client_name,\n'Avamar Server',server_name,\n'Job Type',job_type_name) IS NOT NULL\nGROUP BY \nDECODE('${freeCombo1}',\n'Client',client_name,\n'Avamar Server',server_name,\n'Job Type',job_type_name)\nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
