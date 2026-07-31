---
title: "NBU Ad Hoc Occupancy Report"
report_id: 1189
rtd_name: "NBU Ad Hoc Occupancy Report.rtd"
description: "NBU Ad Hoc Occupancy Report"
problem_statement: "Analyze how much data is being retained so you can adjust your retention periods to be in line with your compliance policies"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 02/07/2018\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo2}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT \nDECODE('${freeCombo1}',\n'Client',client_host_name,\n'Master Server',master_host_name,\n'Media Server',media_host_name,\n'Storage Unit',storage_unit_label,\n'Policy',policy_name,\n'Policy Type',policy_type_name,\n'Job Type',job_type_name,\n'Schedule',schedule_name,\n'Schedule Type',schedule_type_name,\n'Try Count',try_count) unit,\nSUM(kilobytes/div_by) total_unexpired_data,\nSUM(CASE WHEN expiration_date BETWEEN sysdate AND sysdate+30 THEN kilobytes/div_by END) less_than_30,\nSUM(CASE WHEN expiration_date BETWEEN sysdate+30 AND sysdate+90 THEN kilobytes/div_by END) bt_30_and_90,\nSUM(CASE WHEN expiration_date BETWEEN sysdate+90 AND sysdate+365.25 THEN kilobytes/div_by END) bt_90_and_1yr,\nSUM(CASE WHEN expiration_date BETWEEN sysdate+365.25 AND sysdate+1825 THEN kilobytes/div_by END) bt_1_and_5yrs,\nSUM(CASE WHEN expiration_date > sysdate+1825 THEN kilobytes/div_by END) over_5yrs\nFROM apt_v_nbu_job_detail, var\nWHERE client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nAND expiration_date > sysdate\nAND DECODE('${freeCombo1}',\n'Client',client_host_name,\n'Master Server',master_host_name,\n'Media Server',media_host_name,\n'Storage Unit',storage_unit_label,\n'Policy',policy_name,\n'Policy Type',policy_type_name,\n'Job Type',job_type_name,\n'Schedule',schedule_name,\n'Schedule Type',schedule_type_name,\n'Try Count',try_count) IS NOT NULL\nGROUP BY DECODE('${freeCombo1}',\n'Client',client_host_name,\n'Master Server',master_host_name,\n'Media Server',media_host_name,\n'Storage Unit',storage_unit_label,\n'Policy',policy_name,\n'Policy Type',policy_type_name,\n'Job Type',job_type_name,\n'Schedule',schedule_name,\n'Schedule Type',schedule_type_name,\n'Try Count',try_count)\nORDER BY 7,6,5,4,3,2,1 DESC"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
