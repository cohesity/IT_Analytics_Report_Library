---
title: "NBU Top 10 Error Code Occurrances"
report_id: 948
rtd_name: "NBU Top 10 Error Code Occurrances.rtd"
description: "NBU Top 10 Error Code Occurrances"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last updated: 12/06/2012\nWITH \nt1 AS ( \nSELECT\nvendor_status,\ncount(job_id) occurances\nFROM apt_v_nbu_job\nWHERE client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nAND vendor_status NOT IN (0,1,150)\nGROUP BY vendor_status\nORDER BY 2 DESC\n)\nSELECT * \nFROM t1\nWHERE rownum <= ${freeCombo1}"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
