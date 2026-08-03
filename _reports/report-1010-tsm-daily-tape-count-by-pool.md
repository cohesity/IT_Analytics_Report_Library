---
title: "TSM Daily Tape Count by Pool"
report_id: 1010
rtd_name: "TSM Daily Tape Count by Pool.rtd"
description: "TSM Daily Tape Count by Pool"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nSELECT to_char(poll_date,'MM/DD/YY') poll_date, storage_pool_name,\n    sum(nbr_of_volumes) nbr_of_volumes\n    FROM apt_v_tsm_occupancy_log \n    WHERE client_id IN (${hosts})\n      AND poll_date BETWEEN ${startDate} AND ${endDate}\n    GROUP BY to_char(poll_date,'MM/DD/YY'), storage_pool_name"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
