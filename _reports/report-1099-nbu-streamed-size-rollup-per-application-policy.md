---
title: "NBU Streamed Size Rollup per Application Policy"
report_id: 1099
rtd_name: "NBU Streamed Size Rollup per Application Policy.rtd"
description: "Using the policy name as the \"Application\" roll up how much data was backed up (streamed data)."
problem_statement: "My application names are the first characters in my policy name up to the first underscore.  Aggregate all job data by that so I can see how much was written."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last updated: 03/26/2013\n--This report assumes the first characters in the policy name to be the Application\n--The first characters up to the first underscore _ or the first 4 characters if there is no _\nWITH\nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays,\n${startDate} startDate,\nDECODE('${freeCombo1}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by\nFROM dual\n),\nt1 AS (\nSELECT\nNVL(SUBSTR(j.policy_name,1,INSTR(j.policy_name,'_',1)-1),SUBSTR(j.policy_name,1,4)) application,\nj.policy_id,\nj.policy_name,\nCOUNT(j.job_id) job_count,\nSUM(j.kilobytes/var.div_by) job_size,\nREPLACE(aptStringConcat(DISTINCT pf.pathname),',','<br/>') pathname\nFROM apt_v_nbu_job_detail j,apt_v_nbu_policy_file pf, var\nWHERE j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.job_type <> 105\nAND j.policy_id = pf.policy_id\nGROUP BY\nSUBSTR(j.policy_name,1,INSTR(j.policy_name,'_',1)-1),\nj.policy_id,\nj.policy_name\nORDER BY 1,3\n)\nSELECT\napplication application_sort,\napplication,\npolicy_id,\npolicy_name,\njob_count,\njob_size,\npathname\nFROM t1\nUNION\nSELECT\napplication application_sort,\n'<B> Total - '||application||'</b>' application,\nNULL policy_id,\nNULL policy_name,\nSUM(job_count) job_count,\nSUM(job_size) job_size,\nNULL pathname\nFROM t1\nGROUP BY application,'<B> Total - '||application||'</b>'\nUNION\nSELECT\n'zzzzzz' application_sort,\n'<B> Grand Total' application,\nNULL policy_id,\nNULL policy_name,\nSUM(job_count) job_count,\nSUM(job_size) job_size,\nNULL pathname\nFROM t1\nGROUP BY 'zzzzzz','<B> Grand Total'\nORDER BY 1,4"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
