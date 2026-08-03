---
title: "Switch Port Daily Peak Utilization Percentages Sparklines"
report_id: 1231
rtd_name: "Switch Port Daily Peak Utilization Percentages Sparklines.rtd"
description: "Switch Port Daily Peak Utilization Percentages Sparklines"
problem_statement: "I need to identify patterns in peak utilization of my switch ports to help track down potential problems."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 06/28/2018\nWITH \nvar AS (\nSELECT DECODE('${freeCombo1}','0%',0,'5%',5,'10%',10,'20%',20,'30%',30,'40%',40,'50%',50,'60%',60,'70%',70,'80%',80,'90%',90) the_pct FROM apt_v_dual\n),\nt1 AS (\nSELECT\npdl.switch_fc_port_id,\nROUND(MAX((pdl.peak_utilization_pct*100)),2) peak_pct_used\nFROM \nvar, aps_v_swi_perform_daily_log pdl\nWHERE\npdl.log_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\npdl.switch_fc_port_id\nHAVING ROUND(MAX((pdl.peak_utilization_pct*100)),2) > var.the_pct\n) \nSELECT\npdl.switch_fc_port_id,\nNVL(fc.element_name,'UNKNOWN') element_name,\nrtd.collectString(CAST(COLLECT(TO_CHAR(ROUND((pdl.peak_utilization_pct*100),2)) ORDER BY log_date) AS StringListType),', ') Peak_Utilization_spk,\nAVG(ROUND((pdl.peak_utilization_pct*100),2)) avg_utilization_pct,\nMAX(ROUND((pdl.peak_utilization_pct*100),2)) max_utilization_pct,\nrtd.collectString(CAST(COLLECT(TO_CHAR(ROUND((throughput_kbps/1000),2)) ORDER BY log_date) AS StringListType),', ') throughput_mbps_spk,\nAVG(throughput_kbps/1000) avg_throughput_mbps,\nMAX(throughput_kbps/1000) max_throughput_mbps,\nrtd.collectString(CAST(COLLECT(TO_CHAR(ROUND((total_bytes_rx_counter/1024/1024/1024),2)) ORDER BY log_date) AS StringListType),', ') rx_spk,\nAVG(total_bytes_rx_counter/1024/1024/1024) avg_rx,\nMAX(total_bytes_rx_counter/1024/1024/1024) max_rx,\nrtd.collectString(CAST(COLLECT(TO_CHAR(ROUND((total_bytes_tx_counter/1024/1024/1024),2)) ORDER BY log_date) AS StringListType),', ') tx_spk,\nAVG(total_bytes_tx_counter/1024/1024/1024) avg_tx,\nMAX(total_bytes_tx_counter/1024/1024/1024) max_tx,\nrtd.collectString(CAST(COLLECT(TO_CHAR(log_date,'MMDD') ORDER BY log_date) AS StringListType),', ') date_history\nFROM \nvar, t1, aps_v_swi_switch_fc_port fc, aps_v_swi_perform_daily_log pdl\nWHERE\nt1.switch_fc_port_id = fc.switch_fc_port_id\nAND fc.switch_fc_port_id = pdl.switch_fc_port_id \nAND pdl.log_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY\npdl.switch_fc_port_id,\nNVL(fc.element_name,'UNKNOWN')"
has_explanation: false
products: [{"slug": "fabric-manager-general", "name": "General"}, {"slug": "fabric-manager-brocade", "name": "Brocade"}, {"slug": "fabric-manager-cisco", "name": "Cisco"}]
categories: []
product_slugs: ["fabric-manager-general", "fabric-manager-brocade", "fabric-manager-cisco"]
category_slugs: []
---
