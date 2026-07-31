---
title: "NetApp SnapMirror Detailed Status.D"
report_id: 1083
rtd_name: "NetApp SnapMirror Detailed Status.D.rtd"
description: "NetApp SnapMirror Detailed Status"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 06/12/2012\nSELECT\nnvl(rtd.getObjectAttributeValue(src.storage_array_id,'${queryCombo1}','A'),'Unassigned') Attribute,\nsc.source_storage_system_id,\nsc.source_system_name,\nsc.source_volume_id,\nsc.source_volume_name,\nsc.source_qtree_id,\nsc.source_qtree_name,\nsc.destination_storage_system_id,\nsc.destination_system_name,\nsc.destination_volume_id,\nsc.destination_volume_name,\nss.nap_snapmirror_status_id,\nss.mirror_timestamp,\nDECODE(ss.summary_status,0,'blue',1,'yellow',2,'red') summary_status,\nrtd.secsToHoursMinSecs(ss.lag_time) lag_time\nFROM aps_v_nap_snapmirror_status ss, aps_v_nap_snapmirror_schd sc,\naps_v_storage_array src, aps_v_storage_array dest\nWHERE ss.nap_snapmirror_schd_id = sc.nap_snapmirror_schd_id\nAND sc.source_storage_system_id = src.storage_array_id\nAND sc.destination_storage_system_id = dest.storage_array_id\nAND ss.mirror_timestamp BETWEEN ${startDate} AND ${endDate}\nAND ss.summary_status = ${the_status}\nAND nvl(rtd.getObjectAttributeValue(src.storage_array_id,'${queryCombo1}','A'),'Unassigned') = '${the_attribute}'"
has_explanation: false
products: []
categories: []
product_slugs: []
category_slugs: []
---
