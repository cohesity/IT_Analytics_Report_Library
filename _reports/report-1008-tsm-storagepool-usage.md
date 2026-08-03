---
title: "TSM Storagepool Usage"
report_id: 1008
rtd_name: "TSM Storagepool Usage.rtd"
description: "TSM Storagepool Usage"
problem_statement: ""
author: "rich.rose@aptare.com \r\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "\n--Author:rich.rose@aptare.com \n--Last Updated:08/27/2012 \nSELECT \ninstance_name,\nstorage_pool_type,\ndevice_class_name,\nclass_type,\nstorage_pool_name,\nest_mbyte_capacity/1024 est_capacity,\nutilization_pct,\nutilization_pct/100 pct_util\nFROM apt_v_tsm_storage_pool\nWHERE est_mbyte_capacity > 0\nORDER BY 7 DESC"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
