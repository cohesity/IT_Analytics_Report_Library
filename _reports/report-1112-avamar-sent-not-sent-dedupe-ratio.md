---
title: "Avamar Sent-Not-Sent DeDupe Ratio"
report_id: 1112
rtd_name: "Avamar Sent-Not-Sent DeDupe Ratio.rtd"
description: "Avamar Sent-Not-Sent DeDupe Ratio"
problem_statement: "I want to see the de-duplication benefit I'm getting from Avamar in relation to how much data is being protected."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/16/2013\nWITH t1 AS (\nSELECT\nTRUNC(j.start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) the_date,\nROUND(SUM(aa.modified_not_sent_kb/1024/1024),2) modified_not_sent_gb,\nROUND(SUM(aa.modified_sent_kb/1024/1024),2) modified_sent_gb\nFROM \napt_v_avm_activities aa, apt_v_job j\nWHERE \naa.job_id = j.job_id\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.server_id = DECODE(${queryCombo1},999,j.server_id,${queryCombo1})\nGROUP BY \nTRUNC(j.start_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY'))\n)\nSELECT\nTO_CHAR(the_date,'YYYY/MM/DD') the_date,\nmodified_not_sent_gb,\nmodified_sent_gb,\nROUND((modified_sent_gb/modified_not_sent_gb)*100,2) dd_ratio\nFROM t1\nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
