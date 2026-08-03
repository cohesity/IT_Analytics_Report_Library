---
title: "HPE 3PAR Host Virtual Volume Tiered Storage"
report_id: 1228
rtd_name: "HP3PAR Host Virtual Volume Tiered Storage.rtd"
description: "HP 3PAR Host Virtual Volume Tiered Storage"
problem_statement: "For hosts attached to 3PAR arrays, show me how much of each tier of storage the host is using"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 08/08/2017\nWITH\nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays,\n${startDate} startDate,\nDECODE('${freeCombo1}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n), \nlu AS (\nSELECT DISTINCT\nhlu.H3P_STORAGE_SYSTEM_ID\n, hlu.SYSTEM_NAME\n, hlu.LOGICAL_UNIT_ID\n, hlu.LOGICAL_UNIT_NAME\n,(NVL(hlu.TIER1_USER_KB,0)+NVL(hlu.TIER2_USER_KB,0)+NVL(hlu.TIER3_USER_KB,0)) total_user_kb\nFROM\nAPS_V_H3P_LOGICAL_UNIT hlu\nWHERE\n(NVL(hlu.TIER1_USER_KB,0)+NVL(hlu.TIER2_USER_KB,0)+NVL(hlu.TIER3_USER_KB,0)) > 0\n),\nt1 AS (\nSELECT\nhlu.LOGICAL_UNIT_ID\n, hlu.TIER1_DSP_NAME \n, hlu.TIER1_ADMIN_KB \n, hlu.TIER1_USER_KB \n, hlu.TIER1_SNAPSHOT_KB \nFROM\nAPS_V_H3P_LOGICAL_UNIT hlu\n),\nt2 AS (\nSELECT DISTINCT \nhlu.LOGICAL_UNIT_ID\n, hlu.LOGICAL_UNIT_NAME\n, hlu.TIER2_DSP_NAME \n, hlu.TIER2_ADMIN_KB \n, hlu.TIER2_USER_KB \n, hlu.TIER2_SNAPSHOT_KB \nFROM\nAPS_V_H3P_LOGICAL_UNIT hlu\n),\nt3 AS (\nSELECT\nhlu.LOGICAL_UNIT_ID\n, hlu.LOGICAL_UNIT_NAME\n, hlu.TIER3_DSP_NAME \n, hlu.TIER3_ADMIN_KB \n, hlu.TIER3_USER_KB \n, hlu.TIER3_SNAPSHOT_KB \nFROM\nAPS_V_H3P_LOGICAL_UNIT hlu\n), \nt4 AS (\nSELECT  \nlu.H3P_STORAGE_SYSTEM_ID\n, lu.SYSTEM_NAME\n, h.host_id\n, h.host_name\n, lu.LOGICAL_UNIT_ID\n, lu.LOGICAL_UNIT_NAME\n, t1.TIER1_DSP_NAME \n, lu.total_user_kb/div_by total_user\n, t1.TIER1_ADMIN_KB/div_by  tier1_admin\n, t1.TIER1_USER_KB/div_by tier1_user\n, t1.tier1_user_kb/lu.total_user_kb t1_user_pct_bar\n, t1.tier1_user_kb/lu.total_user_kb*100 t1_user_pct\n, t1.TIER1_SNAPSHOT_KB/div_by teir1_snapshot\n, t2.TIER2_DSP_NAME \n, t2.TIER2_ADMIN_KB/div_by tier2_admin\n, t2.TIER2_USER_KB/div_by tier2_user\n, t2.tier2_user_kb/lu.total_user_kb t2_user_pct_bar\n, t2.tier2_user_kb/lu.total_user_kb*100 t2_user_pct\n, t2.TIER2_SNAPSHOT_KB/div_by tier2_snapshot\n, t3.TIER3_DSP_NAME \n, t3.TIER3_ADMIN_KB/div_by tier3_admin\n, t3.TIER3_USER_KB/div_by tier3_user\n, t3.tier3_user_kb/lu.total_user_kb t3_user_pct_bar\n, t3.tier3_user_kb/lu.total_user_kb*100 t3_user_pct\n, t3.TIER3_SNAPSHOT_KB/div_by tier3_snapshot\nFROM var, lu, t1, t2, t3, aps_v_storage_path sp, aps_v_host h\nWHERE\nlu.LOGICAL_UNIT_ID = t1.logical_unit_id (+)\nAND lu.LOGICAL_UNIT_ID = t2.logical_unit_id (+)\nAND lu.LOGICAL_UNIT_ID = t3.logical_unit_id (+)\nAND lu.logical_unit_id = sp.logical_unit_id\nAND sp.host_id IN (${hosts})\nAND sp.host_id = h.host_id (+)\nORDER BY h.host_name\n)\nSELECT DISTINCT \nH3P_STORAGE_SYSTEM_ID\n, SYSTEM_NAME\n, host_id\n, host_name\n, LOGICAL_UNIT_ID\n, LOGICAL_UNIT_NAME\n, TIER1_DSP_NAME \n, total_user\n, tier1_user\n, t1_user_pct_bar\n, t1_user_pct\n, TIER2_DSP_NAME \n, tier2_user\n, t2_user_pct_bar\n, t2_user_pct\n, TIER3_DSP_NAME \n, tier3_user\n, t3_user_pct_bar\n, t3_user_pct\nFROM t4\nORDER BY host_name"
has_explanation: false
products: [{"slug": "capacity-manager-hpe-3par", "name": "HPE 3PAR"}]
categories: []
product_slugs: ["capacity-manager-hpe-3par"]
category_slugs: []
---
