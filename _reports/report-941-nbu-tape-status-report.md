---
title: "NBU Tape Status Report"
report_id: 941
rtd_name: "NBU Tape Status Report.rtd"
description: "NBU Tape Status Report"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nSELECT \nntm.server_id,\ns.hostname as \"master server\",\nnvl(tl.library_id,999) library_id,\nnvl(tl.library_name,'Outside Library') library_name,\ncount(ntm.tape_media_id) total_tapes,\nsum(DECODE(ntm.vendor_media_status, '1',1,0)) Available,\nsum(DECODE(ntm.vendor_media_status, '2',1,0)) Assigned,\nsum(DECODE(ntm.vendor_media_status, '3',1,0)) Frozen,\nsum(DECODE(ntm.vendor_media_status, '4',1,0)) Suspended,\nsum(DECODE(ntm.vendor_media_status, '5',1,0)) Imported,\nsum(DECODE(ntm.vendor_media_status, '6',1,0)) Full,\nsum(DECODE(ntm.vendor_media_status, '7',1,0)) Expired,\nsum(DECODE(ntm.vendor_media_status, '8',1,0)) Catalog,\nsum(DECODE(ntm.vendor_media_status, '9',1,0)) Cleaning,\nsum(DECODE(ntm.vendor_media_status, '0',1,0)) Unknown\nFROM apt_v_nbu_tape_media ntm,apt_v_server s,apt_v_tape_library tl\nWHERE ntm.server_id = s.server_id\nAND ntm.server_id = DECODE(${queryCombo1},999,ntm.server_id,${queryCombo1})\nAND ntm.library_id = tl.library_id (+)\nAND '${freeCombo1}' IN \n  CASE \n    WHEN '${freeCombo1}' NOT IN ('All') THEN\n      CASE\n        WHEN tl.library_name IS NULL THEN 'Outside Library'\n        WHEN tl.library_name LIKE '%#0%' THEN '#0'\n        WHEN tl.library_name LIKE '%#1%' THEN '#1'\n        WHEN tl.library_name LIKE '%#2%' THEN '#2'\n        WHEN tl.library_name LIKE '%#3%' THEN '#3'\n        WHEN tl.library_name LIKE '%#4%' THEN '#4'\n      END\n   ELSE 'All'\n END\nGROUP BY\nntm.server_id,\ns.hostname,\nnvl(tl.library_id,999),\nnvl(tl.library_name,'Outside Library')"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
