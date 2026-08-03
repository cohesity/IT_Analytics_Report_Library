---
title: "NetBackup Duplicate Copies Details"
report_id: 1295
rtd_name: "NetBackup Duplicate Copies Details.rtd"
description: "Drilldown target of NetBackup Duplicate Copies"
problem_statement: "I want to display details from the NetBackup Duplicate Copies template."
author: "mandar.kulkarni@veritas.com"
modified_date: "2024-07-15"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "SELECT h.hostname Client,\n       j.*\nFROM apt_v_nbu_duplication_job j,\n     apt_v_server h\nWHERE j.target_client_id=h.server_id\n  AND j.finish_date BETWEEN ${startDate} AND ${endDate}\n  AND j.target_client_id IN (${hosts})\n -- AND TRUNC(j.finish_date) = TO_DATE('${the_date_char}')\n  AND TRUNC(j.finish_date) = sysdate\nORDER BY j.target_client_id, j.finish_date"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: [{"slug": "opscenter-reports", "name": "OpsCenter Reports"}]
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: ["opscenter-reports"]
---
