---
title: "NBU Disk Volume and Pool Available Capacity Pivot"
report_id: 1155
rtd_name: "NBU Disk Volume and Pool Available Capacity Pivot.rtd"
description: "NBU Disk Pool Available Capacity Pivot"
problem_statement: ""
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 08/28/2015\nWITH\nvar AS (\nSELECT\n'${freeCombo2}' unit,\nDECODE('${freeCombo2}','KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by,\nDECODE('${freeCombo3}','5%',5,'10%',10,'20%',20,'30%',30,'40%',40,'50%',50,'60%',60,'70%',70,'80%',80,'90%',90,'100%',100) threshold \nFROM apt_v_dual\n),\nt1 AS (\nSELECT\nto_char(trunc(vl.log_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY') log_date,\nto_char(trunc(vl.log_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24MI') sort_order,\ns.display_name||' > '||vl.disk_volume_name||' > '||dp.disk_pool_name server_volume_pool, \nROUND(MAX(vl.free_space_kb/div_by),2) free_space\nFROM apt_v_nbu_disk_volume_log vl, apt_v_nbu_disk_pool dp, apt_v_server s, var\nWHERE\nvl.management_server_id IN (${hosts})\nAND vl.management_server_id = s.server_id\nAND vl.disk_pool_id = dp.disk_pool_id\nAND vl.log_date BETWEEN ${startDate} AND  ${endDate}\nGROUP BY \nto_char(trunc(vl.log_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY'),\nto_char(trunc(vl.log_date,DECODE('${freeCombo1}','Minute','MI','Hour','HH24','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'YYYYMMDDHH24MI'),\ns.display_name||' > '||vl.disk_volume_name||' > '||dp.disk_pool_name\n),\nt2 AS (\nSELECT\nlog_date,\nsort_order,\nserver_volume_pool,\nfree_space,\nLAG(free_space, 1, 0) OVER (PARTITION BY server_volume_pool ORDER BY server_volume_pool, log_date) prev_free_space\nFROM t1\n),\nt3 AS (\nSELECT\nlog_date,\nsort_order,\nserver_volume_pool,\nfree_space,\nROUND((free_space - prev_free_space),2) free_delta,\nROUND((free_space - prev_free_space)/DECODE(free_space,0,null,free_space)*100,2) free_pct_change\nFROM t2\n)\nSELECT\nlog_date,\nserver_volume_pool,\nCASE \n  WHEN ABS(free_pct_change) > var.threshold THEN \n    CASE \n    WHEN free_delta < 0 THEN '<font color=red>'||free_space||' '||unit||'</font>'\n    WHEN free_delta > 0 THEN '<font color=green>'||free_space||' '||unit||'</font>'\n   END\n  ELSE '<font color=blue>'||free_space||' '||unit||'</font>'\nEND free_space_char,\nfree_space,\nfree_delta,\nfree_pct_change,\nCASE \n  WHEN free_delta < 0 THEN 'Decreased'\n  WHEN free_delta > 0 THEN 'Increased'\nEND i_or_d,\nunit\nFROM t3, var\nORDER BY 1 DESC, 2"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
