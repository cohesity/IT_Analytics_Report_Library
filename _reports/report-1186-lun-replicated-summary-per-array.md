---
title: "LUN Replicated Summary per Array"
report_id: 1186
rtd_name: "LUN Replicated Summary per Array.rtd"
description: "LUN Replicated Summary per Array"
problem_statement: "Shows the capacity of the LUNs which are replicated per array"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 10/27/2017\nWITH\nVAR AS (\nSELECT\nDECODE('${freeCombo1}','GB',1,'TB',1024,'PB',(1024*1024)) div_by \nFROM apt_v_dual \n), \nrep AS (\nSELECT\n'EMC Symmetrix' array_type,\nlogical_unit_id, \nCASE WHEN SUBSTR(raid_type,1,4) = 'RDF1' THEN 'Y'WHEN SUBSTR(raid_type,1,5) = '2-Way' THEN 'Y' ELSE 'N' END is_replicated_lun\nFROM aps_v_emc_sym_logical_unit\nUNION ALL\nSELECT \n'HDS' array_type,\nlogical_unit_id,\nCASE WHEN true_copy_vol_type = 'P-VOL' \nOR univ_replicator_vol_type = 'P-VOL' \nOR shadow_image_vol_type = 'P-VOL' \nOR quick_shadow_vol_type = 'P-VOL' THEN 'Y' ELSE 'N' END is_replicated_lun\nFROM aps_v_hds_logical_unit \nUNION ALL\nSELECT\n'IBM XIV' array_type,\nxiv_volume_id logical_unit_id, \nis_mirrored is_replicated_lun\nFROM aps_v_xiv_volume\nUNION ALL\nSELECT\n'IBM SVC' array_type,\nsvc_storage_volume_id logical_unit_id, \nCASE WHEN COUNT(svc_mirror_extent_id) > 1 THEN 'Y' ELSE 'N' END is_replicated_lun\nFROM aps_v_svc_mirror_extent sme\nGROUP BY sme.svc_storage_volume_id\nUNION ALL\nSELECT\n'HP EVA' array_type,\nlogical_unit_id, \ndoes_mirror_exists is_replicated_lun\nFROM aps_v_eva_logical_unit sme\n),\nt1 AS (\nSELECT \nlu.storage_array_id,\nlu.array_name,\nCOUNT(lu.logical_unit_id) tot_lun_count,\nCOUNT(DECODE(NVL(rep.is_replicated_lun,'N'),'N',lu.logical_unit_id)) non_rep_lun_count,\nCOUNT(DECODE(NVL(rep.is_replicated_lun,'N'),'Y',lu.logical_unit_id)) rep_lun_count,\nSUM(lu.total_capacity_gb/div_by) tot_lun_capacity,\nSUM(DECODE(NVL(rep.is_replicated_lun,'N'),'N',lu.total_capacity_gb)/div_by) non_rep_lun_capacity,\nSUM(DECODE(NVL(rep.is_replicated_lun,'N'),'Y',lu.total_capacity_gb)/div_by) rep_lun_capacity\nFROM aps_v_logical_unit lu, rep, var\nWHERE lu.logical_unit_id = rep.logical_unit_id (+)\nGROUP BY \nlu.storage_array_id,\nlu.array_name\n)\nSELECT \ns.vendor_name,\ns.array_family,\nt1.storage_array_id,\nt1.array_name,\nt1.tot_lun_count,\nnon_rep_lun_count,\nrep_lun_count,\nrep_lun_count/tot_lun_count rep_lun_pct_count,\nrep_lun_count/tot_lun_count*100 pct_rep_lun_count,\ntot_lun_capacity,\nnon_rep_lun_capacity,\nrep_lun_capacity,\nrep_lun_capacity/tot_lun_capacity rep_lun_pct_cap,\nrep_lun_capacity/tot_lun_capacity*100 pct_rep_lun_cap\nFROM t1, aps_v_storage_array s, var\nWHERE\nt1.storage_array_id IN (${arrays}) \nAND t1.storage_array_id = s.storage_array_id\nAND rep_lun_count > 0\nORDER BY 2"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
