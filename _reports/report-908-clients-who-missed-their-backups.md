---
title: "Clients Who Missed Their Backups"
report_id: 908
rtd_name: "Clients Who Missed Their Backups.rtd"
description: "Clients Who Missed Their Backups"
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
sql_query: "-- Of the jobs run within the specified time frame, display the clients\n-- that are in the same server group, who did not have a job present.\n-- In addition to displaying the client, also display the last tbackup they had, and what was\n-- it's status.\nWITH \nt1 as (--All clients in the server group\nSELECT DISTINCT server_id\nFROM apt_v_server\nWHERE server_id IN (${hosts})\n),\nt2 as (--Clients which had backups in the last x days\nSELECT \nDISTINCT client_id\nFROM apt_v_job  j\nWHERE  j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\n)\nSELECT t1.server_id, s.hostname, lcj.job_id, lcj.finish_date,\nDECODE(lcj.summary_status,0,'blue',1,'yellow',2,'red') summary_status\nFROM t1, apt_v_server s, apt_v_last_client_job lcj\nWHERE t1.server_id NOT IN (SELECT client_id FROM t2)\nAND t1.server_id = s.server_id\nAND t1.server_id = lcj.client_id (+)"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
