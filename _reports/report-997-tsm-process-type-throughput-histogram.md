---
title: "TSM Process Type Throughput Histogram"
report_id: 997
rtd_name: "TSM Process Type Throughput Histogram.rtd"
description: "TSM Process Type Throughput Histogram"
problem_statement: ""
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 10/30/2015\nWITH \navg_tpt AS (\nSELECT AVG((j.kilobytes/1024) / ((j.finish_date-j.start_date)*24*60*60)) avgThroughput\n  FROM apt_v_job j, apt_v_tsm_process p\n  WHERE j.server_id          IN (${hosts})\n    AND j.start_date         BETWEEN ${startDate} AND ${endDate}\n    AND j.finish_date        IS NOT NULL\n    AND j.job_id = p.job_id\n    AND j.finish_date        > j.start_date\n    AND j.kilobytes          > 1024\n    AND j.summary_status     <= 1\n),\npol AS ( \nSELECT DISTINCT p.job_type_name\n  FROM apt_v_job j, apt_v_tsm_process p\n  WHERE j.server_id          IN (${hosts})\n    AND j.start_date         BETWEEN ${startDate} AND ${endDate}\n    AND j.job_id = p.job_id\n    AND j.finish_date        IS NOT NULL\n    AND j.finish_date        > j.start_date\n    AND j.kilobytes          >1024\n    AND j.summary_status     <= 1\n), \njt AS (\nSELECT job_type_name, the_date\n  FROM pol, (SELECT the_date FROM TABLE(CAST(rtd.APTlistOfDates(${startDate}, ${endDate}, 10) AS dateListType))) d\n), \njobs AS (\nSELECT jt.job_type_name, jt.the_date, \n  ROUND(NVL(SUM(j.kilobytes/1024) / (SUM(j.finish_date-j.start_date)*24*60*60),0 ) , 2) throughput\n  FROM jt, apt_v_job j, apt_v_tsm_process p\n  WHERE jt.job_type_name   = p.job_type_name\n    AND j.client_id          IN (${hosts})\n    AND j.job_id = p.job_id\n    AND j.start_date         <= (jt.the_date + 3599/86400)\n    AND j.finish_date        >= jt.the_date\n    AND j.finish_date        IS NOT NULL\n    AND j.finish_date        > j.start_date\n    AND j.kilobytes          > 1024\n    AND j.summary_status     <= 1\n    GROUP BY jt.job_type_name, jt.the_date\n)   \nSELECT to_char(jt.the_date,'MM/DD hh:AM') the_date, jt.job_type_name,  \n  CASE \n  WHEN throughput > 0 AND throughput <= avgThroughput-(avgThroughput*.3333) THEN\n    '<table width=100% border=0 cellspacing=0 cellpadding=0><td style=background-color:red align=right><font color=white>'||throughput||'</td></table>'\n  WHEN throughput >= avgThroughput-(avgThroughput*.3333) AND throughput <= avgThroughput+(avgThroughput*.3333) THEN\n    '<table width=100% border=0 cellspacing=0 cellpadding=0><td style=background-color:yellow align=right><font color=black>'||throughput||'</td></table>'\n  WHEN throughput >= avgThroughput+(avgThroughput*.3333) THEN\n    '<table width=100% border=0 cellspacing=0 cellpadding=0><td style=background-color:green align=right><font color=white>'||throughput||'</td></table>'\n  WHEN throughput = 0 THEN\n    ' '\n  END throughput  \n  FROM jt, jobs, avg_tpt \n  WHERE jt.job_type_name       = jobs.job_type_name (+)\n    AND jt.the_date        = jobs.the_date (+)\n  ORDER BY upper(jt.job_type_name), jt.the_date"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
