---
title: "VM Guest Disk Writes Heat Map"
report_id: 1136
rtd_name: "VM Guest Disk Writes Heat Map.rtd"
description: "VM Guest Disk Writes Heat Map"
problem_statement: "I need to visualize the disk writes across multiple VM guests to quickly identify bottlenecks and help track down root cause of performance complaints."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 12/17/2014\nWITH \nt1 AS (\nSELECT\nTO_CHAR(TRUNC(l.start_log_date,'HH24'),'YY/MM/DD HH24') the_date,\nl.partition_id,\nl.partition_name,\nSUM(l.nbr_of_disk_write) nbr_of_disk_write,\nROUND((RATIO_TO_REPORT(SUM(l.nbr_of_disk_write)) OVER (PARTITION BY l.partition_id, l.partition_name))*100,2) rr_nbr_of_disk_write\nFROM\napt_v_vmw_perform_disk_log l, apt_v_partition p\nWHERE l.start_log_date BETWEEN ${startDate} AND ${endDate}\nAND l.partition_id = p.partition_id \nAND p.host_id IN (${hosts})\nAND l.partition_type = 'VM'\nGROUP BY\nTO_CHAR(TRUNC(l.start_log_date,'HH24'),'YY/MM/DD HH24'),\nl.partition_id,\nl.partition_name\nORDER BY 1,2\n),\nt2 AS (--Rank them\nSELECT\nthe_date,\npartition_id,\npartition_name,\nnbr_of_disk_write,\nrr_nbr_of_disk_write,\nDENSE_RANK() OVER (PARTITION BY partition_id, partition_name ORDER BY nbr_of_disk_write) dr_nbr_of_disk_write\nFROM t1\nORDER BY 1,2\n),\nt3 AS (--Assign colors to the rankings\nSELECT\nthe_date,\npartition_id,\npartition_name,\nnbr_of_disk_write,\nrr_nbr_of_disk_write,\ndr_nbr_of_disk_write,\nCASE\nWHEN dr_nbr_of_disk_write BETWEEN 0  AND 5  THEN '#FBEFEF'\nWHEN dr_nbr_of_disk_write BETWEEN 5  AND 10 THEN '#F6CECE'\nWHEN dr_nbr_of_disk_write BETWEEN 10 AND 15 THEN '#F78181'\nWHEN dr_nbr_of_disk_write BETWEEN 15 AND 20 THEN '#FE2E2E'\nWHEN dr_nbr_of_disk_write BETWEEN 20 AND 25 THEN '#DF0101'\nWHEN dr_nbr_of_disk_write BETWEEN 25 AND 30 THEN '#B40404'\nWHEN dr_nbr_of_disk_write BETWEEN 30 AND 35 THEN '#8A0808'\nWHEN dr_nbr_of_disk_write BETWEEN 35 AND 100 THEN '#610B0B'\nELSE '#FBEFEF'\nEND cell_color\nFROM t2\nORDER BY 1,2\n)\nSELECT\nthe_date,\npartition_id,\npartition_name,\nnbr_of_disk_write,\nrr_nbr_of_disk_write,\ndr_nbr_of_disk_write,\n'<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><td style=background-color:'||cell_color||' align=right>'||nbr_of_disk_write||'</td></table>' heatmap\nFROM t3\nORDER BY 1,2"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
