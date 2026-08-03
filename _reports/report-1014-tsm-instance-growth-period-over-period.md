---
title: "TSM Instance Growth Period over Period"
report_id: 1014
rtd_name: "TSM Instance Growth Period over Period.rtd"
description: "TSM Instance Growth Period over Period"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 09/09/2011\n--\n--Compares the client count and job volume period over period\n--EXAMPLE: If you choose \"Last 7 Days\" it compares last 7 days to prior 7 days if you choose last \n--\"30 Days\" it compares last 30 days to prior 30 days, etc...\n--NOTE: in large environments it may take a while to run if select all instances and long time periods\n--(like 1 year) so be sure to select a small time period first (like last 24 hrs), and see how it goes.\nWITH d1 as (\nSELECT (trunc(${endDate}) - trunc(${startDate})) num_day\nFROM apt_v_dual\n),\nt1 as (\nSELECT server_name, \ncount(DISTINCT client_id) client_count_curr,\nsum(kilobytes)/1024/1024 GB_SIZE_curr\nFROM apt_v_tsm_job, d1\nWHERE trunc(start_date) between (trunc(sysdate) - num_day) AND trunc(sysdate) \ngroup by server_name\n),\nt2 AS (\nSELECT server_name, \ncount(DISTINCT client_id) client_count_prior,\nsum(kilobytes)/1024/1024 GB_SIZE_Prior\nFROM apt_v_tsm_job, d1\nWHERE trunc(start_date) between trunc(sysdate) - (num_day*2) AND (trunc(sysdate) - num_day)\nGROUP BY server_name\n)\nSELECT t1.server_name, \ntrunc(sysdate) - (num_day*2) ||'-'|| (trunc(sysdate) - num_day) prior_period,\nclient_count_prior,\nt2.GB_SIZE_Prior,\n(trunc(sysdate) - num_day) ||'-'|| trunc(sysdate) curr_period,\nclient_count_curr,\nt1.GB_SIZE_curr, \n(t1.client_count_curr - t2.client_count_Prior) delta_client_count,\n(t1.GB_SIZE_curr - t2.GB_SIZE_Prior) delta_volume\nFROM t1,t2,d1\nWHERE t1.server_name = t2.server_name (+)\nORDER BY (t1.GB_SIZE_curr- t2.GB_SIZE_Prior) desc"
has_explanation: false
products: [{"slug": "backup-manager-ibm-spectrum-protect-tsm", "name": "IBM Spectrum Protect (TSM)"}]
categories: []
product_slugs: ["backup-manager-ibm-spectrum-protect-tsm"]
category_slugs: []
---
