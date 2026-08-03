---
title: "NBU Restore Job Age"
report_id: 943
rtd_name: "NBU Restore Job Age.rtd"
description: "NBU Restore Job Age"
problem_statement: ""
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/12/2012\nSELECT\nrbj.backup_job_id,\nbj.client_host_name backup_client,\nbj.start_date backup_start_date,\nrbj.restore_job_id,\nrj.client_host_name restore_client,\nrj.start_date restore_start_date,\nrj.target_client_id,\ntc.hostname target_client,\nrj.kilobytes/1024/1024 restore_size_gb,\nround(rj.start_date-bj.start_date) restore_age,\n(SELECT REPLACE(aptStringConcat(jf.pathname),',','<br>') FROM apt_v_nbu_job_file jf WHERE jf.job_id=rj.job_id) files_restored\nFROM apt_v_nbu_job bj, apt_v_nbu_job rj, apt_v_nbu_restore_backup_job rbj, apt_v_server tc\nWHERE bj.job_id = rbj.backup_job_id\nAND rj.job_id = rbj.restore_job_id\nAND rj.client_id IN (${hosts})\nAND rj.start_date BETWEEN ${startDate} AND ${endDate}\nAND rj.target_client_id = tc.server_id"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
