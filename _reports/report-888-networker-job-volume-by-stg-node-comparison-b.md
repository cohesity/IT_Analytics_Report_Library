---
title: "Networker Job Volume by Stg Node Comparison (B)"
report_id: 888
rtd_name: "LEG Job Volume by Stg Node Comparison.rtd"
description: "LEG Job Volume by Stg Node Comparison"
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
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\n--DD/WM/MM/Q/YY Job Volume by Storage Node\nWITH t1 as (\nSELECT \nto_char(trunc(j.start_date,'${freeCombo1}'),'MM/DD/YY') the_date,\nsubstr(jtm.drive_name,4,instr(jtm.drive_name,':',4,1)-4) storage_node,\nsum(jtm.kilobytes/1024/1024) job_size_gb\nFROM apt_v_job_tape_media jtm, apt_v_job j, apt_v_leg_job lj\nWHERE j.job_id = lj.job_id\nAND j.job_id = jtm.job_id\nAND j.client_id IN (${hosts})\nAND jtm.drive_name LIKE 'rd=%'\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND '${freeCombo2}' IN \n  CASE \n    WHEN '${freeCombo2}' NOT IN ('All') THEN\n      CASE\n        WHEN j.job_type_name LIKE 'Full%' THEN 'Full'\n        WHEN j.job_type_name LIKE 'Incr%' THEN 'Incremental'\n        WHEN j.job_type_name NOT LIKE 'Incr%' AND j.job_type_name NOT LIKE 'Full%' THEN 'Other'\n      END\n   ELSE 'All'\n END\nGROUP BY to_char(trunc(j.start_date,'${freeCombo1}'),\n'MM/DD/YY'),substr(jtm.drive_name,4,instr(jtm.drive_name,':',4,1)-4)\nORDER BY 1\n)\nSELECT \nthe_date,\nsum(DECODE(storage_node,'${queryCombo1}',job_size_gb,0)) stg_node1,\nsum(DECODE(storage_node,'${queryCombo2}',job_size_gb,0)) stg_node2\nFROM t1\nGROUP BY the_date"
has_explanation: false
products: [{"slug": "backup-manager-emc-networker-legato", "name": "EMC NetWorker (Legato)"}]
categories: []
product_slugs: ["backup-manager-emc-networker-legato"]
category_slugs: []
---
