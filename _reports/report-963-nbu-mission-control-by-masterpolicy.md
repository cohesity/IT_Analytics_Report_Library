---
title: "NBU Mission Control by MasterPolicy"
report_id: 963
rtd_name: "NBU Mission Control by Master - Policy.rtd"
description: "NBU Mission Control by Master - Policy"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nSELECT to_char(start_date,'Mon DD') run_date, master_host_name||' - '||policy_name master_server_policy,  \nDECODE(max(summary_status),0,'<img src=\"../skins/aptare/statusBlue.gif\">&nbsp;</img>' ,1,'<img src=\"../skins/aptare/statusYellow.gif\">&nbsp;</img>',2,'<img src=\"../skins/aptare/statusRed.gif\">&nbsp;</img>'\n)\nstatus \nFROM apt_v_nbu_job_detail\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND client_id in (${hosts})\nAND policy_name IS NOT NULL\nAND start_date IS NOT NULL\nGROUP BY to_char(start_date,'Mon DD'), master_host_name||' - '||policy_name"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
