---
title: "Sample Use of Backup Window Dates"
report_id: 882
rtd_name: "Sample Use of Backup Window Dates.rtd"
description: "Sample Use of Backup Window Dates"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "SELECT rownum, start_date, finish_date \nFROM TABLE(rtd.ListOfBackupWindowDates(${startDate},${endDate},${queryCombo1})) bw"
has_explanation: false
products: [{"slug": "misc-utilities-general", "name": "General"}]
categories: []
product_slugs: ["misc-utilities-general"]
category_slugs: []
---
