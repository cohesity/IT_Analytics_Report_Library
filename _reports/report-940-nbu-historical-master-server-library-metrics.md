---
title: "NBU Historical Master Server - Library Metrics"
report_id: 940
rtd_name: "NBU Historical Master Server - Library Metrics.rtd"
description: "NBU Historical Master Server - Library Metrics"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 06/13/2012\nWITH t1 AS (\nSELECT to_char(trunc(j.start_date,DECODE('${freeCombo2}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YY') the_date, \nj.server_name||' - '||tl.library_name master_library, \ncount(DISTINCT tm.tape_media_id) tapes_used,\nsum(jtm.kilobytes/1024/1024) tape_volume_gb,\nsum(j.kilobytes/1024/1024) job_volume_gb,\ncount(DISTINCT j.client_id) distinct_clients,\nsum(j.nbr_of_files) file_count,\ncount(DISTINCT j.job_id) job_count\nFROM apt_v_tape_media tm,apt_v_tape_library tl, apt_v_job j,apt_v_nbu_job_tape_media jtm\nWHERE j.client_id IN  (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.job_id = jtm.job_id \nAND jtm.tape_media_id = tm.tape_media_id       \nAND tm.library_id=tl.library_id \nGROUP BY to_char(trunc(j.start_date,DECODE('${freeCombo2}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YY'),j.server_name||' - '||tl.library_name\nORDER BY 1 DESC\n)\nSELECT\nthe_date,\nmaster_library,\nDECODE('${freeCombo1}',\n'Tape Volume(GB)',tape_volume_gb,\n'Job Volume(GB)',job_volume_gb,\n'Tapes Used',tapes_used,\n'Distinct Clients',distinct_clients,\n'File Count',file_count,\n'Job Count',job_count\n) metric\nFROM t1 \nORDER by 1 DESC"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
