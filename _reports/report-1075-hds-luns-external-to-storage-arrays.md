---
title: "HDS LUNs External to Storage Arrays"
report_id: 1075
rtd_name: "HDS LUNs External to Storage Arrays.rtd"
description: "HDS LUNs External to Storage Arrays"
problem_statement: ""
author: "paul.hogan@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: paul.hogan@aptare.com\n--Last Updated: 09/15/2011\n--This report shows the array and LUNs that are external to the array that is virtualizing them.\nSELECT a.logical_unit_id,\n  a.logical_unit_name,\n  a.array_name,\n  b.array_name ext_array_name,\n  b.group_name ext_raid_group,\n  b.open_allocated_capacity_gb ext_group_capacity_gb,\n  b.disk_size_gb ext_disk_size_gb,\n  b.raid_type ext_raid_type\nFROM\n  (SELECT a.logical_unit_id,\n    a.logical_unit_name,\n    a.array_name,\n    a.external_serial_nbr,\n    a.external_device_nbr,\n    b.array_group_id,\n    b.ldev_id\n  FROM\n    (SELECT c.logical_unit_id,\n      c.logical_unit_name,\n      b.array_name,\n      b.external_serial_nbr,\n      b.external_device_nbr\n    FROM aps_v_hds_ldev a,\n      aps_v_hds_virtual_volume b,\n      aps_v_hds_logical_unit c\n    WHERE a.ldev_id = b.ldev_id\n    AND c.logical_unit_id=a.logical_unit_id\n    ) a,\n    aps_v_hds_ldev b,\n    aps_v_hds_storage_array c\n  WHERE a.external_device_nbr = b.device_nbr\n  AND c.serial_nbr = a.external_serial_nbr\n  AND c.storage_array_id = b.storage_array_id\n  ) a,\n  aps_v_hds_array_group b\nWHERE a.array_group_id = b.array_group_id\nAND a.array_name LIKE DECODE('${queryCombo1}',' All','%','${queryCombo1}')\nORDER BY a.logical_unit_name,\n  b.storage_array_id"
has_explanation: false
products: [{"slug": "capacity-manager-hds-reports", "name": "HDS Reports"}]
categories: []
product_slugs: ["capacity-manager-hds-reports"]
category_slugs: []
---
