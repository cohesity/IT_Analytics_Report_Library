---
title: "HDS LUSE Summary by Array"
report_id: 1070
rtd_name: "HDS LUSE Summary by Array.rtd"
description: "HDS LUSE Summary by Array"
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
sql_query: "--Author:paul.hogan@aptare.com\n--Last Updated: 10/4/2012\n--This will list all LDEV's that make up a LUSE\nWITH t1 AS\n  (SELECT a.logical_unit_id,\n    a.logical_unit_name,\n    a.storage_array_id,\n    c.device_nbr,\n    c.array_name,\n    c.capacity_gb ldev_capacity_gb,\n    c.raid_type,\n    c.array_group_name,\n    a.dp_type,\n    a.dp_pool_id,\n    CASE\n      WHEN a.logical_unit_name=SUBSTR(logical_unit_name,0,3)\n        ||regexp_replace(SUBSTR(TO_CHAR(c.device_nbr,'XXXX'),-2,1)\n        ||NVL(SUBSTR(TO_CHAR(c.device_nbr,'XXXX'),           -1,1),'0'),' ','0')\n      THEN b.luse_capacity_gb\n      ELSE NULL\n    END luse_capacity_gb,\n    CASE\n      WHEN a.logical_unit_name=SUBSTR(logical_unit_name,0,3)\n        ||regexp_replace(SUBSTR(TO_CHAR(c.device_nbr,'XXXX'),-2,1)\n        ||NVL(SUBSTR(TO_CHAR(c.device_nbr,'XXXX'),           -1,1),'0'),' ','0')\n      THEN c.path_exists\n      ELSE NULL\n    END allocated,\n    --c.path_exists allocated,\n    CASE\n      WHEN a.logical_unit_name=SUBSTR(logical_unit_name,0,3)\n        ||regexp_replace(SUBSTR(TO_CHAR(c.device_nbr,'XXXX'),-2,1)\n        ||NVL(SUBSTR(TO_CHAR(c.device_nbr,'XXXX'),           -1,1),'0'),' ','0')\n      THEN logical_unit_name\n      ELSE NULL\n    END luse_head,\n    CASE\n      WHEN a.logical_unit_name<>SUBSTR(logical_unit_name,0,3)\n        ||regexp_replace(SUBSTR(TO_CHAR(c.device_nbr,'XXXX'),-2,1)\n        ||NVL(SUBSTR(TO_CHAR(c.device_nbr,'XXXX'),           -1,1),'0'),' ','0')\n      THEN logical_unit_name\n      ELSE NULL\n    END luse_sub,\n    SUBSTR(logical_unit_name,0,3)\n    ||regexp_replace(SUBSTR(TO_CHAR(c.device_nbr,'XXXX'),-2,1)\n    ||NVL(SUBSTR(TO_CHAR(c.device_nbr,'XXXX'),           -1,1),'0'),' ','0') ldev\n  FROM\n    (SELECT *\n    FROM aps_v_hds_ldev\n    WHERE logical_unit_id IN\n      (SELECT logical_unit_id\n      FROM aps_v_hds_ldev\n      GROUP BY logical_unit_id\n      HAVING (COUNT(logical_unit_id ) > 1)\n      )\n    ) c,\n    (SELECT SUM(c.capacity_gb) luse_capacity_gb,\n      a.logical_unit_id\n    FROM\n      (SELECT *\n      FROM aps_v_hds_ldev\n      WHERE logical_unit_id IN\n        (SELECT logical_unit_id\n        FROM aps_v_hds_ldev\n        GROUP BY logical_unit_id\n        HAVING (COUNT(logical_unit_id ) > 1)\n        )\n      ) c,\n      aps_v_hds_logical_unit a\n    WHERE c.logical_unit_id=a.logical_unit_id\n    GROUP BY a.logical_unit_id\n    ) b,\n    aps_v_hds_logical_unit a\n  WHERE c.logical_unit_id=a.logical_unit_id\n  AND c.logical_unit_id  =b.logical_unit_id\n  )\nSELECT array_name,\n  logical_unit_name,\n  SUM(ldev_capacity_gb) luse_capacity_gb,\n  REPLACE(aptStringConcat(DISTINCT ldev),'+',',') ldev_list\nFROM t1\nWHERE array_name = DECODE('${queryCombo1}',' All',array_name,'${queryCombo1}')\nGROUP BY array_name,\n  logical_unit_name"
has_explanation: false
products: [{"slug": "capacity-manager-hds-reports", "name": "HDS Reports"}]
categories: []
product_slugs: ["capacity-manager-hds-reports"]
category_slugs: []
---
