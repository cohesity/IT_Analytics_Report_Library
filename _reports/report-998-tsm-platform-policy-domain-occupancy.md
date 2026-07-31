---
title: "TSM Platform Policy Domain Occupancy"
report_id: 998
rtd_name: "TSM Platform Policy Domain Occupancy.rtd"
description: "TSM Platform Policy Domain Occupancy"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "WITH pd as (\nSELECT\npd.server_instance_id,\npd.server_instance_name,\ns.os_version,\npd.domain_id,\npd.domain_name,\npd.backup_retention_days,\npd.archive_retention_days,\ncount(DISTINCT n.node_id) nbr_of_nodes,\n--sum((fs.capacity_kbytes*(pct_utilized/100))/1024/1024) fs_capacity_gb\nsum(fs.capacity_kbytes/1024/1024) fs_capacity_gb\nFROM apt_v_tsm_policy_domain pd, apt_v_tsm_node n, apt_v_server s, apt_v_tsm_filespace fs\nWHERE pd.domain_id = n.domain_id\nAND n.client_id IN (${hosts})\nAND n.client_id = s.server_id\nAND fs.node_id = n.node_id\nAND s.os_version is not null\nGROUP BY\npd.server_instance_id,\npd.server_instance_name,\ns.os_version,\npd.domain_id,\npd.domain_name,\npd.backup_retention_days,\npd.archive_retention_days\n),\nsp AS (\nSELECT s.os_version, n.domain_id, SUM(spc.stg_pool_phy_kbytes/1024/1024) total_occupancy\n    FROM apt_v_tsm_node n, apt_v_tsm_stgpool_contents spc, apt_v_tsm_storage_pool p, apt_v_server s\n    WHERE n.client_id = spc.client_id\n    AND n.client_id IN (${hosts})\n    AND n.client_id = s.server_id\n    AND spc.storage_pool_id=p.storage_pool_id\n    AND s.os_version is not null\n    AND Upper(p.storage_pool_type) LIKE DECODE('${freeCombo1}','ALL','%','PRIMARY','PRIMARY','COPY','COPY')\n    GROUP BY s.os_version, n.domain_id\n),\nvo AS (\nSELECT  s.os_version,n.domain_id, COUNT(UNIQUE vc.volume_id) nbr_of_volumes\n    FROM apt_v_tsm_node n, apt_v_tsm_volume_contents vc, apt_v_server s\n    WHERE n.client_id = vc.client_id\n    AND n.client_id IN (${hosts})\n    AND n.client_id = s.server_id\n    AND s.os_version is not null\n    GROUP BY  s.os_version, n.domain_id\n)\nSELECT\ns.server_id,\npd.server_instance_id,\npd.server_instance_name,\npd.os_version node_os,\npd.domain_id,\npd.domain_name,\npd.backup_retention_days,\npd.archive_retention_days,\npd.nbr_of_nodes,\npd.fs_capacity_gb,\nsp.total_occupancy,\nvo.nbr_of_volumes\nFROM pd,sp,vo,apt_v_server s, apt_v_server_instance si\nWHERE pd.os_version = sp.os_version\nAND pd.os_version = vo.os_version\nAND pd.domain_id = sp.domain_id\nAND pd.domain_id = vo.domain_id\nAND pd.server_instance_id = si.server_instance_id\nAND si.server_id = s.server_id"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
