---
title: "Tape Drive Activity and Idle Time"
report_id: 891
rtd_name: "Tape Drive Activity and Idle Time.rtd"
description: "Tape Drive Activity and Idle Time"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 08/27/2012\nWITH \nd0 as (\nSELECT (${endDate} - ${startDate})*24 nbr_of_hrs\nFROM apt_v_dual\n),\nt1 as (\nSELECT \ntd.management_server_name, \ntd.controlling_server_name,\ntd.library_id,\ntd.library_name, \ntd.drive_id,\ntd.drive_name, \nsum(DECODE(tdl.in_use,'Y',1,0)) in_use,\nsum(DECODE(tdl.in_use,'N',1,0)) not_in_use\nFROM apt_v_tape_drive td, apt_v_tape_drive_log tdl\nWHERE td.drive_id = tdl.drive_id \nAND tdl.poll_time BETWEEN ${startDate} AND ${endDate}\nAND td.management_server_id IN (${hosts}) \nGROUP BY  td.management_server_name, td.controlling_server_name,\ntd.library_id,td.library_name, td.drive_id, td.drive_name \n),\nt2 as (\nSELECT\nmanagement_server_name, \ncontrolling_server_name,\nlibrary_id,library_name, \ndrive_id, drive_name, \nin_use,not_in_use,\nin_use+not_in_use nbr_of_samples,\nDECODE(not_in_use,0,null,not_in_use)/DECODE((in_use+not_in_use),0,null,(in_use+not_in_use))*100 not_in_use_pct\nFROM t1\n)\nSELECT management_server_name, controlling_server_name,library_id,library_name, drive_id, drive_name, \nin_use,not_in_use,\nnot_in_use_pct,\nnbr_of_hrs,\nnbr_of_samples,\nnbr_of_samples/nbr_of_hrs samples_hr,\n(not_in_use_pct/100)*nbr_of_hrs available_hours,\nrtd.secsToHoursMinSecs((not_in_use_pct/100)*nbr_of_hrs*60*60) idle_time\nFROM t2,d0\nORDER by 1,2,4,5"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
