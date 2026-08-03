---
title: "Job and Client Success by Window and Server Group"
report_id: 897
rtd_name: "Job and Client Success by Window and Server Group.rtd"
description: "Job and Client Success by Window and Server Group"
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
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\n--This report requires a defined backup window and a properly structured\n--server grouping\n--Status 1 jobs (partially successful) are treated as successful\n--A comma separated list of error codes can be specified for exclusion at runtime.\n--If no error error code is to be excluded enter None or some other bogus value\n--Note: \n-- 1. You have to enter something in the Exclude Error Codes: i.e. None\n-- 2. If you put in a comma separated list of codes, use no spaces!\n-- EXAMPLE 150,50,6 NOT 150, 50, 6\n-- You can always edit the template and remove this option from the Report Designer and the SQL\n-- or you can hard code the errors for exclusion\nWITH \ng0 as (--Be sure to only select one server group if multiple were selected\nSELECT max(group_id) server_group\nFROM apt_v_group \nWHERE group_id IN (decode('${serverGroups}','',-1,'${serverGroups}'))\n),\nt1 as (--Seed the backup window dated based on the window_id from the dropdown\nSELECT start_date, finish_date finish_date  \nFROM TABLE(rtd.ListOfBackupWindowDates(${startDate},${endDate},${queryCombo1})) bw\n),\nt2 as ( --Aggregate the job data by  the server group selected\nSELECT \nrtd.getServerGroupContextById(g0.server_group,client_id,1) server_group,\nt1.start_date, t1.finish_date,\ncount(DISTINCT client_id) Client_count,\ncount(j.job_id) Job_Count,\nsum(1*(1-abs(sign(j.summary_status-0)))) success,\nsum(1*(1-abs(sign(j.summary_status-1)))) partial,\nsum(1*(1-abs(sign(j.summary_status-2)))) failed,\nsum(1*(1-abs(sign(j.vendor_state-1)))) running,\nsum(1*(1-abs(sign(j.vendor_state-0)))) queued,\nsum(1*(1-abs(sign(j.vendor_state-2)))) re_queued\nFROM apt_v_job j,t1,g0\nWHERE j.start_date BETWEEN t1.start_date AND t1.finish_date\nAND t1.start_date >= ${startDate}\nAND j.client_id IN (${hosts})\nAND j.job_type_name like '%Backup'\nAND j.vendor_status NOT IN (${freeText1})\nGROUP BY  \nrtd.getServerGroupContextById(g0.server_group,client_id,1) ,\nt1.start_date, t1.finish_date\nORDER BY \n      rtd.getServerGroupContextById(g0.server_group,client_id,1) ,\n      t1.start_date, t1.finish_date\n),\nt3 as (\n      SELECT \n      rtd.getServerGroupContextById(g0.server_group,client_id,1) server_group,\n      t1.start_date, t1.finish_date, client_id, min(summary_status) \n      FROM apt_v_job j,t1,g0\n      WHERE j.start_date BETWEEN t1.start_date AND t1.finish_date\n      AND t1.start_date >= ${startDate}\n      AND j.server_id IN (${hosts})\n      AND j.vendor_status NOT IN (150)\n      GROUP BY client_id, \n      rtd.getServerGroupContextById(g0.server_group,client_id,1) ,\n      t1.start_date, t1.finish_date\n      HAVING min(summary_status) > 1\n      ORDER BY \n      client_id, \n      rtd.getServerGroupContextById(g0.server_group,client_id,1) ,\n      t1.start_date, t1.finish_date\n) \nSELECT DISTINCT \nt2.server_group, \nt2.start_date AS \"Window Start\", \nt2.finish_date AS \"Window End\",\nt2.job_count AS \"Jobs\", \n(t2.success+t2.partial) AS \"Successful\", \nt2.failed AS \"Failed\", t2.running, t2.queued+t2.re_queued AS \"Queued\", \n(t2.success + t2.partial) / t2.job_count*100 AS \"Job Success Rate\",\n      t2.client_count AS \"Total Clients\", \n      (SELECT count(*) FROM t3 WHERE t2.start_date = t3.start_date \n        AND t2.finish_date = t3.finish_date ) AS \"Failed Clients\",\n      (t2.client_count-(SELECT count(*) FROM t3 WHERE t2.start_date = t3.start_date \n        AND t2.finish_date = t3.finish_date )) / t2.client_count*100 AS \"Client Success Rate\"\n      FROM t2,t3\n      WHERE t2.start_date = t3.start_date (+)\n      AND t2.finish_date = t3.finish_date (+)"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
