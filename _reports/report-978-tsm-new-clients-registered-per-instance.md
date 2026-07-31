---
title: "TSM New Clients Registered per Instance"
report_id: 978
rtd_name: "TSM New Clients Registered per Instance.rtd"
description: "TSM New Clients Registered per Instance"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 09/09/2011\nSELECT n.instance_name,\ncount(DISTINCT ca.client_id) client_count\nFROM apt_v_tsm_client_association ca, apt_v_tsm_node n \nWHERE ca.client_id IN (${hosts})\nAND modification_date BETWEEN ${startDate} AND ${endDate}\nAND ca.node_id = n.node_id\nGROUP BY n.instance_name\nORDER BY 2"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
