---
title: "Fabric Switch Alerts"
report_id: 1026
rtd_name: "Fabric Switch Alerts.rtd"
description: "Fabric Switch Alerts"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "SELECT\n'Alert' source,\nDECODE(ai.alerting_managed_element_type\n,'PHYSICAL_SWITCH_FC_PORT','PORT'\n,ai.alerting_managed_element_type\n) element_type,\nDECODE(ai.alerting_managed_element_type\n,'PHYSICAL_SWITCH_FC_PORT',sw1.element_name||' Port '||fcp.port_nbr \n,'SWITCH',sw.element_name\n,'OTHER'\n) element_name,\nai.perceived_severity severity,\nDECODE(\nai.perceived_severity,\n0,'blue' ,\n5,'yellow',\n2,'red',\n3,'red',\n'white'\n) status,\nai.indication_date, \nai.description \nFROM aps_v_swi_alert_ind ai, aps_v_swi_switch sw, aps_v_swi_switch_fc_port fcp, aps_v_swi_switch sw1\nWHERE ai.switch_id = sw.switch_id(+)\nAND ai.switch_fc_port_id = fcp.switch_fc_port_id(+)\nAND fcp.physical_switch_id = sw1.physical_switch_id(+)"
has_explanation: false
products: [{"slug": "fabric-manager-general", "name": "General"}, {"slug": "fabric-manager-brocade", "name": "Brocade"}, {"slug": "fabric-manager-cisco", "name": "Cisco"}]
categories: []
product_slugs: ["fabric-manager-general", "fabric-manager-brocade", "fabric-manager-cisco"]
category_slugs: []
---
