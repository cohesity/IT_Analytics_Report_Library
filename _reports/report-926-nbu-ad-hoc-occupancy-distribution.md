---
title: "NBU Ad Hoc Occupancy Distribution"
report_id: 926
rtd_name: "NBU Ad Hoc Occupancy Distribution.rtd"
description: "NBU Ad Hoc Occupancy Distribution"
problem_statement: "I need to see which clients and policies have data that has long term retention to be sure that valuable resources are only used by critical systems and those under regulatory compliance."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/02/2015\nSELECT /*+ NO_MERGE */\nDECODE('${freeCombo1}',\n'Client',client_host_name,\n'Master Server',master_host_name,\n'Media Server',media_host_name,\n'Storage Unit',storage_unit_label,\n'Policy',policy_name,\n'Policy Type',policy_type_name,\n'Job Type',job_type_name,\n'Schedule',schedule_name,\n'Schedule Type',schedule_type_name) metric,\nSUM(kilobytes)/1024/1024/1024 total_unexpired_data,\nROUND(SUM(CASE WHEN expiration_date BETWEEN sysdate AND sysdate+30 THEN kilobytes END)/1024/1024/1024,2) less_than_30,\nROUND(SUM(CASE WHEN expiration_date BETWEEN sysdate+30 AND sysdate+90 THEN kilobytes END)/1024/1024/1024,2) bt_30_and_90,\nSUM(CASE WHEN expiration_date BETWEEN sysdate+90 AND sysdate+365.25 THEN kilobytes END)/1024/1024/1024 bt_90_and_1yr,\nROUND(SUM(CASE WHEN expiration_date BETWEEN sysdate+365.25 AND sysdate+1825 THEN kilobytes END)/1024/1024/1024,2) bt_1_and_5yrs,\nROUND(SUM(CASE WHEN expiration_date > sysdate+1825 THEN kilobytes END)/1024/1024/1024,2) over_5yrs\nFROM apt_v_nbu_job_detail\nWHERE client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nAND expiration_date > sysdate\nAND DECODE('${freeCombo1}',\n'Client',client_host_name,\n'Master Server',master_host_name,\n'Media Server',media_host_name,\n'Storage Unit',storage_unit_label,\n'Policy',policy_name,\n'Policy Type',policy_type_name,\n'Job Type',job_type_name,\n'Schedule',schedule_name,\n'Schedule Type',schedule_type_name) IS NOT NULL\nGROUP BY DECODE('${freeCombo1}',\n'Client',client_host_name,\n'Master Server',master_host_name,\n'Media Server',media_host_name,\n'Storage Unit',storage_unit_label,\n'Policy',policy_name,\n'Policy Type',policy_type_name,\n'Job Type',job_type_name,\n'Schedule',schedule_name,\n'Schedule Type',schedule_type_name)\nORDER BY 2 DESC"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
