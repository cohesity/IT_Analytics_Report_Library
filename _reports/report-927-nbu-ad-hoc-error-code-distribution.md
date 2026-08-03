---
title: "NBU Ad Hoc Error Code Distribution"
report_id: 927
rtd_name: "NBU Ad Hoc Error Code Distribution.rtd"
description: "NBU Ad Hoc Error Code Distribution"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "WITH t1 as (\nSELECT\nsummary_status,\nvendor_status status,\nserver_id,\nnvl(DECODE('${freeCombo1}',\n'Client',client_host_name,\n'Master Server',master_host_name,\n'Media Server',media_host_name,\n'Storage Unit',storage_unit_label,\n'Policy',policy_name,\n'Policy Type',policy_type_name,\n'Job Type',job_type_name,\n'Schedule',schedule_name,\n'Schedule Type',schedule_type_name),'None') unit,  \ncount(job_id) job_count\nFROM apt_v_nbu_job_detail\nWHERE client_id IN (${hosts})\nAND finish_date BETWEEN ${startDate}  AND ${endDate}\nAND vendor_status is not null\nGROUP BY\nsummary_status, \nvendor_status,\nserver_id,\nnvl(DECODE('${freeCombo1}',\n'Client',client_host_name,\n'Master Server',master_host_name,\n'Media Server',media_host_name,\n'Storage Unit',storage_unit_label,\n'Policy',policy_name,\n'Policy Type',policy_type_name,\n'Job Type',job_type_name,\n'Schedule',schedule_name,\n'Schedule Type',schedule_type_name),'None')\n)\nSELECT\nto_char(${startDate},'MM/DD/YYYY') start_date_char,\nto_char(${startDate},'HH24') start_hour_char,\nto_char(${endDate},'MM/DD/YYYY') finish_date_char,\nto_char(${endDate},'HH24') finish_hour_char,\nt1.server_id,\nt1.summary_status,\nt1.status,\nt1.unit,\nt1.job_count  \nFROM t1"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
