---
title: "NBU Mission Control by Policy"
report_id: 920
rtd_name: "NBU Mission Control by Policy.rtd"
description: "NBU Mission Control by Policy"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/10/2011\nSELECT to_char(start_date,'MM/DD') run_date, policy_name policy,  \nDECODE(min(summary_status),0,'green' ,1,'yellow',2,'red'\n)\nstatus \nFROM apt_v_nbu_job_detail\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND client_id in (${hosts})\nAND policy_name IS NOT NULL\nAND start_date IS NOT NULL\nGROUP BY to_char(start_date,'MM/DD'), policy_name\nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
