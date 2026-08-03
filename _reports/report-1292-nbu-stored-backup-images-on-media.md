---
title: "NBU Stored Backup Images on Media"
report_id: 1292
rtd_name: "NetBackup Stored Backup Images on Media.rtd"
description: "This report shows you the total amount of data that was backed up but has not expired yet for each of the days in the report scope. "
problem_statement: "I need to know how much data is being stored on media."
author: ""
modified_date: "2024-06-03"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "WITH \nvar AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays,\nDECODE('${freeCombo2}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\nt1 AS (\nSELECT\nTRUNC(j.start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) the_date,\nCOUNT(DISTINCT j. client_id) client_count,\nROUND(SUM(CASE WHEN j.expiration_date > sysdate THEN (j.kilobytes/div_by) ELSE 0 END),2) job_volume,\nROUND(SUM(CASE WHEN dm.expiration_date > sysdate THEN (dm.written_kilobytes/div_by) ELSE 0 END),2) dm_job_volume,\nROUND(SUM(CASE WHEN tm.expiration_date > sysdate THEN (tm.kilobytes/div_by) ELSE 0 END),2) tm_job_volume,\nROUND(AVG(CASE WHEN j.expiration_date > sysdate THEN (j.kilobytes/div_by) ELSE 0 END),2) avg_job_volume,\nROUND(AVG(CASE WHEN dm.expiration_date > sysdate THEN (dm.written_kilobytes/div_by) ELSE 0 END),2) dm_avg_volume,\nROUND(AVG(CASE WHEN tm.expiration_date > sysdate THEN (tm.kilobytes/div_by) ELSE 0 END),2) tm_avg_volume\nFROM apt_v_nbu_job_detail j, apt_v_nbu_job_disk_media dm, apt_v_nbu_job_tape_media tm, var\nWHERE j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.job_id=dm.job_id (+)\nAND j.job_id=tm.job_id (+)\nAND REGEXP_LIKE(j.policy_name,'${freeText1}')\nGROUP BY\nTRUNC(j.start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY'))\n)\nSELECT\nTO_CHAR(the_date,'MM/DD/YY') the_date,\nTO_CHAR(the_date,'YYYYMMDD') sort_order,\nclient_count,\nAVG(avg_job_volume + dm_avg_volume + tm_avg_volume) avg_job_volume,\nSUM(job_volume + dm_job_volume + tm_job_volume) job_volume\nFROM t1\nGROUP BY the_date, client_count\nORDER BY 2"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
