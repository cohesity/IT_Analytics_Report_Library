---
title: "Avamar Scanned-New DeDupe Ratio"
report_id: 976
rtd_name: "Avamar Scanned-New DeDupe Ratio.rtd"
description: "Avamar Scanned-New DeDupe Ratio"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "WITH t1 as (\nSELECT\ntrunc(aa.recorded_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')) the_date,\nsum(scanned_kb/1024/1024) scanned_gb,\nsum(new_kb/1024/1024) new_gb\nFROM \napt_v_avm_activities aa, apt_v_job j\nWHERE \naa.job_id = j.job_id\nAND aa.recorded_date BETWEEN ${startDate} AND ${endDate}\nAND aa.server_id = DECODE(${queryCombo1},999,aa.server_id,${queryCombo1})\nGROUP BY trunc(aa.recorded_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year'))\n)\nSELECT\nthe_date,\nscanned_gb,\nnew_gb,\n100-((new_gb/scanned_gb)*100) dedup_pct\nFROM t1"
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
