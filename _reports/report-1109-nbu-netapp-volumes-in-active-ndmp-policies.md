---
title: "NBU NetApp Volumes in Active NDMP Policies"
report_id: 1109
rtd_name: "NBU NetApp Volumes in Active NDMP Policies.rtd"
description: "NBU NetApp Volumes in Active Policies correlates information gathered from both NetApp's On-Tap API and VERITAS NetBackup to produce a consolidated view of which volumes are configured for backup.  This can be used for both compliance and billing purposes."
problem_statement: "I need to know if my NetApp Volumes are being protected by NetBackup for SOX compliance."
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 05/02/2013\n--NDMP Policies clients and pathnames\nWITH \nVAR AS (\nSELECT\nROUND((${endDate} - ${startDate})) nbrOfDays,\n${startDate} startDate\nFROM apt_v_dual\n),\nt1 AS (\nSELECT \ns.display_name master_server,\npc.client_id,\nUPPER(pc.client_name) client_name,\nCASE \nWHEN REGEXP_COUNT(pc.client_name,'\\\\.') = 3 THEN pc.client_name\nWHEN REGEXP_COUNT(pc.client_name,'\\\\.') IN (1,2) THEN UPPER(SUBSTR(pc.client_name,1,INSTR(pc.client_name,'.',1)-1)) \nWHEN REGEXP_COUNT(pc.client_name,'\\\\.') = 0 THEN pc.client_name\nEND\nshort_client_name,\np.policy_id,\np.policy_name,\nUPPER(pf.pathname) pathname\nFROM \napt_v_nbu_policy_file pf, apt_v_nbu_policy p, apt_v_nbu_policy_client pc, apt_v_server s\nWHERE \npc.client_id IN (${hosts})\nAND p.server_id = s.server_id\nAND pc.policy_id = p.policy_id\nAND p.policy_type_name = 'NDMP'\nAND p.policy_id = pf.policy_id\nAND p.is_active = 'Y'\nAND UPPER(SUBSTR(pf.pathname,1,4)) = '/VOL'\n),\nt2 AS (\nSELECT\nclient_id,\npolicy_id,\nMAX(j.start_date) last_backup\nFROM apt_v_nbu_job j, var \nWHERE \nclient_id IN (${hosts})\nAND j.start_date >= sysdate - var.nbrOfDays\nGROUP BY \nclient_id,\npolicy_id\n)\nSELECT \nt1.*,\nNVL(TO_CHAR(t2.last_backup,'MM/DD/YYYY HH:MI'),'<font color=red>No backup in '||var.nbrOfDays||' days</font>') last_backup\nFROM t1,t2,var\nWHERE t1.client_id = t2.client_id (+)\nAND t1.policy_id = t2.policy_id (+)"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
