---
title: "NBU Load Balance By Master Server"
report_id: 956
rtd_name: "NBU Load Balance by Master Server.rtd"
description: "NBU Load Balance by Master Server"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 04/10/2012\n--NBU Master Server Load Balance  \nWITH\nt1 AS (\nSELECT \nj.master_host_name,\ncount(DISTINCT j.media_server_id) media_server_count,\ncount(DISTINCT td.drive_id) drive_count,\ncount(j.job_id) job_count,\nNVL(SUM((j.finished_readwrite-j.started_readwrite)*24*60*60),0) duration_secs,\nROUND(NVL(SUM(j.kilobytes/1024/1024),0 ),2) job_size,\nROUND(NVL(SUM(j.kilobytes/1024)/(SUM(j.finished_readwrite-j.started_readwrite)*24*60*60),0 ),2) throughput\nFROM apt_v_nbu_job_try j, apt_v_nbu_job_tape_media jtm, apt_v_nbu_tape_drive td\nWHERE j.job_id = jtm.job_id\nAND jtm.drive_id = td.drive_id\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.finish_date IS NOT NULL\nAND j.server_id IN (${hosts})\nAND j.media_host_name IS NOT NULL\nAND j.kilobytes > 1024\nAND j.summary_status <= 1\nGROUP BY j.master_host_name\nHAVING ROUND(NVL(AVG(jtm.kilobytes/1024/1024),0 ),2) > 1 --Exclude Small Stuff\n),\navg_val AS (\nSELECT \nROUND(AVG(drive_count),2) avg_drive_count,\nROUND(AVG(job_count),2) avg_job_count,\nROUND(AVG(duration_secs),2) avg_duration_secs,\nROUND(AVG(job_size),2) avg_job_size,\nROUND(AVG(throughput),2) avg_throughput\nFROM t1\n)\nSELECT \nmaster_host_name,\nmedia_server_count,\ndrive_count,\njob_size,\navg_job_size,\nROUND(((job_size-avg_job_size)/avg_job_size)*100,2) pct_avg_job_size,\nCASE \nWHEN job_size BETWEEN avg_job_size-(avg_job_size*.3333) AND avg_job_size+(avg_job_size*.3333) THEN 'yellow'\nWHEN job_size < avg_job_size-(avg_job_size*.3333) THEN 'red'\nWHEN job_size > avg_job_size+(avg_job_size*.3333) THEN 'green'\nELSE 'white'\nEND job_size_dot,\njob_count,\navg_job_count,\nROUND(((job_count-avg_job_count)/avg_job_count)*100,2) pct_avg_job_count,\nCASE \nWHEN job_count BETWEEN avg_job_count-(avg_job_count*.3333) AND avg_job_count+(avg_job_count*.3333) THEN 'yellow'\nWHEN job_count < avg_job_count-(avg_job_count*.3333) THEN 'red'\nWHEN job_count > avg_job_count+(avg_job_count*.3333) THEN 'green'\nELSE 'white'\nEND job_count_dot,\nrtd.secsToHoursMinSecs(duration_secs) duration,\nrtd.secsToHoursMinSecs(avg_duration_secs) avg_duration_secs,\nROUND(((duration_secs-avg_duration_secs)/avg_duration_secs)*100,2) pct_avg_duration_secs,\nCASE \nWHEN duration_secs BETWEEN avg_duration_secs-(avg_duration_secs*.3333) AND avg_duration_secs+(avg_duration_secs*.3333) THEN 'yellow'\nWHEN duration_secs < avg_duration_secs-(avg_duration_secs*.3333) THEN 'red'\nWHEN duration_secs > avg_duration_secs+(avg_duration_secs*.3333) THEN 'green'\nELSE 'white'\nEND duration_secs_dot,\nthroughput,\navg_throughput,\nROUND(((throughput-avg_throughput)/avg_throughput)*100,2) pct_avg_throughput,\nCASE \nWHEN throughput BETWEEN avg_throughput-(avg_throughput*.3333) AND avg_throughput+(avg_throughput*.3333) THEN 'yellow'\nWHEN throughput < avg_throughput-(avg_throughput*.3333) THEN 'red'\nWHEN throughput > avg_throughput+(avg_throughput*.3333) THEN 'green'\nELSE 'white'\nEND throughput_dot\nFROM t1, avg_val\nORDER BY job_size DESC"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
