---
title: "Networker Avg Throughput by Stg Node"
report_id: 887
rtd_name: "LEG Avg Throughput by Stg Node.rtd"
description: "LEG Avg Throughput by Stg Node"
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
sql_query: "--DD/WM/MM/Q/YY Job Volume by Storage Node\nSELECT \nto_char(trunc(j.start_date,'${freeCombo1}'),'MM/DD/YY') the_date,\nsubstr(jtm.drive_name,4,instr(jtm.drive_name,':',4,1)-4) storage_node, \navg(j.mbytes_sec) job_throughput\nFROM apt_v_job_tape_media jtm, apt_v_job j, apt_v_leg_job lj\nWHERE j.job_id = lj.job_id\nAND j.job_id = jtm.job_id\nAND j.client_id IN (${hosts})\nAND jtm.drive_name LIKE 'rd=%'\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.kilobytes>0\nAND '${freeCombo2}' IN \n  CASE \n    WHEN '${freeCombo2}' NOT IN ('All') THEN\n      CASE\n        WHEN j.job_type_name LIKE 'Full%' THEN 'Full'\n        WHEN j.job_type_name LIKE 'Incr%' THEN 'Incremental'\n        WHEN j.job_type_name NOT LIKE 'Incr%' AND j.job_type_name NOT LIKE 'Full%' THEN 'Other'\n      END\n   ELSE 'All'\n END\nGROUP BY to_char(trunc(j.start_date,'${freeCombo1}'),'MM/DD/YY'),substr(jtm.drive_name,4,instr(jtm.drive_name,':',4,1)-4)\nUNION ALL\nSELECT \nto_char(trunc(j.start_date,'${freeCombo1}'),'MM/DD/YY') the_date,\n'~Total' storage_node,\navg(j.mbytes_sec) job_throughput\nFROM apt_v_job_tape_media jtm, apt_v_job j, apt_v_leg_job lj\nWHERE j.job_id = lj.job_id\nAND j.job_id = jtm.job_id\nAND j.client_id IN (${hosts})\nAND jtm.drive_name LIKE 'rd=%'\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.kilobytes>0\nAND '${freeCombo2}' IN \n  CASE \n    WHEN '${freeCombo2}' NOT IN ('All') THEN\n      CASE\n        WHEN j.job_type_name LIKE 'Full%' THEN 'Full'\n        WHEN j.job_type_name LIKE 'Incr%' THEN 'Incremental'\n        WHEN j.job_type_name NOT LIKE 'Incr%' AND j.job_type_name NOT LIKE 'Full%' THEN 'Other'\n      END\n   ELSE 'All'\n END\nGROUP BY to_char(trunc(j.start_date,'${freeCombo1}'),'MM/DD/YY'),'~Total'\nORDER BY 1"
has_explanation: false
products: [{"slug": "backup-manager-emc-networker-legato", "name": "EMC NetWorker (Legato)"}]
categories: []
product_slugs: ["backup-manager-emc-networker-legato"]
category_slugs: []
---
