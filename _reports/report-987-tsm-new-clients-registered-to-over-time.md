---
title: "TSM New Clients Registered to Over Time"
report_id: 987
rtd_name: "TSM New Clients Registered to Over Time.rtd"
description: "TSM New Clients Registered to Over Time"
problem_statement: ""
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/09/2011\n--Displays the number of clients registered to TSM grouped by Day, Week, Month, Qtr, or Year\nSELECT  trunc(modification_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year')) the_date,\ncount(DISTINCT client_id) client_count \nFROM apt_v_tsm_client_association\nWHERE client_id IN (${hosts})\nAND modification_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY trunc(modification_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year'))\nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
