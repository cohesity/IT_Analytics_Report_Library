---
title: "SAN Stats vs Last Month"
report_id: 1164
rtd_name: "SAN Stats vs Last Month.rtd"
description: "SAN Stats vs Last Month"
problem_statement: "I need high level KPI's on my SAN environment that I can present to my CIO, i.e. more information, less data."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/18/2015\n--Compare SAN metrics today vs same time last month\nWITH \nVAR AS (\nSELECT \n'${freeCombo1}' unit,\nDECODE('${freeCombo1}', 'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by,\nADD_MONTHS(TRUNC(sysdate,'MM'),-1) p_first, \nLAST_DAY(ADD_MONTHS(sysdate,-1)) p_last, \nADD_MONTHS(TRUNC(sysdate,'DD'),-1) p_day,\nTRUNC(sysdate,'MM') c_first, \nLAST_DAY(sysdate) c_last,\nTRUNC(sysdate,'DD') c_day,\ndomain_id  \nFROM aps_v_domain d\nWHERE domain_name = '${queryCombo1}'\n),\np0 AS (\nSELECT \np.switch_id,\np.switch_fc_port_id,\nMAX(l.total_bytes_tx_counter) tx_counter,\nMAX(l.total_bytes_rx_counter) rx_counter\nFROM aps_v_swi_perform_daily_log l, aps_v_swi_switch_fc_port p, var\nWHERE p.switch_fc_port_id = l.switch_fc_port_id \nAND p.domain_id = var.domain_id \nAND l.log_date BETWEEN p_first AND p_day\nGROUP BY\np.switch_id,\np.switch_fc_port_id\n),\np1 AS (\nSELECT\nCOUNT(DISTINCT switch_id) switches,\nCOUNT(DISTINCT switch_fc_port_id) ports,\nROUND(SUM(tx_counter/1000000000),2) tx_counter,\nROUND(SUM(rx_counter/1000000000),2) rx_counter\nFROM p0, var\n),\nc0 AS (\nSELECT \np.switch_id,\np.switch_fc_port_id,\nMAX(l.total_bytes_tx_counter) tx_counter,\nMAX(l.total_bytes_rx_counter) rx_counter\nFROM aps_v_swi_perform_daily_log l, aps_v_swi_switch_fc_port p, var\nWHERE p.switch_fc_port_id = l.switch_fc_port_id \nAND p.domain_id = var.domain_id \nAND l.log_date BETWEEN c_first AND c_day\nGROUP BY\np.switch_id,\np.switch_fc_port_id\n),\nc1 AS (\nSELECT\nCOUNT(DISTINCT switch_id) switches,\nCOUNT(DISTINCT switch_fc_port_id) ports,\nROUND(SUM(tx_counter/1000000000),2) tx_counter,\nROUND(SUM(rx_counter/1000000000),2) rx_counter\nFROM c0, var\n)\n-- Metrics Begin Here  --\nSELECT\n1 sort_order,\n'SAN Switches' metric,\np1.switches p_value,\nc1.switches c_value, \n(c1.switches - p1.switches) delta, \nROUND((c1.switches - p1.switches) / DECODE(p1.switches,0,NULL,p1.switches),2) delta_pct,\nABS(ROUND((c1.switches - p1.switches) / DECODE(p1.switches,0,NULL,p1.switches),2)) pct_delta\nFROM p1, c1\nUNION\nSELECT\n2 sort_order,\n'SAN Switch Ports' metric,\np1.ports p_value,\nc1.ports c_value, \n(c1.ports - p1.ports) delta, \nROUND((c1.ports - p1.ports) / DECODE(p1.ports,0,NULL,p1.ports),2) delta_pct,\nABS(ROUND((c1.ports - p1.ports) / DECODE(p1.ports,0,NULL,p1.ports),2)) pct_delta\nFROM p1, c1\nUNION\nSELECT\n3 sort_order,\n'Port Tx Traffic (Billion Packets)' metric,\np1.tx_counter p_value,\nc1.tx_counter c_value, \n(c1.tx_counter - p1.tx_counter) delta, \nROUND((c1.tx_counter - p1.tx_counter) / DECODE(p1.tx_counter,0,NULL,p1.tx_counter),2) delta_pct,\nABS(ROUND((c1.tx_counter - p1.tx_counter) / DECODE(p1.tx_counter,0,NULL,p1.tx_counter),2)) pct_delta\nFROM p1, c1\nUNION\nSELECT\n4 sort_order,\n'Port Rx Traffic (Billion Packets)' metric,\np1.rx_counter p_value,\nc1.rx_counter c_value, \n(c1.rx_counter - p1.rx_counter) delta, \nROUND((c1.rx_counter - p1.rx_counter) / DECODE(p1.rx_counter,0,NULL,p1.rx_counter),2) delta_pct,\nABS(ROUND((c1.rx_counter - p1.rx_counter) / DECODE(p1.rx_counter,0,NULL,p1.rx_counter),2)) pct_delta\nFROM p1, c1"
has_explanation: false
products: [{"slug": "fabric-manager-general", "name": "General"}, {"slug": "fabric-manager-brocade", "name": "Brocade"}, {"slug": "fabric-manager-cisco", "name": "Cisco"}]
categories: []
product_slugs: ["fabric-manager-general", "fabric-manager-brocade", "fabric-manager-cisco"]
category_slugs: []
---
