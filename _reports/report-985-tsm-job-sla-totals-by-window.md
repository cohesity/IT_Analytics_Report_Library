---
title: "TSM Job SLA Totals by Window"
report_id: 985
rtd_name: "TSM Job SLA Totals by Window.rtd"
description: "TSM Job SLA Totals by Window"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "WITH t1 as (\n  SELECT start_date, finish_date finish_date  FROM \n              TABLE(rtd.ListOfBackupWindowDates(${startDate},${endDate}, \n      apt_BackupWindowListType( \n        APT_BACKUPWINDOWTYPE('Mon',44,68), \n        APT_BACKUPWINDOWTYPE('Tue',68,92), \n        APT_BACKUPWINDOWTYPE('Wed',92,116), \n        APT_BACKUPWINDOWTYPE('Thu',116,140), \n        APT_BACKUPWINDOWTYPE('Weekend',140,212) ))) bw\n),\nt2 as (\n  SELECT t1.start_date, t1.finish_date,\n      count(j.job_id) Job_Count,\n      sum(1*(1-abs(sign(j.summary_status-0)))) success,\n      sum(1*(1-abs(sign(j.summary_status-1)))) partial,\n      sum(1*(1-abs(sign(j.summary_status-2)))) failed\n      FROM apt_v_tsm_job j,t1\n      WHERE j.start_date BETWEEN t1.start_date AND t1.finish_date\n      AND t1.start_date >= ${startDate}\n      AND j.client_id IN (${hosts})\n      AND j.job_type_name like '%Backup'\n      AND j.summary_status IS NOT null \n      AND j.vendor_state IS NOT null \n      GROUP BY  t1.start_date, t1.finish_date\n      ORDER BY t1.start_date, t1.finish_date\n) SELECT t2.start_date AS \"Window Start\", t2.finish_date AS \"Window End\", \n      t2.job_count AS \"Jobs\", t2.success AS \"Successful\", t2.partial AS \"Partial\", \n      t2.failed AS \"Failed\",\n      (t2.success+t2.partial) / t2.job_count AS \"Success Rate\"\n      FROM t2"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
