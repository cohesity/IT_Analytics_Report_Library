---
title: "CommVault Tape Media Lookup"
report_id: 1243
rtd_name: "CommVault Tape Media Lookup.rtd"
description: "CommVault Tape Media Lookup"
problem_statement: "I need to be able to lookup tapes whic may be gone from CommVault's database but still have active data on them that I may need to recall and restore from."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified:09/19/2018\nWITH \nvar AS (\nSELECT\nDECODE('${freeCombo1}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n)\nSELECT\nsi.host_name,\nsi.display_name server,\nct.bar_code,\nct.cmv_tape_media_id_ext,\nct.tape_media_id,\nct.media_name,\nct.server_instance_id,\nct.slot_name,\nct.slot_type,\nct.media_type,\nct.media_vendor_type,\nct.cmv_current_drive_id,\ntm.media_status_name,\nct.cmv_media_status,\nct.media_location,\nct.export_location,\nct.block_size_kb,\nct.total_space_kb/div_by total_space,\nct.used_space_kb/div_by used_space,\nct.free_space_kb/div_by free_space,\nct.nbr_sides,\nct.nbr_backups,\nct.nbr_restores,\nct.nbr_reuse,\nct.nbr_soft_errors,\nct.nbr_hard_errors,\nct.media_creation_time,\nct.last_backup_time,\nct.last_restore_time,\nct.last_export_time,\nct.last_updated\nFROM \napt_v_cmv_tape_media ct, apt_v_tape_media tm, apt_v_server_instance si, var\nWHERE \nct.tape_media_id = tm.tape_media_id\nAND si.server_id IN (${hosts})\nAND ct.server_instance_id = si.server_instance_id (+)\nAND REGEXP_LIKE(ct.bar_code,'${freeText1}')"
has_explanation: false
products: [{"slug": "backup-manager-commvault", "name": "CommVault"}]
categories: []
product_slugs: ["backup-manager-commvault"]
category_slugs: []
---
