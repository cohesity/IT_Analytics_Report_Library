---
title: "Client Failures in X Days"
report_id: 1103
rtd_name: "Clients Failures in X Days.rtd"
description: "Client Failures in X Days"
problem_statement: "Are my clients failing on a daily basis?"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 01/11/2018\nWITH \nc1 AS (\nSELECT \nDISTINCT server_id client_id, hostname\nFROM apt_v_server\nWHERE server_id IN (${hosts})\n),\nj1 AS (\nSELECT\nclient_id,\nMAX(lcj.job_id) last_job_id,\nMAX(lcj.finish_date) last_backup\nFROM apt_v_last_client_job lcj\nWHERE server_id IN (${hosts})\nGROUP BY client_id\n),\nj2 AS (\nSELECT\nc1.hostname client,\nlast_job_id,\nNVL(to_char(last_backup,'MM/DD/YYYY'),'Never') last_backup, \nNVL((sysdate - last_backup),99999) days_since_last\nFROM j1, c1\nWHERE\nc1.client_id = j1.client_id (+)\n)\nSELECT \nclient,\nlast_backup,\nlast_job_id,\ndays_since_last\nFROM j2\nWHERE days_since_last >=\nDECODE('${freeCombo1}',\n'in at least 3 Days',3,\n'in at least 7 Days',7,\n'in at least 14 Days',14,\n'in at least 30 Days',30,\n'in at least 60 Days',60,\n'Ever',99999\n)\nORDER BY\ndays_since_last"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
