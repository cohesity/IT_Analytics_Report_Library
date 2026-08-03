---
title: "Overall Client Status Detail"
report_id: 909
rtd_name: "Overall Client Status Detail.rtd"
description: "Overall Client Status Detail"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 09/24/20111\n--All Failed, All Success, All Partial, All Mixed Success & Failure\nWITH t1 as (\nSELECT '<font color=red>All Jobs Failed</font>' status,\nj.server_name as \"Backup Server\",\nj.client_name as \"Client\",\nj.JOB_TYPE_NAME as \"Job Type\",\nmin(start_date) as \"First Job\",\nmax(start_date) as \"Last Job\",\ncount(j.job_id) as \"Nbr. of Jobs\",\ntrunc(sum(kilobytes)/1024/1024) as \"size(GB)\",\nclient_id, job_type\nFROM apt_v_job j\nWHERE finish_date BETWEEN ${startDate} AND ${endDate}\nAND client_id IN (${hosts} )\nAND j.summary_status IS NOT NULL\nGROUP BY j.server_name,j.client_name, j.job_type_name, client_id, job_type\nHAVING min(summary_status) >1\nUNION\nSELECT '<font color=green>Mixed Success & Failures</font>' status,\nj.server_name as \"Backup Server\",\nj.client_name as \"Client\",\nj.JOB_TYPE_NAME as \"Job Type\",\nmin(start_date) as \"First Job\",\nmax(start_date) as \"Last Job\",\ncount(j.job_id) as \"Nbr. of Jobs\",\ntrunc(sum(kilobytes)/1024/1024) as \"size(GB)\",\nclient_id, job_type\nFROM apt_v_job j\nWHERE finish_date BETWEEN ${startDate} AND ${endDate}\nAND client_id IN (${hosts} )\nAND j.summary_status IS NOT NULL\nGROUP BY j.server_name,j.client_name, j.job_type_name, client_id, job_type\nHAVING max(summary_status) > 1\nAND min(summary_status) = 0\nUNION\nSELECT '<font color=orange>All Jobs Partial</font>' status,\nj.server_name as \"Backup Server\",\nj.client_name as \"Client\",\nj.JOB_TYPE_NAME as \"Job Type\",\nmin(start_date) as \"First Job\",\nmax(start_date) as \"Last Job\",\ncount(j.job_id) as \"Nbr. of Jobs\",\ntrunc(sum(kilobytes)/1024/1024) as \"size(GB)\",\nclient_id, job_type\nFROM apt_v_job j\nWHERE finish_date BETWEEN ${startDate} AND ${endDate}\nAND client_id IN (${hosts} )\nAND j.summary_status IS NOT NULL\nGROUP BY j.server_name,j.client_name, j.job_type_name, client_id, job_type\nHAVING min(summary_status) =1\nAND max(summary_status) =1\nUNION\nSELECT '<font color=blue>All Jobs Successful</font>' status,\nj.server_name as \"Backup Server\",\nj.client_name as \"Client\",\nj.JOB_TYPE_NAME as \"Job Type\",\nmin(start_date) as \"First Job\",\nmax(start_date) as \"Last Job\",\ncount(j.job_id) as \"Nbr. of Jobs\",\ntrunc(sum(kilobytes)/1024/1024) as \"size(GB)\",\nclient_id, job_type\nFROM apt_v_job j\nWHERE finish_date BETWEEN ${startDate} AND ${endDate}\nAND client_id IN (${hosts} )\nAND j.summary_status IS NOT NULL\nGROUP BY j.server_name,j.client_name, j.job_type_name, client_id, job_type\nHAVING max(summary_status) =0\n)\nSELECT * FROM t1 \nWHERE status LIKE DECODE('${freeCombo1}','All','%','%${freeCombo1}%')"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
