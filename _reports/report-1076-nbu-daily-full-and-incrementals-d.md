---
title: "NBU Daily Full and Incrementals.D"
report_id: 1076
rtd_name: "NBU Daily Full and Incrementals.D.rtd"
description: "NBU Daily Full and Incrementals"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Updated, 10/22/2012\nSELECT \nserver_id,\nmaster_host_name,\nclient_id,\nclient_host_name,\npolicy_id,\npolicy_name, \npolicy_type_name,\njob_id,\nstart_date,\nfinish_date,\nexpiration_date,\njob_type_name,\nkilobytes/1024/1024 job_size\nFROM apt_v_nbu_job_detail\nWHERE start_date BETWEEN ${startDate} AND ${endDate}\nAND job_type IN (101,102)\nAND summary_status IN (0,1)\nAND client_host_name||' - '||policy_name = '${the_client_policy}'\nAND to_char(start_date,'MM/DD/YY') = '${the_date}'"
has_explanation: false
products: []
categories: []
product_slugs: []
category_slugs: []
---
