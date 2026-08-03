---
title: "Backup Job and Client Status per Backup Server"
report_id: 890
rtd_name: "Backup Job and Client Status per Backup Server CL.rtd"
description: "Backup Job and Client Status per Backup Server"
problem_statement: "I have a large backup environment with multiple backup vendors, TSM, NetBackup, Avamar, Legato and CommVault.  I want a single morning report which shows me the job and client status for everything that occurred during last night's backup window."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 01/11/2019\nWITH \nd1 AS (\nSELECT\n--Dates Required for Drilldown \nTO_CHAR(${startDate},'MM/DD/YYYY') start_date_char,\nTO_CHAR(${startDate},'HH24') start_hour_char,\nTO_CHAR(${endDate},'MM/DD/YYYY') finish_date_char,\nTO_CHAR(${endDate},'HH24') finish_hour_char\nFROM apt_v_dual\n),\nj1 AS (--Job Stats\nSELECT \nj.server_id,\nj.server_name,\nj.product_type_name,\nSUM(j.kilobytes/1024/1024/1024) job_volume,\nCOUNT(j.job_id) job_count,\nSUM(DECODE(j.vendor_status_name,'Successful',1,0)) successful_job_count,\nSUM(DECODE(j.vendor_status_name,'Failed',1,0)) failed_job_count,\nSUM(DECODE(j.vendor_status_name,'Partial',1,0)) partial_job_count,\nROUND((sum(DECODE(j.vendor_status_name,'Successful',1,0))+sum(DECODE(j.vendor_status_name,'Partial',1,0)))\n/count(j.job_id)*100,2) job_success_rate\nFROM apt_v_job j\nWHERE j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.server_id IN (${hosts})\nGROUP BY \nj.server_id,\nj.server_name,\nj.product_type_name\n),\nfc1 AS (--Failed Clients \nSELECT\nj.server_id,\nj.client_id,\nmin(summary_status) min_summary_status,\nmax(summary_status) max_summary_status\nFROM apt_v_job j\nWHERE j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND summary_status IS NOT NULL\nGROUP BY\nj.server_id,\nj.client_id\n),\nfc2 AS (\nSELECT\nserver_id,\nCOUNT(DISTINCT client_id) client_count,\nSUM(CASE WHEN min_summary_status = 2 AND max_summary_status = 2 THEN 1 ELSE 0 END) failed_clients,\nSUM(CASE WHEN min_summary_status = 1 AND max_summary_status = 1 THEN 1 ELSE 0 END) partial_clients,\nSUM(CASE WHEN min_summary_status = 0 AND max_summary_status = 0 THEN 1 ELSE 0 END) successful_clients,\nSUM(CASE WHEN min_summary_status <> max_summary_status THEN 1 ELSE 0 END) mixed_clients\nFROM fc1\nGROUP BY server_id\n), \nfc3 AS (\nSELECT\nserver_id,\nfailed_clients,\npartial_clients,\nsuccessful_clients,\nmixed_clients,\nclient_count,\nROUND(failed_clients/client_count*100,2) client_failure_rate,\nROUND(partial_clients/client_count*100,2) client_partial_rate,\nROUND(successful_clients/client_count*100,2) client_success_rate,\nROUND(mixed_clients/client_count*100,2) client_mixed_rate\nFROM fc2\n)\nSELECT \n--If you have attributes for your backup servers un-comment the line \n--below and modify the attribute name if necessary.  The example below assumes a\n--'Location' attribute has been assigned to each backup server.\n--rtd.getObjectAttributeValue(j1.server_id,'Location','S') location,\nj1.server_id,\nserver_name,\nproduct_type_name,\njob_volume,\njob_count,\nCASE \nWHEN job_success_rate BETWEEN ${freeCombo2} AND 99.999 THEN 'green'\nWHEN job_success_rate BETWEEN ${freeCombo1} AND ${freeCombo2} THEN 'yellow'\nWHEN job_success_rate < ${freeCombo1} THEN 'red'\nWHEN job_success_rate = 100 THEN 'blue'\nELSE 'white'\nEND job_status_dot,\nsuccessful_job_count,\npartial_job_count,\nfailed_job_count,\njob_success_rate,\nclient_count,\nCASE \nWHEN client_success_rate BETWEEN ${freeCombo2} AND 99.999 THEN 'green'\nWHEN client_success_rate BETWEEN ${freeCombo1} AND ${freeCombo2} THEN 'yellow'\nWHEN client_success_rate < ${freeCombo1} THEN 'red'\nWHEN client_success_rate = 100 THEN 'blue'\nELSE 'white'\nEND client_status_dot,\nsuccessful_clients,\npartial_clients,\nfailed_clients,\nmixed_clients,\nclient_success_rate,\nstart_date_char,\nstart_hour_char,\nfinish_date_char,\nfinish_hour_char\nFROM d1, j1, fc3\nWHERE j1.server_id = fc3.server_id \nORDER BY 10 asc"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
