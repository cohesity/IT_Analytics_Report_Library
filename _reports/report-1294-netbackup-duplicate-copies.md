---
title: "NetBackup Duplicate Copies"
report_id: 1294
rtd_name: "NetBackup Duplicate Copies.rtd"
description: "A report that mimics the 'Duplicate Copies' Report in OpsCenter. The report is used by OpsCenter users to ensure there is more than 1 Duplication copy (also known as extra duplication copy) of the Original Backup for Backup Client/Clients of their choice. Please note, the tool used to develop the report is different from the OpsCenter Product and hence some look and feel of the report may vary"
problem_statement: "For OpsCenter Users migrating to NetBackup IT Analytics, provide a report that mimics OpsCenter Report 'Duplicate Copies'. "
author: "mandar.kulkarni@veritas.com"
modified_date: "2024-07-15"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: true
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "-- Total Clients participating in Duplication Jobs for the given time frame\nWITH t1 AS (\nSELECT TRUNC(finish_date) finish_date,\n       COUNT(DISTINCT(target_client_id)) original_backups,\n       SUM(nbr_of_copies) total_duplication_images\nFROM apt_v_nbu_duplication_job\nWHERE finish_date BETWEEN ${startDate} AND ${endDate}\n  AND target_client_id IN (${hosts})\n  AND summary_status=0\nGROUP BY TRUNC(finish_date)\n)\n\nSELECT finish_date,\n       total_duplication_images - original_backups total_duplication_images_bar,   \n       ROUND((total_duplication_images - original_backups)/total_duplication_images * 100) pct_of_extra_backup_copies_bar, \n       total_duplication_images - original_backups,\n       ROUND((total_duplication_images - original_backups)/total_duplication_images * 100),\n       TO_CHAR(finish_date,'DD-MON-YYYY') start_date_char \nFROM t1\nORDER BY finish_date"
has_explanation: true
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: [{"slug": "opscenter-reports", "name": "OpsCenter Reports"}]
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: ["opscenter-reports"]
---

This report mirrors OpsCenter's classic "Duplicate Copies" report: it flags backup images that don't have the expected number of duplicate (extra) copies, so you can spot backups at risk if their primary copy is lost or expires. Pick a time range and a scope (hosts, policies, etc.) and it lists images where the duplication count falls short.
