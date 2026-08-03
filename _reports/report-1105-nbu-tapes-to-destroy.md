---
title: "NBU Tapes to Destroy"
report_id: 1105
rtd_name: "NBU Tapes to Destroy.rtd"
description: "NBU Tapes to Destroy"
problem_statement: "To avoid legal hold, I need to destroy backups based on our corporate policy."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 05/15/2013\nSELECT \njtm.tape_media_id,\ntm.bar_code,\nCOUNT(DISTINCT jtm.job_id) images,\nCOUNT(DISTINCT jtm.client_id) clients,\nMIN(jtm.expiration_date) newest_image,\nMAX(jtm.expiration_date) oldest_image,\nSUM(jtm.kilobytes/1024/1024) size_gb\nFROM apt_v_nbu_job_tape_media jtm, apt_v_nbu_tape_media tm\nWHERE \njtm.client_id IN (${hosts})\nAND jtm.controlling_server_id IN (${hosts})\nAND jtm.expiration_date BETWEEN ${startDate} AND ${endDate}\nAND jtm.tape_media_id = tm.tape_media_id\nGROUP BY\njtm.tape_media_id,tm.bar_code"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
