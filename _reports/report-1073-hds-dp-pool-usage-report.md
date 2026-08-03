---
title: "HDS DP Pool Usage Report"
report_id: 1073
rtd_name: "HDS DP Pool Usage Report.rtd"
description: "HDS DP Array Pool Usage Summary"
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
sql_query: "--Author:rich.rose@aptare.com\n--Last Modified: 09/10/2015\nWITH\nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays, \n${startDate} startDate, \n'${freeCombo1}' unit,\nDECODE('${freeCombo1}', 'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual \n)\nSELECT\nstorage_array_id,\narray_name,\npool_id,\nNVL(pool_name,'DP '||pool_id) pool_name, \ncapacity_kb/div_by capacity,\nfree_capacity_kb/div_by free_capacity,\n(capacity_kb - free_capacity_kb)/div_by touched,\nROUND((capacity_kb - free_capacity_kb)/capacity_kb*100) pct_touched,\n(capacity_kb - free_capacity_kb)/capacity_kb touched_pct,\nthreshold,\nCASE WHEN ((capacity_kb - free_capacity_kb)/capacity_kb*100) >= threshold THEN 'red' ELSE 'green' END t1_dot,\nCASE WHEN ((capacity_kb - free_capacity_kb)/capacity_kb*100) >= threshold THEN 'Exceeds' ELSE 'Less Than' END t1_message,\nthreshold2,\nCASE WHEN ((capacity_kb - free_capacity_kb)/capacity_kb*100) >= threshold2 THEN 'red' ELSE 'green' END t2_dot,\nCASE WHEN ((capacity_kb - free_capacity_kb)/capacity_kb*100) >= threshold2 THEN 'Exceeds' ELSE 'Less Than' END t2_message,\ncapacity_of_vvols_kb/div_by capacity_of_vvols,\n((capacity_kb-capacity_of_vvols_kb)/div_by)*-1 provisioned,\nCASE WHEN (capacity_of_vvols_kb/capacity_kb*100) > 100 \nTHEN '<font color=red>'||ROUND((capacity_of_vvols_kb/capacity_kb*100))||'%'\nELSE '<font color=green>'||ROUND((capacity_of_vvols_kb/capacity_kb*100))||'%'\nEND prov_pct,\n--usage_rate,\nDECODE(threshold_vol_forewarn,-1,null,threshold_vol_forewarn) threshold_vol_forewarn,\nCASE \nWHEN threshold_vol_forewarn = -1 THEN 'white'\nWHEN ROUND((capacity_of_vvols_kb/capacity_kb*100)) >= threshold_vol_forewarn THEN 'red' \nWHEN ROUND((capacity_of_vvols_kb/capacity_kb*100)) BETWEEN 0 AND threshold_vol_forewarn THEN 'green' \nELSE 'blue' END fore_dot,\nDECODE(threshold_vol_overwarn,-1,null,threshold_vol_overwarn) threshold_vol_overwarn,\nCASE \nWHEN threshold_vol_overwarn = -1 THEN 'white'\nWHEN ROUND((capacity_of_vvols_kb/capacity_kb*100)) >= threshold_vol_overwarn THEN 'red' \nWHEN ROUND((capacity_of_vvols_kb/capacity_kb*100)) BETWEEN 0 AND threshold_vol_overwarn THEN 'green' \nELSE 'blue' END over_dot\nFROM aps_v_hds_journal_pool, var\nWHERE array_name LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\nAND array_name IS NOT NULL\nAND capacity_of_vvols_kb > 0"
has_explanation: false
products: [{"slug": "capacity-manager-hds-reports", "name": "HDS Reports"}]
categories: []
product_slugs: ["capacity-manager-hds-reports"]
category_slugs: []
---
