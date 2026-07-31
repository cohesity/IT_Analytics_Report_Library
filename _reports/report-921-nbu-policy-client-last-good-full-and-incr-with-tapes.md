---
title: "NBU Policy Client Last Good Full and Incr with Tapes"
report_id: 921
rtd_name: "NBU Policy Client Last Good Full and Incr with Tapes.rtd"
description: "NBU Policy Client Last Good Full and Incr with Tapes"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "-- Author: rich.rose@aptare.com\n-- Last Updated: 02/06/2012\nWITH\nfull AS (--Find the last successful full backup that for each client\nSELECT\nnj.client_id,\nnj.policy_id,\nmax(nj.job_id) job_id\nFROM apt_v_nbu_job nj\nWHERE nj.client_id IN (${hosts})\nAND nj.start_date BETWEEN ${startDate} AND ${endDate}\nAND nj.job_type = 101\nAND nj.summary_status IN (0,1)\nAND nj.expiration_date >= sysdate\nGROUP BY \nnj.client_id,nj.policy_id\n),\nincr AS (--Find the last successful incr backup that for each client\nSELECT\nnj.client_id,nj.policy_id,\nmax(nj.job_id) job_id\nFROM apt_v_nbu_job nj\nWHERE nj.client_id IN (${hosts})\nAND nj.start_date BETWEEN ${startDate} AND ${endDate}\nAND nj.job_type = 102\nAND nj.summary_status IN (0,1)\nAND nj.expiration_date >= sysdate\nGROUP BY nj.client_id,nj.policy_id\n),\nftapes AS (--String together all the tapes used for full jobs\nSELECT\nfull.client_id,\nfull.policy_id,\nfull.job_id,\naptStringConcat(ntm.bar_code) ftapes\nFROM full, apt_v_nbu_job_tape_media jtm, apt_v_nbu_tape_media ntm\nWHERE full.job_id = jtm.job_id\nAND jtm.tape_media_id = ntm.tape_media_id\nGROUP BY full.client_id, full.policy_id, full.job_id\n),\nitapes AS (--String together all the tapes used for incr jobs\nSELECT\nincr.client_id,\nincr.job_id,\nincr.policy_id,\naptStringConcat(ntm.bar_code) itapes\nFROM incr, apt_v_nbu_job_tape_media jtm, apt_v_nbu_tape_media ntm\nWHERE incr.job_id = jtm.job_id\nAND jtm.tape_media_id = ntm.tape_media_id\nGROUP BY incr.client_id,incr.policy_id,incr.job_id\n),\nijobs AS (--Find all the incremental backups that occurred after the full\nSELECT\nnj.client_id,\nnj.policy_id,\ncount(nj.job_id) job_count,\nsum(DECODE(nj.summary_status,0,1,1,1,0)) success,\nsum(DECODE(nj.summary_status,2,1,0)) failed,\nsum(DECODE(nj.summary_status,0,nj.duration_secs,1,nj.duration_secs,0)) duration_secs\nFROM full, apt_v_nbu_job nj\nWHERE nj.client_id = full.client_id\nAND nj.job_id > full.job_id\nAND nj.job_type = 102\nGROUP BY nj.client_id,nj.policy_id\n)\nSELECT\nfj.master_host_name,\nfj.client_id,\nfj.client_host_name,\nfj.policy_id,\nfj.policy_name fj_policy_name,\nfj.schedule_name fj_schedule_name,\nfj.job_id fj_job_id,\nfj.nbu_job_id fj_nbu_job_id,\nftapes,\nfj.finish_date fj_finish_date,\nfj.duration fj_duration,\nsysdate+(fj.duration_secs/60/60/24) est_full_revovery_date,\nij.schedule_name ij_schedule_name,\nij.job_id ij_job_id,\nij.nbu_job_id ij_nbu_job_id,\nitapes,\nij.finish_date ij_finish_date,\nDECODE(ijobs.job_count,null,'white','blue') ijobs_count_status,\nnvl(ijobs.job_count,0) ijobs_job_count,\nCASE WHEN ijobs.success >=1\n  THEN\n   CASE WHEN ijobs.failed >= 1\n     THEN 'yellow'\n   WHEN ijobs.failed = 0 \n     THEN 'green'\n  END\n  ELSE 'red'\nEND ijobs_status,\nnvl(ijobs.success,0) success,\nnvl(ijobs.failed,0) failed,\nsysdate+(ijobs.duration_secs/60/60/24) est_incr_revovery_date\nFROM full, incr, apt_v_nbu_job_detail fj, apt_v_nbu_job_detail ij, ftapes, itapes, ijobs\nWHERE full.client_id = incr.client_id (+) \nAND full.policy_id = incr.policy_id (+)\nAND full.client_id = ijobs.client_id (+) \nAND full.job_id = fj.job_id \nAND incr.job_id = ij.job_id\nAND full.job_id = ftapes.job_id \nAND incr.job_id = itapes.job_id"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
