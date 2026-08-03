---
title: "Avamar Open File Error Summary"
report_id: 1113
rtd_name: "Avamar Open File Error Summary.rtd"
description: "Avamar Open File Error Summary"
problem_statement: "Show where I may be exposed due to files being skipped because they were held open during the backup process."
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/19/2013\nSELECT\ns.server_id,\ns.hostname,\nclient_id,\nclient_name,\neffective_path,\nSUM(nbr_files_skipped) nbr_files_skipped,\nMAX(job_id) job_id,\nMAX(recorded_date) last_backup\nFROM apt_v_avm_activities j,apt_v_server s\nWHERE\nj.server_id = s.server_id\nAND recorded_date BETWEEN ${startDate} AND ${endDate}\nAND nbr_files_skipped > 0\nAND client_id IN (${hosts})\nGROUP BY \ns.server_id,\ns.hostname,\nclient_id,\nclient_name,\neffective_path\nORDER BY 2,4,8"
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
