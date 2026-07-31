---
title: "NBU Policy Audit - Schedule Changes"
report_id: 946
rtd_name: "NBU Policy Audit - Schedule Changes.rtd"
description: "NBU Policy Audit - Schedule Changes"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 11/04/2012\n--NOTE: These require the purchase of the NBU Policy Audit Module license in order to work.\nSELECT \nlog_date,\nserver_id, server_name,\npolicy_id, policy_name,\nschedule_id, schedule_name,\nschedule_change change\nFROM\nTABLE(nbu_rtd.listScheduleChanges(${startDate}, ${endDate}, ${spHosts},NULL,${serverGroups},1)) s"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
