---
title: "NBU Load Balance by Tape Drive"
report_id: 933
rtd_name: "NBU Load Balance by Tape Drive.rtd"
description: "NBU Load Balance by Tape Drive"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "WITH \navg_tpt AS (\nSELECT to_char(j.start_date,'MM/DD/YY') avg_run_date,  \nROUND(NVL(avg(jtm.kilobytes/1024/1024),0 ) , 2) avgSize\nFROM apt_v_nbu_job_detail j, apt_v_nbu_job_tape_media jtm, apt_v_nbu_tape_drive td\nWHERE j.job_id = jtm.job_id\n  AND jtm.drive_id = td.drive_id\n  AND j.start_date BETWEEN ${startDate} AND ${endDate}\n  AND j.finish_date        IS NOT NULL\n  AND j.client_id in (${hosts})\n  AND j.kilobytes          > 1024\n  AND j.summary_status     <= 1\nGROUP BY to_char(j.start_date,'MM/DD/YY')\n),\nt1 AS (\nSELECT to_char(j.start_date,'MM/DD/YY') run_date, td.drive_name,  \nROUND(NVL(avg(jtm.kilobytes/1024/1024),0 ) , 2) size_gb\nFROM apt_v_nbu_job_detail j, apt_v_nbu_job_tape_media jtm, apt_v_nbu_tape_drive td\nWHERE j.job_id = jtm.job_id\n  AND jtm.drive_id = td.drive_id\n  AND j.start_date BETWEEN ${startDate} AND ${endDate}\n  AND j.finish_date        IS NOT NULL\n  AND j.client_id in (${hosts})\n  AND j.kilobytes          > 1024\n  AND j.summary_status     <= 1\nGROUP BY to_char(start_date,'MM/DD/YY'), td.drive_name\n)\nSELECT run_date, drive_name, \nCASE WHEN size_gb >= avgSize+(avgSize*(${freeCombo1}*.01))\n  THEN '<font color=\"red\">'||size_gb||'</font>'\n  ELSE '<font color=\"blue\">'||size_gb||'</font>'\nEND size_gb\nFROM t1, avg_tpt"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
