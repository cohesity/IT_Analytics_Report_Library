---
title: "Host Network Packets Sent & Received"
report_id: 1242
rtd_name: "Host Network Packets Sent & Received.rtd"
description: "Host Network Packets Sent & Received"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 09/19/2018\nWITH \nt1 AS (\nSELECT \nserver_id,\nexternal_name,\nNVL(NIC_NAME,'NA') nic_name,\nTRUNC(log_date,'dd') + round(to_char(log_date,'sssss') / 900) / 96  log_date, --Round up to nearest 15 Min\npackets_received,\nLEAD(packets_received, 1, 0) OVER (PARTITION BY server_id, NVL(NIC_NAME,'NA') ORDER BY server_id, log_date) lead_packets_received,\n(LEAD(packets_received, 1, 0) OVER (PARTITION BY server_id, NVL(NIC_NAME,'NA') ORDER BY server_id, log_date) - packets_received) pkts_rec,\npackets_sent,\nLEAD(packets_sent, 1, 0) OVER (PARTITION BY server_id, NVL(NIC_NAME,'NA') ORDER BY server_id, log_date) lead_packets_sent,\n(LEAD(packets_sent, 1, 0) OVER (PARTITION BY server_id, NVL(NIC_NAME,'NA') ORDER BY server_id, log_date) - packets_sent) pkts_sent\nFROM \napt_v_host_network_log\nWHERE \nserver_id IN (${hosts})\nAND log_date BETWEEN ${startDate} AND ${endDate}\n)\nSELECT\nlog_date,\nSUM(pkts_rec) pkts_rec,\nSUM(pkts_sent) pkts_sent \nFROM t1\nWHERE \npkts_rec > 0\nGROUP BY\nlog_date"
has_explanation: false
products: [{"slug": "capacity-manager-host-probe-reports", "name": "Host Probe Reports"}]
categories: []
product_slugs: ["capacity-manager-host-probe-reports"]
category_slugs: []
---
