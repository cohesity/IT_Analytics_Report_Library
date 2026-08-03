---
title: "80-20 Rule of Problematic Clients"
report_id: 1139
rtd_name: "80-20 Rule of Problematic Clients.rtd"
description: "80-20 Rule of Problematic Clients"
problem_statement: "I need a report which shows me my \"Problem Children\" i.e. slowest, longest running, largest, most number of files and most failures."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: true
video_url: "https://www.youtube.com/watch?v=WVUnFmKtcO4"
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 01/19/2015\nWITH t1 AS (\nSELECT \nj.client_name,\nj.server_name,\naptStringConcat(DISTINCT j.job_type_name) job_types,\nSUM(j.duration_secs) duration,\nSUM(j.kilobytes/1024/1024) size_gb,\nAVG(CASE WHEN j.kilobytes > 4096 THEN j.mbytes_sec ELSE NULL END) mbytes_sec,\nSUM(j.nbr_of_files) nbr_of_files,\nSUM(DECODE(j.summary_status,2,1,0)) most_failures,\nSUM(DECODE(j.summary_status,1,1,0)) most_partials\nFROM apt_v_job j\nWHERE start_date between ${startDate} and ${endDate}\nAND j.client_id IN (${hosts})\nAND j.client_id <> j.server_id\nGROUP BY\nj.client_name,\nj.server_name\n),\nlargest AS (\nSELECT 1 sort_order,  ' Largest' metric, \nclient_name, server_name, job_types, \nCASE\nWHEN size_gb < 1024 THEN ROUND(size_gb,2)||' GB' \nWHEN size_gb > 1024 THEN ROUND(size_gb/1024,2)||' TB' \nEND value \nFROM t1\nWHERE size_gb IS NOT NULL\nORDER BY size_gb DESC\n),\nlongest AS (\nSELECT 2 sort_order,  ' Longest Running' metric, \nclient_name, server_name, job_types, rtd.secsToHoursMinSecs(duration)||' Hrs' value\nFROM t1\nORDER BY duration DESC\n),\nslowest AS (\nSELECT 3 sort_order,  ' Slowest' metric, \nclient_name, server_name, job_types, ROUND(mbytes_sec,2)||' MB/Sec' value \nFROM t1\nWHERE mbytes_sec > 0\nORDER BY mbytes_sec ASC\n),\nmost_files AS (\nSELECT 4 sort_order,  ' Most Files' metric, \nclient_name, server_name, job_types, \nCASE \nWHEN nbr_of_files > 1000000 THEN ROUND(nbr_of_files/1000000,1)||' Million Files'\nWHEN nbr_of_files < 1000000 THEN ROUND(nbr_of_files/1000,0)||' Thousand Files'\nEND value \nFROM t1\nWHERE nbr_of_files IS NOT NULL\nORDER BY nbr_of_files DESC\n),\nmost_failures AS (\nSELECT 5 sort_order,  ' Most Failures' metric, \nclient_name, server_name, job_types, most_failures||' Failed Jobs' value  \nFROM t1\nWHERE most_failures > 0\nORDER BY most_failures DESC\n),\nmost_partials AS (\nSELECT 6 sort_order,  ' Most Partials' metric, \nclient_name, server_name, job_types, most_partials||' Partial Jobs' value  \nFROM t1\nWHERE most_partials > 0\nORDER BY most_partials DESC\n),\nt2 AS (\nSELECT sort_order, rownum rank, rownum||DECODE(rownum,1,'st',2,'nd',3,'rd','th')||metric metric,client_name, server_name, job_types, value FROM slowest\nWHERE rownum <= ${freeCombo1}\nUNION\nSELECT sort_order, rownum rank, rownum||DECODE(rownum,1,'st',2,'nd',3,'rd','th')||metric metric,client_name, server_name, job_types, value FROM largest\nWHERE rownum <= ${freeCombo1}\nUNION\nSELECT sort_order,rownum  rank, rownum||DECODE(rownum,1,'st',2,'nd',3,'rd','th')||metric metric,client_name, server_name, job_types, value FROM longest\nWHERE rownum <= ${freeCombo1}\nUNION\nSELECT sort_order,rownum rank, rownum||DECODE(rownum,1,'st',2,'nd',3,'rd','th')||metric metric,client_name, server_name, job_types, value FROM most_files\nWHERE rownum <= ${freeCombo1}\nUNION\nSELECT sort_order,rownum rank, rownum||DECODE(rownum,1,'st',2,'nd',3,'rd','th')||metric metric,client_name, server_name, job_types, value FROM most_partials\nWHERE rownum <= ${freeCombo1}\nUNION\nSELECT sort_order,rownum rank, rownum||DECODE(rownum,1,'st',2,'nd',3,'rd','th')||metric metric,client_name, server_name, job_types, value FROM most_failures\nWHERE rownum <= ${freeCombo1}\n),\noccurrences AS (\nSELECT\nclient_name,\nCOUNT(*) occurrences,\naptStringConcat(metric) other_bad_things\nFROM t2\nGROUP BY client_name\n)\nSELECT t2.*, occurrences,\nDECODE(occurrences,1,'white',2,'yellow','red') status_dot,\nother_bad_things,\nREPLACE(REPLACE(other_bad_things,',',' '),metric,'') also\nFROM t2, occurrences occ\nWHERE\nt2.client_name = occ.client_name\nORDER BY\nsort_order ASC, rank ASC"
has_explanation: false
products: [{"slug": "backup-manager-general-all-backup-vendors", "name": "General (All Backup Vendors)"}]
categories: []
product_slugs: ["backup-manager-general-all-backup-vendors"]
category_slugs: []
---
