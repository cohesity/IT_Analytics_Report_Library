---
title: "Job and Client Success by Window"
report_id: 904
rtd_name: "Job and Client Success by Window.rtd"
description: "Job and Client Success by Window"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "WITH t1 as (\n  SELECT start_date, finish_date finish_date  FROM \n              TABLE(rtd.ListOfBackupWindowDates(${startDate},${endDate},${queryCombo1})) bw\n),\nt2 as (\n  SELECT t1.start_date, t1.finish_date,\n      count(DISTINCT client_id) Client_count,\n      count(j.job_id) Job_Count,\n      sum(1*(1-abs(sign(j.summary_status-0)))) success,\n      sum(1*(1-abs(sign(j.summary_status-1)))) partial,\n      sum(1*(1-abs(sign(j.summary_status-2)))) failed,\n      sum(1*(1-abs(sign(j.vendor_state-1)))) running,\n      sum(1*(1-abs(sign(j.vendor_state-0)))) queued,\n      sum(1*(1-abs(sign(j.vendor_state-2)))) re_queued\n      FROM apt_v_job j,t1\n      WHERE j.start_date BETWEEN t1.start_date AND t1.finish_date\n      AND t1.start_date >= ${startDate}\n      AND j.server_id IN (${hosts})\n      AND j.job_type_name like '%Backup'\n      AND j.vendor_status NOT IN (150)\n      GROUP BY  t1.start_date, t1.finish_date\n      ORDER BY t1.start_date, t1.finish_date\n),\nt3 as (\n  SELECT t1.start_date, t1.finish_date, client_id, min(summary_status) \n      FROM apt_v_job j,t1\n      WHERE j.start_date BETWEEN t1.start_date AND t1.finish_date\n      AND t1.start_date >= ${startDate}\n      AND j.server_id IN (${hosts})\n      AND j.vendor_status NOT IN (150)\n      GROUP BY client_id, t1.start_date, t1.finish_date\n      HAVING min(summary_status) > 1\n      ORDER BY client_id, t1.start_date, t1.finish_date\n) \nSELECT DISTINCT t2.start_date AS \"Window Start\", t2.finish_date AS \"Window End\",\n      t2.job_count AS \"Jobs\", (t2.success+t2.partial) AS \"Successful\", \n      t2.failed AS \"Failed\", t2.running, t2.queued+t2.re_queued AS \"Queued\", \n      (t2.success + t2.partial) / t2.job_count*100 AS \"Job Success Rate\",\n      t2.client_count AS \"Total Clients\", \n      (SELECT count(*) FROM t3 WHERE t2.start_date = t3.start_date \n        AND t2.finish_date = t3.finish_date ) AS \"Failed Clients\",\n      (t2.client_count-(SELECT count(*) FROM t3 WHERE t2.start_date = t3.start_date \n        AND t2.finish_date = t3.finish_date )) / t2.client_count*100 AS \"Client Success Rate\"\n      FROM t2,t3\n      WHERE t2.start_date = t3.start_date (+)\n      AND t2.finish_date = t3.finish_date (+)"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
