---
title: "NBU Dup Job Summary by Media Server Tape Drive"
report_id: 949
rtd_name: "NBU Dup Job Summary by Media Server Tape Drive.rtd"
description: "NBU Dup Job Summary by Media Server Tape Drive"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nSELECT\nndj.media_host_name, ndj.drive_id, ntd.drive_name tape_drive,count(ndj.job_id) job_count,\navg(ndj.mbytes_sec) avg_mbytes_sec,\nsum(ndj.kilobytes/1024/1024) size_gb \nFROM apt_v_nbu_duplication_job ndj, apt_v_nbu_tape_drive ntd\nWHERE ndj.start_date BETWEEN ${startDate} AND ${endDate}\nAND ndj.server_id IN (${hosts})\nAND ndj.drive_id = ntd.drive_id(+)\nAND ndj.is_active = 'N'\nGROUP BY \nndj.drive_id,\nntd.drive_name,\nndj.media_host_name\nORDER BY 1,2"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
