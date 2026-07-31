---
title: "Networker Job Volume by Stg Node.P"
report_id: 886
rtd_name: "LEG Job Volume by Stg Node.P.rtd"
description: "LEG Job Volume by Stg Node"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "SELECT substr(jtm.drive_name,4,instr(jtm.drive_name,':',4,1)-4) storage_node, \nsum(jtm.kilobytes/1024/1024) job_volume_gb\nFROM apt_v_job_tape_media jtm, apt_v_leg_job j\nWHERE \nj.job_id = jtm.job_id\nAND jtm.drive_name LIKE 'rd=%'\nAND j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND '${freeCombo1}' IN \n  CASE \n    WHEN '${freeCombo1}' NOT IN ('All') THEN\n      CASE\n        WHEN j.job_type_name LIKE 'Full%' THEN 'Full'\n        WHEN j.job_type_name LIKE 'Incr%' THEN 'Incremental'\n        WHEN j.job_type_name NOT LIKE 'Incr%' AND j.job_type_name NOT LIKE 'Full%' THEN 'Other'\n      END\n   ELSE 'All'\n END\nGROUP BY jtm.drive_id, jtm.drive_name"
has_explanation: false
products: [{"slug": "backup-manager-emc-networker-legato", "name": "EMC NetWorker (Legato)"}]
categories: []
product_slugs: ["backup-manager-emc-networker-legato"]
category_slugs: []
---
