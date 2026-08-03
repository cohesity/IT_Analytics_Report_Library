---
title: "NBU Images to Destroy"
report_id: 1106
rtd_name: "NBU Images to Destroy.rtd"
description: "NBU Images to Destroy"
problem_statement: "I need to know which backups I need to destroy based on our company's compliance policy."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 05/14/2013\nSELECT \nj.job_id,\nj.master_host_name,\nj.client_host_name,\nj.policy_id, j.policy_name,\nj.backup_id,\nj.start_date,\nj.expiration_date,\nj.expiration_date - j.start_date age,\ntm.tape_media_id,\ntm.bar_code\nFROM apt_v_nbu_job_detail j,apt_v_nbu_job_tape_media jtm, apt_v_nbu_tape_media tm\nWHERE j.client_id IN (${hosts})\nAND jtm.client_id IN (${hosts})\nAND jtm.controlling_server_id IN (${hosts})\nAND j.job_id = jtm.job_id\nAND jtm.tape_media_id = tm.tape_media_id\nAND j.expiration_date BETWEEN ${startDate} AND ${endDate}\nAND jtm.expiration_date BETWEEN ${startDate} AND ${endDate}\nAND j.backup_id IS NOT NULL"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
