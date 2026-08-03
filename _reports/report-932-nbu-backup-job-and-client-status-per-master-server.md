---
title: "NBU Backup Job and Client Status per Master Server"
report_id: 932
rtd_name: "NBU Backup Job and Client Status per Master Server.rtd"
description: "NBU Backup Job and Client Status per Master Server"
problem_statement: ""
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 07/06/2015\n--NOTE: Requires drilldown report \"Client Status Summary.D\"\n--from the Drilldown Components menu\nWITH \nd1 AS (--Dates Required for Drilldown \nSELECT\nTO_CHAR(${startDate},'MM/DD/YYYY') start_date_char,\nTO_CHAR(${startDate},'HH24') start_hour_char,\nTO_CHAR(${endDate},'MM/DD/YYYY') finish_date_char,\nTO_CHAR(${endDate},'HH24') finish_hour_char\nFROM apt_v_dual\n),\nj1 AS (--Gathers Job Status\nSELECT \nj.server_id,\nj.master_host_name,\nCOUNT(DISTINCT j.media_server_id) media_server_count,\nCOUNT(DISTINCT policy_id) policy_count,\nSUM(j.kilobytes/1024/1024/1024) job_volume,\nCOUNT(j.job_id) job_count,\nSUM(DECODE(j.vendor_status_name,'Successful',1,0)) successful_job_count,\nSUM(DECODE(j.vendor_status_name,'Failed',1,0)) failed_job_count,\nSUM(DECODE(j.vendor_status_name,'Partial',1,0)) partial_job_count,\nROUND((sum(DECODE(j.vendor_status_name,'Successful',1,0))+sum(DECODE(j.vendor_status_name,'Partial',1,0)))\n/count(j.job_id)*100,2) job_success_rate,\nROUND(SUM(DECODE(j.summary_status,0,1,0))/COUNT(j.job_id)*100,2) job_strict_success_rate,\nROUND(SUM(DECODE(j.summary_status,1,1,0))/COUNT(j.job_id)*100,2) job_partial_rate,\nROUND(SUM(DECODE(j.summary_status,2,1,0))/COUNT(j.job_id)*100,2) job_failed_rate\nFROM apt_v_nbu_job_detail j\nWHERE j.start_date BETWEEN ${startDate} AND ${endDate}\nAND j.client_id IN (${hosts})\nGROUP BY \nj.server_id,\nj.master_host_name\n),\nfc1 AS (--Gathers Clients Status\nSELECT\nj.server_id,\nj.client_id,\nMIN(summary_status) min_summary_status,\nMAX(summary_status) max_summary_status\nFROM apt_v_job j\nWHERE j.client_id IN (${hosts})\nAND j.start_date BETWEEN ${startDate} AND ${endDate}\nAND summary_status IS NOT NULL\nGROUP BY\nj.server_id,\nj.client_id\n),\nfc2 AS (\nSELECT\nserver_id,\nCOUNT(DISTINCT client_id) client_count,\nSUM(CASE WHEN min_summary_status = 2 AND max_summary_status = 2 THEN 1 ELSE 0 END) failed_clients,\nSUM(CASE WHEN min_summary_status = 1 AND max_summary_status = 1 THEN 1 ELSE 0 END) partial_clients,\nSUM(CASE WHEN min_summary_status = 0 AND max_summary_status = 0 THEN 1 ELSE 0 END) successful_clients,\nSUM(CASE WHEN min_summary_status = 0 AND max_summary_status = 1 THEN 1 ELSE 0 END) successful_partial_clients,\nSUM(CASE WHEN min_summary_status <> max_summary_status THEN 1 ELSE 0 END) mixed_clients\nFROM fc1\nGROUP BY server_id\n), \nfc3 AS (\nSELECT\nserver_id,\nfailed_clients,\npartial_clients,\nsuccessful_clients,\nmixed_clients,\nclient_count,\nROUND(failed_clients/client_count*100,2) client_failure_rate,\nROUND(partial_clients/client_count*100,2) client_partial_rate,\nROUND(mixed_clients/client_count*100,2) client_mixed_rate,\nROUND((successful_clients+partial_clients+successful_partial_clients)/client_count*100,2) client_success_rate\nFROM fc2\n)\nSELECT \ns.location,\nj1.server_id,\nmaster_host_name,\nmedia_server_count,\npolicy_count,\njob_volume,\njob_count,\nCASE \nWHEN job_success_rate BETWEEN ${freeCombo2} AND 99.999 THEN 'green'\nWHEN job_success_rate BETWEEN ${freeCombo1} AND ${freeCombo2} THEN 'yellow'\nWHEN job_success_rate < ${freeCombo1} THEN 'red'\nWHEN job_success_rate = 100 THEN 'blue'\nELSE 'white'\nEND job_status_dot,\nsuccessful_job_count,\njob_strict_success_rate,\npartial_job_count,\njob_partial_rate,\nfailed_job_count,\njob_failed_rate,\njob_success_rate,\nclient_count,\nCASE \nWHEN client_success_rate BETWEEN ${freeCombo2} AND 99.999 THEN 'green'\nWHEN client_success_rate BETWEEN ${freeCombo1} AND ${freeCombo2} THEN 'yellow'\nWHEN client_success_rate < ${freeCombo1} THEN 'red'\nWHEN client_success_rate = 100 THEN 'blue'\nELSE 'white'\nEND client_status_dot,\nsuccessful_clients,\npartial_clients,\nfailed_clients,\nmixed_clients,\nclient_success_rate,\nstart_date_char,\nstart_hour_char,\nfinish_date_char,\nfinish_hour_char\nFROM d1, j1, fc3, apt_v_server s\nWHERE j1.server_id = fc3.server_id \nAND j1.server_id = s.server_id\nORDER BY 10 asc\n"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
