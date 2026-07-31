---
title: "NBU Image Logs.D"
report_id: 1077
rtd_name: "NBU Image Logs.D.rtd"
description: "NBU Image Logs"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/20/2012\n--Drilldown templateName is: NBUImageLogs.D\nSELECT \nm.hostname master_server,\nc.hostname client,\nl.trans_date,\nl.backup_id image_id,\nDECODE(l.trans_type,'D','Duplication','E','Expiration','P','Primary Change') trans_type,\nDECODE(l.was_successful,'Y','Successful','N','Failed','Unknown') status_name,\nDECODE(l.was_successful,'Y','blue','N','red','white') status_dot,\nl.msg_log\nFROM \napt_v_nbu_image_log l,  apt_v_server c, apt_v_server m\nWHERE \nbackup_id = '${BackupID}'\nAND l.client_id = c.server_id\nAND l.server_id = m.server_id"
has_explanation: false
products: []
categories: []
product_slugs: []
category_slugs: []
---
