---
title: "TSM ANR Messages"
report_id: 981
rtd_name: "TSM ANR Messages.rtd"
description: "TSM ANR Messages"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "WITH t1 as (\nSELECT count(jm.job_id) occurances, \njm.msg_code, jm.message, jm.explanation, jm.msg_type \nFROM apt_v_tsm_job j, apt_v_tsm_job_message jm\nWHERE j.job_id=jm.job_id\nAND msg_date BETWEEN ${startDate} AND ${endDate}\nAND j.client_id IN (${hosts})\nAND upper(msg_code) LIKE upper('${freeText1}')\nAND upper(message) LIKE upper('${freeText2}')\nGROUP BY jm.msg_code, jm.message, jm.explanation, jm.msg_type\n)\nSELECT occurances, \nCASE msg_type\n  WHEN 'E' THEN '<font color=\"red\">Error</font>'\n  WHEN 'W' THEN '<font color=\"orange\">Warning</font>'\n  ELSE '<font color=\"red\">Other</font>'\nEND type,\nmsg_code,\nmessage,explanation\nFROM T1 \nORDER by occurances DESC"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
