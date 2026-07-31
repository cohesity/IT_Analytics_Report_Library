---
title: "Job Volume Per Backup Server"
report_id: 900
rtd_name: "Job Volume Per Backup Server.rtd"
description: "Job Volume Per Backup Server"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 05/19/2012\n--Job volume per backup master server\n--Note: Key's off of the server_id rather than the client_id.\n--Also plot max and average on a separate axis when mixing lines and bars on the same chart\n--otherwise the average line will appear along the top instead of the center.\nWITH \nt1 AS (\nSELECT \nserver_name,\nROUND(SUM(kilobytes/1024/1024/1024),2) job_size_tb\nFROM apt_v_job\nWHERE server_id IN (${hosts})\nAND finish_date BETWEEN ${startDate} AND ${endDate}\nAND '${freeCombo1}' IN \n  CASE \n    WHEN '${freeCombo1}' NOT IN ('All') THEN\n      CASE\n        WHEN job_type_name like 'Full%' THEN 'Full'\n        WHEN job_type_name like 'Incr%' THEN 'Incremental'\n        WHEN job_type_name not like 'Incr%' AND job_type_name not like 'Full%' THEN 'Other'\n      END\n   ELSE 'All'\n END\nGROUP BY server_name\n),\nt2 AS ( \nSELECT \nROUND(MAX(job_size_tb),2) max_job_size_tb,\nROUND(AVG(job_size_tb),2) avg_job_size_tb\nFROM t1\n)\nSELECT\nt1.server_name,\nt1.job_size_tb,\nt2.max_job_size_tb,\nt2.avg_job_size_tb\nFROM t1,t2\nORDER BY 2 DESC"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
