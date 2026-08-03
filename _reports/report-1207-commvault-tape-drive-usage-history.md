---
title: "CommVault Tape Drive Usage History"
report_id: 1207
rtd_name: "CommVault Tape Drive Usage History.rtd"
description: "CommVault Tape Drive Usage History"
problem_statement: "Show me the activity of my tape drives"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 06/14/2018\nSELECT\nTO_CHAR(TRUNC(tdl.poll_time,'MI'),'MM/DD hh:mi') the_date,\ntdl.drive_name,\nDECODE(tdl.tape_media_id,null,'white','blue') in_use_dot,\ntdl.media_name\nFROM apt_v_tape_drive_log tdl, apt_v_tape_drive td\nWHERE \ntdl.drive_id = td.drive_id\nAND tdl.poll_time BETWEEN ${startDate} AND ${endDate}\nAND td.controlling_server_id IN (${hosts})\nORDER BY tdl.drive_name, tdl.poll_time"
has_explanation: false
products: [{"slug": "backup-manager-commvault", "name": "CommVault"}]
categories: []
product_slugs: ["backup-manager-commvault"]
category_slugs: []
---
