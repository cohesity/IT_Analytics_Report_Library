---
title: "NetApp SnapVault Status Distribution by Attribute"
report_id: 1021
rtd_name: "NetApp SnapVault Status Distribution by Attribute.rtd"
description: "NetApp SnapVault Status Distribution by Attribute"
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
sql_query: "WITH \nt1 AS (\nSELECT\nnvl(rtd.getObjectAttributeValue(src.storage_array_id,'${queryCombo1}','A'),'Unassigned') attribute,\nsc.source_storage_system_id,\nsc.source_system_name,\nsc.source_volume_id,\nsc.source_volume_name,\nsc.source_qtree_id,\nsc.source_qtree_name,\nsc.destination_storage_system_id,\nsc.destination_system_name,\nsc.destination_volume_id,\nsc.destination_volume_name,\nss.nap_snapvault_status_id,\nss.mirror_timestamp,\nsummary_status,\nrtd.secsToHoursMinSecs(ss.lag_time) lag_time\nFROM aps_v_nap_snapvault_status ss, aps_v_nap_snapvault_config sc,\naps_v_storage_array src, aps_v_storage_array dest\nWHERE ss.nap_snapvault_config_id = sc.nap_snapvault_config_id\nAND sc.source_storage_system_id = src.storage_array_id\nAND sc.destination_storage_system_id = dest.storage_array_id\nAND ss.mirror_timestamp BETWEEN ${startDate} AND ${endDate}\nAND ss.summary_status IS NOT NULL\n)\nSELECT\nattribute,\ncount(*) total_snapvaults,\nsum(decode(summary_status,0,1,0)) success,\nsum(decode(summary_status,1,1,0)) partial,\nsum(decode(summary_status,2,1,0)) failed\nFROM t1\nGROUP BY attribute\nORDER BY 2 DESC"
has_explanation: false
products: [{"slug": "capacity-manager-netapp-reports-7-mode", "name": "NetApp Reports (7 Mode)"}]
categories: []
product_slugs: ["capacity-manager-netapp-reports-7-mode"]
category_slugs: []
---
