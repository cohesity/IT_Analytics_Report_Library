---
title: "NBU Daily Full and Incrementals by Client - Policy"
report_id: 959
rtd_name: "NBU Daily Full and Incrementals by Client - Policy.rtd"
description: "NBU Daily Full and Incrementals by Client - Policy"
problem_statement: ""
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated, 10/30/2015\n--NOTE: Requires Drilldown Report, NBU Daily Full and Incrementals.D\nWITH \nt1 AS (\nSELECT to_char(start_date,'MM/DD/YY') the_date,\nclient_host_name||' - '||policy_name client_policy, \nSUM(DECODE(job_type,'102',1)) incr_job_count,\nSUM(DECODE(job_type,101,1)) full_job_count,\nROUND(SUM(DECODE(job_type,102,kilobytes/1024/1024)),2) incr_job_size,\nROUND(SUM(DECODE(job_type,101,kilobytes/1024/1024)),2) full_job_size\nFROM apt_v_nbu_job_detail\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND client_id IN (${hosts})\nAND job_type IN (101,102)\nAND summary_status IN (0,1)\nGROUP BY to_char(start_date,'MM/DD/YY'), client_host_name||' - '||policy_name\n)\nSELECT\nthe_date,\nclient_policy,\n  NVL2(full_job_size,'<table width=100% border=0 cellspacing=0 cellpadding=0><td style=background-color:#CCCCFF align=left>'||full_job_count||' Full '||full_job_size||' GB </td></table>',null)||NVL2(incr_job_size,'<table width=100% border=0 cellspacing=0 cellpadding=0><td style=background-color:#CCFFFF align=left>'||incr_job_count||' Incr '||incr_job_size||' GB</td></table>',null) job_type_size\nFROM t1\nORDER BY 1,2"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
