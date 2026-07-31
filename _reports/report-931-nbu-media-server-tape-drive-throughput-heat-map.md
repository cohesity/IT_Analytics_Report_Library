---
title: "NBU Media Server - Tape Drive Throughput Heat Map"
report_id: 931
rtd_name: "NBU Media Server - Tape Drive Throughput Heat Map.rtd"
description: "NBU Media Server - Tape Drive Throughput Heat Map"
problem_statement: ""
author: "dave.king@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: dave.king@aptare.com\n--Last Updated: 05/01/2012\n--NBU Media Server Tape Drive Throughput Heat Map\nWITH \navg_tpt AS (\nSELECT \nAVG((j.kilobytes/1024) / ((j.finished_readwrite-j.started_readwrite)*24*60*60)) avgThroughput\nFROM apt_v_nbu_job_try j\nWHERE j.media_server_id IN (${hosts})\nAND j.started_readwrite BETWEEN ${startDate} AND ${endDate}\nAND j.finished_readwrite  IS NOT NULL\nAND j.finished_readwrite > j.started_readwrite\nAND j.kilobytes > 1024\nAND j.summary_status <= 1\n),\npol AS ( \nSELECT \nDISTINCT jtm.drive_id, j.media_host_name\nFROM apt_v_nbu_job_try j, apt_v_job_tape_media jtm\nWHERE j.job_id = jtm.job_id\nAND j.media_server_id IN (${hosts})\nAND j.started_readwrite BETWEEN ${startDate} AND ${endDate}\nAND j.finished_readwrite IS NOT NULL\nAND j.finished_readwrite > j.started_readwrite\nAND j.kilobytes > 1024\nAND j.summary_status <= 1\n), \nap AS (\nSELECT \npol.drive_id, pol.media_host_name, d.the_date\nFROM pol, (SELECT the_date FROM TABLE(CAST(rtd.APTlistOfDates(${startDate}, ${endDate},10) AS dateListType))) d\n), \njobs AS (\nSELECT \nap.drive_id, \nap.media_host_name, \nap.the_date,\n0 throughput\nFROM ap\nUNION ALL\nSELECT \nap.drive_id, \nj.media_host_name, \nap.the_date, \nROUND(NVL(SUM(j.kilobytes/1024)/(SUM(j.finished_readwrite-j.started_readwrite)*24*60*60),0 ),2) throughput\nFROM ap, apt_v_nbu_job_try j, apt_v_job_tape_media jtm\nWHERE j.job_id = jtm.job_id \nAND ap.drive_id = jtm.drive_id\nAND j.media_server_id  IN (${hosts})\nAND j.started_readwrite <= (ap.the_date + 3599/86400)\nAND j.finished_readwrite >= ap.the_date\nAND j.finished_readwrite IS NOT NULL\nAND j.finished_readwrite > j.started_readwrite\nAND j.kilobytes > 1024\nAND j.summary_status <= 1\nGROUP BY ap.drive_id, j.media_host_name, ap.the_date\n),\njobs1 AS (\nSELECT \ndrive_id, \nmedia_host_name, \nthe_date,\nmax(throughput) throughput\nFROM jobs\nGROUP BY \ndrive_id, \nmedia_host_name, \nthe_date\n)   \nSELECT \nto_char(jobs1.the_date,'MM/DD hh:AM') the_date, \njobs1.media_host_name||' - '||td.drive_name media_server_tape_drive,  \nthroughput,\nCASE \n\n\nWHEN throughput > 0 AND throughput <= avgThroughput-(avgThroughput*.3333) THEN\n    '<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><td bgcolor=\"#B30505\" align=right><font color=\"white\">'||throughput||'</td></table>'\n  WHEN throughput >= avgThroughput-(avgThroughput*.3333) AND throughput <= avgThroughput+(avgThroughput*.3333) THEN\n    '<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><td bgcolor=\"#DBD611\" align=right><font color=\"black\">'||throughput||'</td></table>'\n  WHEN throughput >= avgThroughput+(avgThroughput*.3333) THEN\n    '<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><td bgcolor=\"#347800\" align=right><font color=\"white\">'||throughput||'</td></table>'\n  WHEN throughput = 0 THEN\n    ' '\n\nEND throughput_dot\n\nFROM jobs1, avg_tpt, apt_v_tape_drive td\nWHERE jobs1.drive_id = td.drive_id\nAND jobs1.media_host_name    is not null\nORDER BY upper(jobs1.media_host_name), upper(td.drive_name), jobs1.the_date"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
