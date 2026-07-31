---
title: "TSM Node Filespace Volumes"
report_id: 980
rtd_name: "TSM Node Filespace Volumes.rtd"
description: "TSM Node Filespace Volumes"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated: 11/07/2011\nWITH \nc1 AS ( --Only select one client because of performance\nSELECT max(server_id) client_id\nFROM apt_v_server \nWHERE server_id IN (${hosts})\n),\nt1 AS (\nSELECT n.node_id, n.node_name,\n  f.filespace_id, f.filespace_name,\n  f.capacity_kbytes, \n  DECODE(f.capacity_kbytes,NULL,NULL,TRUNC(f.capacity_kbytes - (f.capacity_kbytes * (NVL(f.pct_utilized, 0)/100)))) free_kbytes,\n  f.backup_start_date,\n  f.backup_finish_date\nFROM apt_v_tsm_filespace f, apt_v_tsm_node n, c1\nWHERE n.client_id = c1.client_id\n  AND n.node_id   = f.node_id\n),\nt2 AS (\nSELECT tj.node_id, j.job_id, j.finish_date, t1.filespace_id\nFROM apt_v_job j, apt_v_tsm_job tj, t1, c1\nWHERE j.client_id = c1.client_id\n  AND j.job_type IN (401,402,403,408,420,420)\n  --401=TSM_SCHEDULE_SELECTIVE \n  --402=TSM_SCHEDULE_INCREMENTAL\n  --403=TSM_SCHEDULE_IMAGE_BACKUP\n  --408=TSM_SCHEDULE_COMMAND\n  --420=TSM_PROCESS_NAS_BACKUP\n  --421=TSM_BACKUP_SET   \n  AND t1.backup_start_date  BETWEEN ${startDate}  AND ${endDate}\n  AND j.job_id   = tj.job_id\n  AND tj.node_id = t1.node_id\n  AND j.summary_status IN (1,2)\n),\nf1 AS (\nSELECT p.filespace_id, SUM(p.stg_pool_phy_kbytes) sum_phys_kbytes\nFROM t1, apt_v_tsm_stgpool_contents p, c1\nWHERE p.client_id = c1.client_id\n AND p.filespace_id = t1.filespace_id\nGROUP BY p.filespace_id\n),                          \nv1 AS (\nSELECT \n  v.filespace_id,\n  v.volume_id, \n  NVL(m.media_name, d.media_name) volume_name,\n  NVL(mt.storage_pool_id, d.storage_pool_id) storage_pool_id\nFROM apt_v_tsm_volume_contents v, apt_v_tape_media m, apt_v_tsm_tape_media mt, apt_v_tsm_disk_media d,f1\nWHERE v.filespace_id = f1.filespace_id\n  AND v.volume_id = m.tape_media_id(+)\n  AND v.volume_id = mt.tape_media_id(+)\n  AND v.volume_id = d.disk_media_id(+)                         \n),\nv2 AS (\nSELECT UNIQUE \n  v1.filespace_id,\n  v1.volume_id,\n  v1.volume_name,\n  s.storage_pool_id,\n  s.storage_pool_name\nFROM v1, apt_v_tsm_storage_pool s\nWHERE v1.storage_pool_id = s.storage_pool_id(+)\n  AND v1.volume_name IS NOT NULL\n)\nSELECT t1.node_id,\n  t1.node_name,\n  t1.filespace_id,\n  t1.filespace_name,\n  DECODE(t1.capacity_kbytes, NULL, f1.sum_phys_kbytes, 0, \n  f1.sum_phys_kbytes, t1.capacity_kbytes)/1024 capacity_mbytes,\n  t1.free_kbytes/1024 free_mbytes,\n  t2.job_id,\n  t1.backup_finish_date finish_date,\n  aptStringConcat(DISTINCT v2.storage_pool_name) storage_pools,\n  aptStringConcat(DISTINCT v2.volume_name) volumes\nFROM t1,f1,t2,v2\nWHERE t1.filespace_id = t2.filespace_id(+)\n  AND t1.filespace_id = f1.filespace_id(+)                                                    \n  AND t1.filespace_id = v2.filespace_id(+)   \nGROUP BY \n  t1.node_id,\n  t1.node_name,\n  t1.filespace_id,\n  t1.filespace_name,\n  DECODE(t1.capacity_kbytes, NULL, f1.sum_phys_kbytes, 0, f1.sum_phys_kbytes, t1.capacity_kbytes),\n  t1.free_kbytes,\n  t2.job_id,\n  t1.backup_finish_date                                               \nORDER BY Upper(t1.node_name), Upper(t1.filespace_name)"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
