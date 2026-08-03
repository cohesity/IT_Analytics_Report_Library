---
title: "NBU Image Duplication Jobs"
report_id: 914
rtd_name: "NBU Image Duplication Jobs.rtd"
description: "NBU Image Duplication Jobs"
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
sql_query: "--Drilldowns\n--Dup Jobs Image List\nWITH t1 as (\nSELECT j.job_id,\naptStringConcat('<a onclick=\"drilldown(''templateName=NBUImageLocations.D&amp;BackupID='||jf.pathname||''', this, '''' ); return false;\" href=\"#\">'||jf.pathname||'</a>') images_duplicated\nFROM  apt_v_nbu_job_file jf, apt_v_nbu_job j\nWHERE j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.client_id IN (${hosts})\nAND j.job_id = jf.job_id\nAND j.job_type = 107\nGROUP BY j.job_id\n)\nSELECT t1.job_id, jd.nbu_job_id, jd.master_host_name, jd.storage_unit_label, \njd.start_date, jd.finish_date, jd.kilobytes/1024/1024 size_gb, jd.nbr_of_files, jd.vendor_status,\nDECODE(jd.is_active,'Y','Active','N','Completed') State,\nt1.images_duplicated\nFROM t1, apt_v_nbu_job_detail jd\nWHERE t1.job_id = jd.job_id\nAND '${freeCombo1}' IN \n  CASE \n    WHEN '${freeCombo1}' NOT IN ('All') THEN\n      CASE\n        WHEN jd.is_active = 'Y'  THEN 'Active'\n        WHEN jd.is_active = 'N'  THEN 'Completed'\n      END\n   ELSE 'All'\n END"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
