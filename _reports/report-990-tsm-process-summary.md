---
title: "TSM Process Summary"
report_id: 990
rtd_name: "TSM Process Summary.rtd"
description: "TSM Process Summary"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "SELECT i.instance_name, \n       p.process_type_name,\n       p.job_type_name,\n       p.process_id,\n       CASE j.summary_status \n         WHEN 0 THEN '<font color=\"blue\">Successful</font>'\n         WHEN 1 THEN '<font color=\"orange\">Partial</font>'\n         ELSE '<font color=\"red\">Failed</font>'\n       END status,\n       j.start_date, j.finish_date,\n       p.source_stg_pool || ' -> ' || p.destination_stg_pool transaction_desc,\n       j.kilobytes/1024/1024 size_GB, j.nbr_of_files,\n       p.nbr_examined_objects, p.nbr_failed_objects, p.media_wait_secs,\n       p.idle_secs, p.nbr_of_processes\n    FROM \n         apt_v_job j,\n         apt_v_tsm_process p,\n         apt_v_server s,\n         apt_v_server_instance i\n    WHERE j.server_id IN (${hosts})\n      AND j.finish_date BETWEEN ${startDate} AND ${endDate}\n      AND j.job_id = p.job_id\n      AND p.job_type_name LIKE DECODE('${freeCombo}','All','%','${freeCombo}')\n      AND j.server_id = s.server_id\n      AND p.server_instance_id = i.server_instance_id"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
