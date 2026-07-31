---
title: "NetApp Volume Day-Over-Day Usage Rate Comparison"
report_id: 1144
rtd_name: "NetApp Volume Day-Over-Day Usage Rate Comparison.rtd"
description: "NetApp Volume Day-Over-Day Usage Rate Comparison"
problem_statement: "I need a way to identify which of my NetApp Volumes are changing the most so I can determine the best method of data protection."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/30/2015\nWITH \nvar AS (\nSELECT\n'${freeCombo1}' unit,\nDECODE('${freeCombo1}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by,\nDECODE('${freeCombo2}','5%',5,'10%',10,'20%',20,'30%',30,'40%',40,'50%',50,'60%',60,'70%',70,'80%',80,'90%',90,'100%',100) threshold\nFROM apt_v_dual\n),\nt1 AS (\nSELECT\nvl.system_name,\nvl.nap_volume_id,\nvl.volume_name,\nTO_CHAR(TRUNC(vl.log_date),'YYYY/MM/DD') log_date,\nMAX(vl.available_size_kb/div_by) available_size\nFROM aps_v_nap_volume_log vl, aps_v_nap_storage_system ns, var\nWHERE vl.log_date BETWEEN ${startDate} AND ${endDate}\nAND vl.system_name = ns.system_name\nAND ns.system_name LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\nGROUP BY\nvl.system_name,\nvl.nap_volume_id,\nvl.volume_name,\nTO_CHAR(TRUNC(vl.log_date),'YYYY/MM/DD')\nORDER BY 1,2,3,4\n), \nt2 AS (\nSELECT\nsystem_name,\nnap_volume_id,\nvolume_name,\nlog_date,\navailable_size,\nLAG(available_size, 1, 0) OVER (PARTITION BY system_name, nap_volume_id, volume_name ORDER BY system_name, nap_volume_id, volume_name, log_date) prev_available_size\nFROM t1\n),\nt3 AS (\nSELECT\nlog_date,\nsystem_name||' - '||volume_name system_volume,\nROUND(available_size,2) available_size,\nROUND((available_size - prev_available_size),2) available_delta,\nROUND((available_size - prev_available_size)/DECODE(available_size,0,null,available_size)*100,2) available_pct_change\nFROM t2\n)\nSELECT\nlog_date,\nsystem_volume,\nCASE \n  WHEN ABS(available_pct_change) > var.threshold THEN \n    CASE \n    WHEN available_delta < 0 THEN '<font color=red>'||available_size||'</font>'\n    WHEN available_delta > 0 THEN '<font color=green>'||available_size||'</font>'\n   END\n  ELSE '<font color=blue>'||available_size||'</font>'\nEND available_size_char,\navailable_size,\navailable_delta,\navailable_pct_change,\nCASE \n  WHEN available_delta < 0 THEN 'Decreased'\n  WHEN available_delta > 0 THEN 'Increased'\nEND i_or_d,\nunit\nFROM t3, var\nORDER BY 1 DESC, 2"
has_explanation: false
products: [{"slug": "capacity-manager-netapp-reports-7-mode", "name": "NetApp Reports (7 Mode)"}]
categories: []
product_slugs: ["capacity-manager-netapp-reports-7-mode"]
category_slugs: []
---
