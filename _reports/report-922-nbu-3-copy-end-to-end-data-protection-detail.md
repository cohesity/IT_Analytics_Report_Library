---
title: "NBU 3 Copy End To End Data Protection Detail"
report_id: 922
rtd_name: "NBU 3 Copy End to End Data Protection Detail.rtd"
description: "NBU 3 Copy End to End Data Protection Detail"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 11/02/2012\nWITH \nt1 AS (\nSELECT job_id\nFROM apt_v_nbu_job_detail\nWHERE nbr_of_copies = ${freeCombo1}\nAND client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\n\n),\nt2 AS (--copies\nSELECT\njdm.job_id,\n'Disk' the_source,\njdm.copy_index,\njdm.written_kilobytes kilobytes,\njdm.expiration_date\nFROM t1, apt_v_nbu_job_disk_media jdm\nWHERE t1.job_id = jdm.job_id\nUNION ALL\nSELECT\njtm.job_id,\n'Tape' the_source,\njtm.copy_index,\njtm.kilobytes kilobytes,\njtm.expiration_date\nFROM t1, apt_v_nbu_job_tape_media jtm\nWHERE t1.job_id = jtm.job_id\n),\nt3 AS (\nSELECT\nnjd.job_id,\nnjd.server_id,\nnjd.master_host_name,\nnjd.client_id,\nnjd.client_host_name,\nDECODE(copy_index,1,t2.copy_index) copy_index1,\nDECODE(copy_index,1,t2.the_source) the_source1,\nDECODE(copy_index,1,t2.kilobytes) kilobytes1,\nDECODE(copy_index,1,t2.expiration_date) expiration_date1,\nDECODE(copy_index,2,t2.copy_index) copy_index2,\nDECODE(copy_index,2,t2.the_source) the_source2,\nDECODE(copy_index,2,t2.kilobytes) kilobytes2,\nDECODE(copy_index,2,t2.expiration_date) expiration_date2,\nDECODE(copy_index,3,t2.copy_index) copy_index3,\nDECODE(copy_index,3,t2.the_source) the_source3,\nDECODE(copy_index,3,t2.kilobytes) kilobytes3,\nDECODE(copy_index,3,t2.expiration_date) expiration_date3\nFROM t2,apt_v_nbu_job_detail njd\nWHERE t2.job_id = njd.job_id\n)\nSELECT\njob_id,\nserver_id,\nmaster_host_name,\nclient_id,\nclient_host_name,\nMAX(copy_index1) copy_index1,\nMAX(the_source1) the_source1,\nSUM(kilobytes1/1024/1024) size1,\nMAX(expiration_date1) expiration_date1, \nCASE WHEN MAX(expiration_date1) <= sysdate THEN 'yellow' ELSE 'green' END date1_dot,\nMAX(copy_index2) copy_index2,\nMAX(the_source2) the_source2,\nSUM(kilobytes2/1024/1024) size2,\nMAX(expiration_date2) expiration_date2,\nCASE WHEN MAX(expiration_date2) <= sysdate THEN 'yellow' ELSE 'green' END date2_dot,\nMAX(copy_index3) copy_index3,\nMAX(the_source3) the_source3,\nSUM(kilobytes3/1024/1024) size3,\nMAX(expiration_date3) expiration_date3,\nCASE WHEN MAX(expiration_date3) <= sysdate THEN 'yellow' ELSE 'green' END date3_dot\nFROM t3\nGROUP BY\njob_id,\nserver_id,\nmaster_host_name,\nclient_id,\nclient_host_name"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
