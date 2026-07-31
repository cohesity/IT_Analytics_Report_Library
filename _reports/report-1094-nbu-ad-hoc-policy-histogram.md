---
title: "NBU Ad Hoc Policy Histogram"
report_id: 1094
rtd_name: "NBU Ad Hoc Policy Histogram.rtd"
description: "Provides a visual representation of what policies were running"
problem_statement: "Are all my policies running at the same time?\r\nShould I stagger the start times to improve performance?"
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last modified: 04/29/2013\nWITH \npol AS ( \nSELECT  \nj.policy_id,\nCOUNT(DISTINCT client_id) clients,\nMIN(start_date) min_start,\nMAX(finish_date) max_finish,\nSUM(kilobytes/1024/1024) total_size_gb\nFROM apt_v_nbu_job j\nWHERE j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.finish_date IS NOT NULL\nAND j.finish_date > j.start_date\nAND j.kilobytes > 1024\nAND j.summary_status <= 1\nGROUP BY j.policy_id\n), \nap AS (\nSELECT policy_id, the_date, min_start, max_finish, total_size_gb\nFROM pol, (SELECT the_date FROM TABLE(CAST(rtd.APTlistOfDates(${startDate}, ${endDate}, 10) AS dateListType))) d\n), \njobs AS (\nSELECT ap.policy_id, ap.the_date, \nCOUNT(job_id) jobs,\nCOUNT(DISTINCT client_id) clients,\nROUND(SUM(j.kilobytes/1024/1024),2) size_gb\nFROM ap, apt_v_nbu_job j\nWHERE ap.policy_id = j.policy_id\nAND j.client_id IN (${hosts})\nAND j.start_date <= (ap.the_date + 3599/86400)\nAND j.finish_date >= ap.the_date\nAND j.finish_date IS NOT NULL\nAND j.finish_date > j.start_date\nAND j.kilobytes > 1024\nAND j.summary_status <= 1\nGROUP BY ap.policy_id, ap.the_date\n),\nt1 AS ( \nSELECT ap.the_date, np.policy_name,\nap.min_start, ap.max_finish, ap.total_size_gb,\n--Number of jobs running at the time (number will go down as they complete)\nNVL2(jobs,'<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><td NOWRAP bgcolor=\"#CCCCFF\" align=left>'||jobs||DECODE(jobs,1,' Job',' Jobs')||'</td></table>',null) jobs,\n--Number of clients doing backups at that time (number will go down as they complete)\nNVL2(clients,'<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><td NOWRAP bgcolor=\"#CCCCFF\" align=left>'||clients||DECODE(clients,1,' Client',' Clients')||'</td></table>',null) clients,\n--Amount of total data set was processing at that time (number will go down as clients complete)\nNVL2(size_gb,'<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><td NOWRAP bgcolor=\"#CCCCFF\" align=left>'||size_gb||' GB</td></table>',null) size_gb,\njobs the_jobs,\nclients the_clients,\nsize_gb the_size\nFROM ap, jobs, apt_v_nbu_policy np\nWHERE ap.policy_id = jobs.policy_id (+)\nAND ap.policy_id = np.policy_id\nAND ap.the_date = jobs.the_date (+)\nORDER BY UPPER(np.policy_name), ap.the_date\n)\nSELECT\nto_char(the_date,'MM/DD hh24:MI') the_date,\npolicy_name,\nDECODE('${freeCombo1}',\n'GB',size_gb,\n'Clients',clients,\n'Jobs',jobs) the_metric,\nto_char(the_date,'hh:MI AM') the_time,\nthe_size,\nthe_clients,\nthe_jobs\nFROM t1\nORDER BY UPPER(policy_name), the_date"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
