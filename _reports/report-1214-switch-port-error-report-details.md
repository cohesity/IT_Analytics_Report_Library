---
title: "Switch Port Error Report Details"
report_id: 1214
rtd_name: "Switch Port  Error Report Details.rtd"
description: "Switch Port Error Report Details"
problem_statement: "Show me which switch ports are getting errors so I can troubleshoot which hosts and applications may be affected"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 06/27/2018\nWITH \nal AS (\nSELECT \nms.node_fc_port_id, \nsp.switch_fc_port_id, \nrtd.collectString(set(cast(collect(ma.collection_alias) as StringListType)),', ') alias_list,   \nrtd.collectString(set(cast(collect(ms.wwn) as StringListType)),', ') wwn_list\nFROM \naps_v_swi_zone_membersetting ms,  \naps_v_swi_map_zalias_zmemb   mp,\naps_v_swi_zone_member_alias  ma, \naps_v_swi_switch_fc_port sp\nWHERE \nms.zone_member_setting_id = mp.zone_member_setting_id\nAND mp.zone_member_alias_id = ma.zone_member_alias_id\nAND ms.node_fc_port_id = sp.connect_node_fc_port_id\nGROUP BY \nms.node_fc_port_id,sp.switch_fc_port_id\n)\nSELECT\nd.domain_id,\nd.domain_name,\ns.san_id,\ns.san_name,\ns.element_name san_element_name,\nf.fabric_id,\nf.fabric_name,\nf.element_name fabrc_element_name,\nb.blade_id,\nb.slot_nbr,\nb.vendor_equipment_type,\nt.fc_port_trunk_id,\nt.element_name trunk_element_name,\nt.load_balance_algorithm,\nsw.switch_id,\nsw.element_name switch_element_name,\npsw.physical_switch_id,\npsw.element_name physical_switch_element_name, \npsw.operational_status switch_status,\nDECODE(psw.operational_status,'OK','green','red') switch_status_dot,\np.switch_fc_port_id,\np.port_nbr,\nLPAD(b.slot_nbr,4,'0')||'-'||LPAD(p.port_nbr,4,'0') slot_port_number,\np.port_index,\np.element_name port_element_name,\np.vsan_identifier,\np.enabled_state,\np.speed,\np.max_speed,\np.operational_status port_status,\nDECODE(p.operational_status,'OK','green','red') port_status_dot,\nREPLACE(n.element_name,'\\\"','') node_element_name,\nnp.element_name node_port_element_name,\nal.alias_list,\nal.wwn_list,\nst.address_errors,\nst.bbc_credit_zero,\nst.link_failures,\nst.total_crc_error_received,\nst.loss_of_signal_counter,\nst.loss_of_sync_counter,\nst.total_encoding_out_frame_err,\n(CASE WHEN NVL(st.address_errors,0) > 0 THEN 1 ELSE 0 END) +\n(CASE WHEN NVL(st.bbc_credit_zero,0) > 0 THEN 1 ELSE 0 END) +\n(CASE WHEN NVL(st.link_failures,0) > 0 THEN 1 ELSE 0 END) +\n(CASE WHEN NVL(st.total_crc_error_received,0) > 0 THEN 1 ELSE 0 END) +\n(CASE WHEN NVL(st.loss_of_signal_counter,0) > 0 THEN 1 ELSE 0 END) +\n(CASE WHEN NVL(st.loss_of_sync_counter,0) > 0 THEN 1 ELSE 0 END) +\n(CASE WHEN NVL(st.total_encoding_out_frame_err,0) > 0 THEN 1 ELSE 0 END)\nnbr_of_strikes,\nst.last_updated\nFROM \naps_v_swi_switch_fc_port p, \naps_v_swi_switch sw,\naps_v_swi_physical_switch psw,\naps_v_swi_fc_port_stats st,\naps_v_domain d,\naps_v_swi_san s,\naps_v_swi_fabric f,\naps_v_swi_blade b,\naps_v_swi_fc_port_trunk t,\naps_v_swi_node n,\naps_v_swi_node_fc_port np,\nal\nWHERE\np.physical_switch_id = psw.physical_switch_id\nAND p.physical_switch_id = sw.physical_switch_id\nAND p.switch_fc_port_id = st.switch_fc_port_id\nAND p.domain_id = d.domain_id\nAND p.san_id = s.san_id\nAND p.fabric_id = f.fabric_id\nAND p.blade_id = b.blade_id\nAND p.fc_port_trunk_id = t.fc_port_trunk_id (+)\nAND p.connect_node_id = n.node_id (+)\nAND p.connect_node_fc_port_id = np.node_fc_port_id (+)\nAND (NVL(st.bbc_credit_zero,0) + NVL(st.link_failures,0) + NVL(st.total_crc_error_received,0)) > \nDECODE('${freeCombo1}','All Ports',-1,'Only Ports with Errors',0)\nAND p.switch_fc_port_id = al.switch_fc_port_id (+)\nORDER BY 41 DESC"
has_explanation: false
products: [{"slug": "fabric-manager-general", "name": "General"}, {"slug": "fabric-manager-brocade", "name": "Brocade"}, {"slug": "fabric-manager-cisco", "name": "Cisco"}]
categories: []
product_slugs: ["fabric-manager-general", "fabric-manager-brocade", "fabric-manager-cisco"]
category_slugs: []
---
