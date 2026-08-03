---
title: "D.NBU Tape Status Report"
report_id: 1086
rtd_name: "NBU Tape Status Report.D.rtd"
description: "NBU Tape Status Report"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "SELECT \ns.hostname as \"master server\",\nnvl(tl.library_name,'Outside Library') library_name,\nntm.media_name as \"Barcode\",\nDECODE(ntm.vendor_media_status, \n1,'Available',\n2,'Assigned',\n3,'Frozen',\n4,'Suspended',\n5,'Imported',\n6,'Full',\n7,'Expired',\n8,'Catalog',\n9,'Cleaning',\n0,'Unknown') media_status_name,\nnvp.volume_pool_name as \"volume pool\",\nnvg.volume_group_name as \"volume group\",\n'${the_expiration}' as \"expiration\",\nntm.date_created as \"Date Created\",\nntm.date_assigned as \"Date Assigned\",\nntm.last_mounted as \"Last Mounted\",\nntm.last_written as \"Last Written\",\nntm.last_read as \"Last Read\",\nntm.expiration_date as \"Expiration Date\",\nntm.tape_media_id as \"tape_id\"\nFROM apt_v_nbu_tape_media ntm, apt_v_server s, apt_v_nbu_volume_pool nvp, \napt_v_tape_library tl, apt_v_nbu_volume_group nvg\nWHERE ntm.server_id = s.server_id\nAND ntm.library_id = tl.library_id(+)\nAND ntm.server_id = ${the_server_id}\nAND nvl(ntm.library_id,999) = ${the_library_id}\nAND ntm.vendor_media_status = ${the_status}\nAND ntm.volume_pool_id = nvp.volume_pool_id (+)\nAND ntm.volume_group_id = nvg.volume_group_id (+)"
has_explanation: false
products: []
categories: []
product_slugs: []
category_slugs: []
---
