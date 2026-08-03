---
title: "TSM Node Count by Software Version"
report_id: 1111
rtd_name: "TSM Node Count by Software Version.rtd"
description: "TSM Node Count by Software Version"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "SELECT \nnvl(client_software_version,'??nknown') client_version,\ncount(*) client_count\nFROM apt_v_tsm_node\nWHERE client_id IN (${hosts})\nGROUP BY nvl(client_software_version,'??nknown')\nORDER BY 2 DESC"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
