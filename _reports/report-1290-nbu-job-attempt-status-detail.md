---
title: "NBU Job Attempt Status Detail"
report_id: 1290
rtd_name: "NetBackup Job Attempt Status Detail.rtd"
description: "This report provides information about the completion status for a NetBackup job."
problem_statement: "I need to know when jobs are failing on a daily basis by Vendor Status"
author: ""
modified_date: "2024-05-28"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: tom.sprouse@veritas.com\n--Last Modified: 11.3.2023\n--Report: OpsCenter Report - Job Attempt Status Detail\nSELECT apt_v_nbu_job_detail.master_host_name,\nTRUNC(apt_v_nbu_job_detail.finish_date),\napt_v_nbu_job_detail.vendor_status,\nCOUNT(apt_v_nbu_job_detail.job_id)\nFROM apt_v_nbu_job_detail\nWHERE apt_v_nbu_job_detail.vendor_state = 3\nAND client_id IN (${hosts})\nAND start_date BETWEEN ${startDate} AND ${endDate}\nGROUP BY TRUNC(apt_v_nbu_job_detail.finish_date),apt_v_nbu_job_detail.vendor_status,apt_v_nbu_job_detail.master_host_name\nORDER BY TRUNC(apt_v_nbu_job_detail.finish_date), apt_v_nbu_job_detail.master_host_name, COUNT(apt_v_nbu_job_detail.job_id)"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
