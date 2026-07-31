---
title: "Clients Backed up by Multiple Backup Servers"
report_id: 1170
rtd_name: "Clients Backed up by Multiple Backup Servers.rtd"
description: "Clients Backed up by Multiple Backup Servers"
problem_statement: "Sometimes by choice, sometimes by accident we have clients that are being backed up by more than one backup server.  I need a report which can help me identify these clients."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/16/2015\nSELECT\nclient_id,\nclient_name,\nCOUNT(DISTINCT server_id) server_count,\naptStringConcat(DISTINCT product_type_name) backup_products,\naptStringConcat(DISTINCT server_name) backup_servers\nFROM apt_v_job\nWHERE client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY \nclient_id,\nclient_name\nHAVING COUNT(DISTINCT server_id) > 1"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
