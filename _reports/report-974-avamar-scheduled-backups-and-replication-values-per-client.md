---
title: "Avamar Scheduled Backups and Replication Values per Client"
report_id: 974
rtd_name: "Avamar Scheduled Backups and Replication Values per Client.rtd"
description: "Avamar Scheduled Backups and Replication Values per Client"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Updated: 08/20/2012\nWITH \nt1 AS (--Get the scanned values\nSELECT \ngsan_system_id,gsan_system_name,client_name,\nCOUNT(job_id) job_count,\nCOUNT(DECODE(job_type_name,'Scheduled Backup',job_id,null)) sb_job_count,\nMAX(DECODE(job_type_name,'Scheduled Backup',scanned_kb,0)/1024/1024) sb_MAX_scanned_gb,\nAVG(DECODE(job_type_name,'Scheduled Backup',scanned_kb,0)/1024/1024) sb_AVG_scanned_gb,\nCOUNT(DECODE(job_type_name,'Replication Source',job_id,null)) rs_job_count,\nMAX(DECODE(job_type_name,'Replication Source',scanned_kb,0)/1024/1024) rs_MAX_scanned_gb,\nAVG(DECODE(job_type_name,'Replication Source',scanned_kb,0)/1024/1024) rs_AVG_scanned_gb\nFROM apt_v_avm_activities\nWHERE \ngsan_system_name = '${queryCombo1}'\nAND scanned_kb > 0\nAND recorded_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY gsan_system_id,gsan_system_name,client_name\n),\nt2 AS (--Get the totals\nSELECT\ngsan_system_id,\nSUM(sb_job_count) tot_sb_job_count,\nSUM(sb_MAX_scanned_gb) tot_sb_MAX_scanned_gb,\nSUM(sb_AVG_scanned_gb) tot_sb_AVG_scanned_gb,\nSUM(rs_job_count) tot_rs_job_count,\nSUM(rs_MAX_scanned_gb) tot_rs_MAX_scanned_gb,\nSUM(rs_AVG_scanned_gb) tot_rs_AVG_scanned_gb\nFROM t1\nGROUP BY gsan_system_id\n),\nT3 AS (\nSELECT \nt1.gsan_system_id,t1.gsan_system_name,client_name,\nsb_job_count,\nsb_MAX_scanned_gb,\nsb_AVG_scanned_gb,\nROUND(sb_job_count/tot_sb_job_count*100,4) sb_pct_total_jobs,\nROUND(sb_MAX_scanned_gb/tot_sb_MAX_scanned_gb*100,4) sb_pct_MAX_scanned_gb,\nROUND(sb_AVG_scanned_gb/tot_sb_AVG_scanned_gb*100,4) sb_pct_AVG_scanned_gb,\nrs_job_count,\nrs_MAX_scanned_gb,\nrs_AVG_scanned_gb,\nROUND(rs_job_count/tot_rs_job_count*100,4) rs_pct_total_jobs,\nROUND(rs_MAX_scanned_gb/tot_rs_MAX_scanned_gb*100,4) rs_pct_MAX_scanned_gb,\nROUND(rs_AVG_scanned_gb/tot_rs_AVG_scanned_gb*100,4) rs_pct_AVG_scanned_gb\nFROM t1,t2\nWHERE t1.gsan_system_id = t2.gsan_system_id\n)\nSELECT \nt3.gsan_system_id,t3.gsan_system_name,\nt3.client_name,\nt3.sb_job_count,\nt3.sb_MAX_scanned_gb,\nt3.sb_AVG_scanned_gb,\nt3.sb_pct_total_jobs,\nt3.sb_pct_MAX_scanned_gb,\nt3.sb_pct_AVG_scanned_gb,\nt3.rs_job_count,\nt3.rs_MAX_scanned_gb,\nt3.rs_AVG_scanned_gb,\nt3.rs_pct_total_jobs,\nt3.rs_pct_MAX_scanned_gb,\nt3.rs_pct_AVG_scanned_gb\nFROM T3"
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
