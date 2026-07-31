---
title: "NBU Tape Error Summary"
report_id: 925
rtd_name: "NBU Tape Error Summary.rtd"
description: "NBU Tape Error Summary"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "WITH \nt1 AS (\nSELECT \n  s.server_id, s.hostname, m.tape_media_id, m.media_name, \n  mn.nbr_of_mounts, mn.nbr_of_restores,\n  COUNT(DISTINCT jm.job_id) error_count,\n  MIN(j.finish_date) min_finish_time,\n  MAX(j.finish_date) max_finish_time\nFROM apt_v_job j, apt_v_job_message_log l, apt_v_job_tape_media jm, apt_v_tape_media m, apt_v_nbu_tape_media mn, apt_v_server s\nWHERE j.client_id IN (${hosts})\n  AND j.finish_date BETWEEN ${startDate} AND ${endDate}\n  AND j.job_id = l.job_id\n  AND (Instr(l.message, 'media write error') > 0 OR Instr(l.message, 'media read error') > 0)\n  AND j.job_id = jm.job_id\n  AND jm.tape_media_id = m.tape_media_id\n  AND m.tape_media_id = mn.tape_media_id\n  AND j.server_id = s.server_id\nGROUP BY s.server_id, s.hostname, m.tape_media_id, m.media_name, mn.nbr_of_mounts, mn.nbr_of_restores\n)\nSELECT\n  t1.server_id, t1.hostname, t1.tape_media_id, t1.media_name, d.drive_name, t1.nbr_of_mounts,\n  t1.error_count, t1.min_finish_time, t1.max_finish_time,t1.nbr_of_restores, \nCOUNT(DISTINCT jm.job_id) count_events\nFROM t1, apt_v_job_tape_media jm, apt_v_tape_drive d, apt_v_job j, apt_v_nbu_job jn\nWHERE t1.tape_media_id = jm.tape_media_id\n  AND jm.job_id = j.job_id\n  AND jm.drive_id = d.drive_id(+)\n  AND j.job_id  = jn.job_id\n  AND j.summary_status IN (0,1)\n  AND jn.expiration_date >= SYSDATE\nGROUP BY t1.server_id, t1.hostname, t1.tape_media_id, t1.media_name, d.drive_name, t1.nbr_of_mounts, \n  nbr_of_restores, t1.error_count, t1.min_finish_time, t1.max_finish_time\nORDER BY t1.error_count DESC, t1.server_id, Upper(t1.media_name)"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
