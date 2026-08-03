---
title: "Switch Port Daily Peak Utilization Percentages Pivot"
report_id: 1213
rtd_name: "Switch Port Daily Peak Utilization Percentages Pivot.rtd"
description: "Switch Port Daily Peak Utilization Percentages Pivot"
problem_statement: "Show me which switch port elements have had a peak daily utilization rate of greater than X percent over the past 2 weeks"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 06/26/2018\nWITH \nvar AS (\nSELECT DECODE('${freeCombo1}','0%',0,'5%',5,'10%',10,'20%',20,'30%',30,'40%',40,'50%',50,'60%',60,'70%',70,'80%',80,'90%',90) the_pct FROM apt_v_dual\n),\nt1 AS (\nSELECT\npdl.switch_fc_port_id,\nROUND(MAX((pdl.peak_utilization_pct*100)),2) peak_pct_used\nFROM \nvar, aps_v_swi_perform_daily_log pdl\nWHERE\npdl.log_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\npdl.switch_fc_port_id\nHAVING ROUND(MAX((pdl.peak_utilization_pct*100)),2) > var.the_pct\n) \nSELECT\nTO_CHAR(TRUNC(pdl.log_date),'MM/DD/YY') log_date,\nNVL(fc.element_name,'UNKNOWN') port_element_name,\nCASE \n  WHEN ROUND((pdl.peak_utilization_pct*100),2) >= var.the_pct \n    THEN '<font color=red>'||TO_CHAR(ROUND((pdl.peak_utilization_pct*100),2),'999.00')||'%</font>'\n  ELSE TO_CHAR(ROUND((pdl.peak_utilization_pct*100),2),'999.00')||'%' \nEND  peak_pct_used,\npdl.switch_fc_port_id,\npdl.log_date sort_order\nFROM \nvar, t1, aps_v_swi_switch_fc_port fc, aps_v_swi_perform_daily_log pdl\nWHERE\nt1.switch_fc_port_id = fc.switch_fc_port_id\nAND fc.switch_fc_port_id = pdl.switch_fc_port_id \nAND pdl.log_date BETWEEN ${startDate} AND ${endDate}\nORDER BY 5 DESC"
has_explanation: false
products: [{"slug": "fabric-manager-general", "name": "General"}, {"slug": "fabric-manager-brocade", "name": "Brocade"}, {"slug": "fabric-manager-cisco", "name": "Cisco"}]
categories: []
product_slugs: ["fabric-manager-general", "fabric-manager-brocade", "fabric-manager-cisco"]
category_slugs: []
---
