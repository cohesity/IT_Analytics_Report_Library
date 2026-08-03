---
title: "CommVault Job Size by iData Agent CL"
report_id: 1104
rtd_name: "CommVault Job Size by iData Agent CL.rtd"
description: "CommVault Job Size by iData Agent CL"
problem_statement: "How is my data distributed across the different applications?"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/20/2018\nWITH \nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays,\n${startDate} startDate,\nDECODE('${freeCombo1}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by\nFROM apt_v_dual\n)\nSELECT\nia.idataagent_name,\nROUND(SUM(j.kilobytes/var.div_by),2) job_size\nFROM apt_v_job j, apt_v_cmv_job cj, apt_v_cmv_idataagent ia, var\nWHERE j.job_id = cj.job_id\nAND cj.cmv_idataagent_id = ia.cmv_idataagent_id\nAND j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY ia.idataagent_name\nORDER BY 2 DESC"
has_explanation: false
products: [{"slug": "backup-manager-commvault", "name": "CommVault"}]
categories: []
product_slugs: ["backup-manager-commvault"]
category_slugs: []
---
