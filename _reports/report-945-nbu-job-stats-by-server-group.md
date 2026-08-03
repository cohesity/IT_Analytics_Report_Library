---
title: "NBU Job Stats by Server Group"
report_id: 945
rtd_name: "NBU Job Stats by Server Group.rtd"
description: "NBU Job Stats by Server Group"
problem_statement: ""
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Server Group Aggregation 1 level up\nWITH \ng0 as (\nSELECT max(group_id) server_group\nFROM apt_v_group \nWHERE group_id IN (decode('${serverGroups}','',-1,'${serverGroups}'))\n),\nt1 as \n(\nSELECT DISTINCT server_id\nFROM apt_v_server\nWHERE server_id IN\n(SELECT m.child_id\nFROM apt_v_group_member m,g0\nWHERE m.child_type = 2\nSTART WITH m.group_id =  g0.server_group \nCONNECT BY m.group_id = PRIOR m.child_id AND PRIOR m.child_type = 1)\n),\nt2 as (\nSELECT\nrtd.getServerGroupContextById(g0.server_group,client_id,1) Server_Group ,\ncount(DISTINCT client_id) Client_Count,\ntrunc(sum(kilobytes/1024/1024)) Backup_Volume_GB,\ntrunc(sum(nbr_of_files)) File_Count,\ncount(DISTINCT job_id) Job_Count,\nsum(1*(1-abs(sign(summary_status-0)))) Success,\nsum(1*(1-abs(sign(summary_status-1)))) Partial,\nsum(1*(1-abs(sign(summary_status-2)))) Failed\nFROM apt_v_job j,t1,g0\nWHERE j.client_id = t1.server_id\nAND start_date BETWEEN  ${startDate} AND ${endDate}\nGROUP BY rtd.getServerGroupContextById(g0.server_group,client_id,1)\n)\nSELECT\nserver_group AS \"Group\",\nclient_count AS \"Client Count\",\nBackup_Volume_GB AS \"Backup Volume (GB)\",\nFile_Count AS \"File Count\",\nJob_Count \"Job Count\",\nSuccess AS \"Success\",\nPartial AS \"Partial\",\nFailed AS \"Failed\",\ntrunc(Success/DECODE(Job_Count,0,null,Job_Count)*100) AS \"Success Pct\"\nFROM t2"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
