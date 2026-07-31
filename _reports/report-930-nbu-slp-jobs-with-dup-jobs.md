---
title: "NBU SLP Jobs with Dup Jobs"
report_id: 930
rtd_name: "NBU SLP Jobs with Dup Jobs.rtd"
description: "NBU SLP Jobs with Dup Jobs"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 05/07/1012\nWITH t1 as ( --If the path is an image then it's a dup Job\nSELECT jf.pathname image_id\nFROM  apt_v_nbu_job_file jf, apt_v_nbu_job j\nWHERE jf.pathname = j.backup_id\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.client_id IN (${hosts})\n),\nt2 as ( --The base job\nSELECT j.job_id, j.backup_id,j.nbu_job_id backup_nbu_job_id, j.master_host_name,\nj.client_id,j.client_host_name backup_client,\nj.policy_id,j.policy_name,\nj.schedule_name,j.job_type_name,j.kilobytes/1024 data_mb,\nj.nbr_of_files, j.mbytes_sec,\nj.start_date backup_start_date,\nj.finish_date backup_end_date,\nj.expiration_date backup_expiration, j.storage_unit_label backup_storage_unit\nFROM apt_v_nbu_job_detail j,t1\nWHERE j.backup_id = t1.image_id\n),\nt3 as ( --The Dup Job\nSELECT jf.job_id,j.nbu_job_id dup_nbu_job_id, jf.pathname, \nj.client_id dup_client, \nnp.policy_id dup_job_policy_id, \nnp.policy_name dup_job_policy_name, \nnp.lifecycle_policy_name,\nsu.storage_unit_label dup_storage_unit,\nj.start_date dup_start_date, \nj.finish_date dup_end_date, \nj.vendor_state_name state\nFROM  apt_v_nbu_job_file jf, t1, apt_v_nbu_job j, apt_v_nbu_policy np, apt_v_nbu_storage_unit su\nWHERE jf.pathname = t1.image_id\nAND jf.job_id = j.job_id\nAND j.policy_id = np.policy_id\nAND j.storage_unit_id = su.storage_unit_id (+)\n) \nSELECT \nt2.job_id backup_job_id, backup_nbu_job_id, \nt2.master_host_name, \nt2.client_id,t2.backup_client,\nt2.policy_id, t2.policy_name, \nt2.schedule_name, t2.job_type_name, \nt2.backup_expiration, t2.backup_id,  backup_storage_unit, \nbackup_start_date, backup_end_date,\nt2.data_mb,\nt2.nbr_of_files, t2.mbytes_sec,\nt3.job_id dup_job_id, dup_nbu_job_id, t3.dup_client, \nt3.dup_job_policy_id, t3.dup_job_policy_name,t3.lifecycle_policy_name,\nt3.dup_storage_unit,\nt3.dup_start_date, t3.dup_end_date, \nrtd.secsToHoursMinSecs((t3.dup_start_date - t2.backup_end_date)*24*60*60) elapsed_since_bkup, \nt3.state,\njtm.copy_index, jtm.expiration_date dup_expiration_date\nFROM t2,t3,apt_v_nbu_job_tape_media jtm\nWHERE t2.backup_id = t3.pathname\nAND t2.job_id = jtm.job_id"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
