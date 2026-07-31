---
title: "TSM Tape Status Summary"
report_id: 1003
rtd_name: "TSM Tape Status Summary.rtd"
description: "TSM Tape Status Summary"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "SELECT ttm.library_name, ttm.server_host_name,\n       ttm.media_status_name, \n       COUNT(DISTINCT ttm.tape_media_id) nbr_of_tapes\n    FROM apt_v_tsm_tape_media ttm\n    WHERE ttm.server_id IN (${hosts})\n    GROUP BY ttm.library_name, ttm.server_host_name, ttm.media_status_name\n    ORDER BY Upper(ttm.server_host_name), UPPER(ttm.library_name)"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
