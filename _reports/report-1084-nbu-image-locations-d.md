---
title: "NBU Image Locations.D"
report_id: 1084
rtd_name: "NBU Image Locations.D.rtd"
description: "NBU Image Locations"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/20/2012\n--Drilldown templateName is: NBUImageLocations.D\nWITH t1 as (\nSELECT t.copy_index, 'Tape' media_type, t.tape_media_id media_id, m.media_name, \njtm.kilobytes written_kilobytes, t.expired_copy, \nt.expiration_date, g.volume_group_name,j.backup_id\nFROM\napt_v_nbu_job j,\napt_v_job_tape_media jtm,\napt_v_nbu_job_tape_media t,\napt_v_tape_media m,\napt_v_nbu_tape_media mn,\napt_v_nbu_volume_group g\nWHERE jtm.job_id = j.job_id\nAND j.backup_id = '${BackupID}'\nAND jtm.job_id  = t.job_id\nAND j.client_id IN (${hosts})\nAND jtm.tape_media_id  = t.tape_media_id\nAND t.tape_media_id    = m.tape_media_id\nAND m.tape_media_id    = mn.tape_media_id\nAND mn.volume_group_id = g.volume_group_id(+)\nUNION\nSELECT d.copy_index, 'Disk' media_type, NULL media_id, 'Disk Path' media_name, \nd.written_kilobytes, d.expired_copy, d.expiration_date, NULL volume_group_name,j.backup_id\nFROM apt_v_nbu_job j, apt_v_nbu_job_disk_media d\nWHERE d.job_id = j.job_id\nAND j.backup_id = '${BackupID}'\nAND j.client_id IN (${hosts})\n)\nSELECT t1.*,\n(SELECT count(backup_id) FROM apt_v_nbu_image_log WHERE backup_id = '${BackupID}' ) image_logs\nFROM t1"
has_explanation: false
products: []
categories: []
product_slugs: []
category_slugs: []
---
