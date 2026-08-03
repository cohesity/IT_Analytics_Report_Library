---
title: "NBU Client Tape Lookup"
report_id: 1211
rtd_name: "NBU Client Tape Lookup.rtd"
description: "NBU Client Tape Lookup"
problem_statement: "I have to recover data from a host but NetBackup no longer has record of the backup because it has expired but I know the data is still on the tape somewhere.  I need the ability to put in a client name and have the report tell me all of the tapes that contain data for that client regardless of the expiration date."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 06/21/2018\nSELECT \ntm.tape_media_id,\ntm.media_name,\nnj.nbu_job_id,\nnj.job_id,\nnj.backup_id,\nnj.master_host_name,\nnj.client_host_name,\nnj.policy_id,\nnj.policy_name,\nnj.job_type_name,\nnj.start_date,\nnj.finish_date,\nnj.nbr_of_files,\nROUND(jtm.kilobytes/1024/1024) size_gb,\nnj.expiration_date\nFROM \napt_v_nbu_job_detail nj,apt_v_nbu_job_tape_media jtm, apt_v_tape_media tm\nWHERE\nnj.start_date BETWEEN ${startDate} AND  ${endDate}\nAND nj.job_id=jtm.job_id\nAND jtm.tape_media_id = tm.tape_media_id\nAND nj.client_id IN (${hosts})"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
