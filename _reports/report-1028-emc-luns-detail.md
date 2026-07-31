---
title: "EMC LUNs Detail"
report_id: 1028
rtd_name: "EMC LUNs Detail.rtd"
description: "EMC LUNs Detail"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "SELECT DISTINCT array_family,storage_array_id,array_name,\nemulation_type,group_name,is_mapped,is_mapped_not_masked,total_capacity_gb, is_synchronized,last_updated,logical_unit_name,lun_type,nbr_allocated_luns,nbr_of_luns,normalized_raid_type,raid_type,rdf_grp_name,rdf_grp_nbr,rdf_mode,rdf_state,bcv_pair_state,device_rdf_state\nFROM aps_v_emc_sym_logical_unit\nWHERE '${freeCombo1}' IN \n  CASE \n    WHEN '${freeCombo1}' NOT IN ('All') THEN\n      CASE\n        WHEN is_mapped = 'Y'  THEN 'Yes'\n        WHEN is_mapped = 'N'  THEN 'No'\n      END\n   ELSE 'All'\n END\nAND '${freeCombo2}' IN \n  CASE \n    WHEN '${freeCombo2}' NOT IN ('All') THEN\n      CASE\n        WHEN is_mapped_not_masked = 'Y'  THEN 'Yes'\n        WHEN is_mapped_not_masked = 'N'  THEN 'No'\n      END\n   ELSE 'All'\n END\nAND '${freeCombo3}' IN \n  CASE \n    WHEN '${freeCombo3}' NOT IN ('All') THEN\n      CASE\n        WHEN raid_type LIKE 'RAID-5%'  THEN 'RAID-5'\n        WHEN raid_type NOT LIKE 'RAID-5%' THEN 'Other'\n      END\n   ELSE 'All'\n END\nAND '${queryCombo1}' IN \n  CASE \n    WHEN '${queryCombo1}' NOT IN ('All') THEN\n      CASE\n        WHEN lun_type LIKE '${queryCombo1}' THEN '${queryCombo1}'\n      END\n   ELSE 'All'\n END"
has_explanation: false
products: [{"slug": "capacity-manager-emc-reports", "name": "EMC Reports"}]
categories: []
product_slugs: ["capacity-manager-emc-reports"]
category_slugs: []
---
