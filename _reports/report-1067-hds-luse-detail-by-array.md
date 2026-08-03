---
title: "HDS LUSE Detail by Array"
report_id: 1067
rtd_name: "HDS LUSE Detail by Array.rtd"
description: "HDS LUSE Detail by Array"
problem_statement: ""
author: "paul.hogan@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author:paul.hogan@aptare.com\n--Last Updated: 10/4/2012\n--This will list all LDEV's that make up all LUSE's within an array\nSELECT   a.logical_unit_id,\n  a.logical_unit_name,\n  c.device_nbr,\n         c.array_name, \n         c.capacity_gb ldev_capacity_gb, \n         c.raid_type, \n         c.array_group_name, \n         a.dp_type, \n         a.dp_pool_id, \n         case when a.logical_unit_name=substr(logical_unit_name,0,3)||regexp_replace(substr(to_char(c.device_nbr,'XXXX'),-2,1)||nvl(substr(to_char(c.device_nbr,'XXXX'),-1,1),'0'),' ','0') then b.luse_capacity_gb else null end luse_capacity_gb,\n         case when a.logical_unit_name=substr(logical_unit_name,0,3)||regexp_replace(substr(to_char(c.device_nbr,'XXXX'),-2,1)||nvl(substr(to_char(c.device_nbr,'XXXX'),-1,1),'0'),' ','0') then c.path_exists else null end allocated,\n         --c.path_exists allocated, \n         case when a.logical_unit_name=substr(logical_unit_name,0,3)||regexp_replace(substr(to_char(c.device_nbr,'XXXX'),-2,1)||nvl(substr(to_char(c.device_nbr,'XXXX'),-1,1),'0'),' ','0') then logical_unit_name else null end luse_head, \n         case when a.logical_unit_name<>substr(logical_unit_name,0,3)||regexp_replace(substr(to_char(c.device_nbr,'XXXX'),-2,1)||nvl(substr(to_char(c.device_nbr,'XXXX'),-1,1),'0'),' ','0') then logical_unit_name else null end luse_sub,\n         substr(logical_unit_name,0,3)||regexp_replace(substr(to_char(c.device_nbr,'XXXX'),-2,1)||nvl(substr(to_char(c.device_nbr,'XXXX'),-1,1),'0'),' ','0') ldev\n\nFROM     (SELECT * FROM aps_v_hds_ldev WHERE logical_unit_id IN ( SELECT logical_unit_id FROM aps_v_hds_ldev \n         GROUP BY logical_unit_id HAVING (COUNT(logical_unit_id ) > 1))) c, \n         \n         (SELECT SUM(c.capacity_gb) luse_capacity_gb, a.logical_unit_id FROM (SELECT * FROM aps_v_hds_ldev WHERE logical_unit_id IN (SELECT logical_unit_id FROM aps_v_hds_ldev GROUP BY logical_unit_id HAVING (COUNT(logical_unit_id ) > 1))) c,\n  aps_v_hds_logical_unit a WHERE c.logical_unit_id=a.logical_unit_id GROUP BY a.logical_unit_id) b,\n         \n         aps_v_hds_logical_unit a\n         \nWHERE    c.logical_unit_id=a.logical_unit_id \nAND c.logical_unit_id=b.logical_unit_id\nAND a.array_name = DECODE('${queryCombo1}',' All',a.array_name,'${queryCombo1}')\nORDER BY luse_head"
has_explanation: false
products: [{"slug": "capacity-manager-hds-reports", "name": "HDS Reports"}]
categories: []
product_slugs: ["capacity-manager-hds-reports"]
category_slugs: []
---
