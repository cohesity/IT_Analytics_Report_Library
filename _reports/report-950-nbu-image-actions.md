---
title: "NBU Image Actions"
report_id: 950
rtd_name: "NBU Image Actions.rtd"
description: "NBU Image Actions"
problem_statement: "I needs a report that shows me what images are expiring for compliance and so I can check the capacity against my dedupe storage appliance."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 01/22/2015\nSELECT\nl.job_id, \nm.hostname master_server,\nc.hostname client,\nl.trans_date,\nl.backup_id image_id,\nj.kilobytes/1024/1024 size_gb,\nDECODE(l.trans_type,'D','Duplication','E','Expiration','P','Primary Change') trans_type,\nDECODE(l.was_successful,'Y','blue','N', 'red','white') status_dot,\nl.msg_log\nFROM apt_v_nbu_image_log l,  apt_v_nbu_job j, apt_v_server c, apt_v_server m\nWHERE l.client_id IN (${hosts})\nAND j.client_id IN (${hosts})\nAND l.job_id = j.job_id\nAND l.server_id = m.server_id (+)\nAND l.client_id = c.server_id (+)\nAND l.trans_date BETWEEN ${startDate} AND ${endDate}\nAND trans_type LIKE DECODE('${freeCombo1}','All','%','Duplication','D','Expiration','E','Primary Change','P')\nAND l.was_successful LIKE DECODE('${freeCombo2}','All','%','Successful','Y','Failed','N')"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
