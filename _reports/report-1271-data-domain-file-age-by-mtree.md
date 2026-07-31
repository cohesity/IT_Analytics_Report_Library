---
title: "Data Domain File Age by MTree"
report_id: 1271
rtd_name: "Data Domain File Age by MTree.rtd"
description: "Data Domain File Age by MTree"
problem_statement: "I need a report which can help me quickly identify large data sets that have been on the Data Domain for a long time so I can potentially move it onto something cheaper."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: Muhammad.Tahir@veritas.com\n--Last Modified 03/31/2020\nWITH \nVAR AS (\nSELECT\n  DECODE('${freeCombo1}',\n  'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\nt1 AS ( \nSELECT\n  mtree_id,\n  SUBSTR(mtree_name,12) mtree_name,\n  ROUND(SUM(local_comp_kb/div_by),2) total_size,\n  ROUND(SUM(CASE WHEN file_modified_date > sysdate-1 THEN local_comp_kb/div_by END),2) one_day,\n  ROUND(SUM(CASE WHEN file_modified_date BETWEEN sysdate-7 AND sysdate-2 THEN local_comp_kb/div_by END),2) bt_2_and_7,\n  ROUND(SUM(CASE WHEN file_modified_date BETWEEN sysdate-14 AND sysdate-7 THEN local_comp_kb/div_by END),2) bt_7_and_14,\n  ROUND(SUM(CASE WHEN file_modified_date BETWEEN sysdate-30 AND sysdate-14 THEN local_comp_kb/div_by END),2) bt_14_and_30,\n  ROUND(SUM(CASE WHEN file_modified_date BETWEEN sysdate-60 AND sysdate-30 THEN local_comp_kb/div_by END),2) bt_30_and_60,\n  ROUND(SUM(CASE WHEN file_modified_date BETWEEN sysdate-90 AND sysdate-60 THEN local_comp_kb/div_by END),2) bt_60_and_90,\n  ROUND(SUM(CASE WHEN file_modified_date BETWEEN sysdate-180 AND sysdate-90 THEN local_comp_kb/div_by END),2) bt_90_and_180,\n  ROUND(SUM(CASE WHEN file_modified_date BETWEEN sysdate-365 AND sysdate-180 THEN local_comp_kb/div_by END),2) bt_180_and_365,\n  ROUND(SUM(CASE WHEN file_modified_date < sysdate-366 THEN local_comp_kb/div_by END),2) over_1yr\nFROM \n  apt_v_ddm_file_level_comp, var\nWHERE\n  ddm_host_id IN (${hosts})\nGROUP BY\n  mtree_id,\n  mtree_name\nORDER BY\n  total_size DESC\n)\nSELECT * \nFROM t1 \nWHERE rownum <= ${freeCombo2}"
has_explanation: false
products: [{"slug": "backup-manager-emc-data-domain", "name": "EMC Data Domain"}]
categories: []
product_slugs: ["backup-manager-emc-data-domain"]
category_slugs: []
---
