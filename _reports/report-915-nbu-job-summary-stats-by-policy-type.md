---
title: "NBU Job Summary Stats by Policy Type"
report_id: 915
rtd_name: "NBU Job Summary Stats by Policy Type.rtd"
description: "NBU Job Summary Stats by Policy Type"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 08/09/2012\n--This will display job Information for the selected policy type\nSELECT\nnj.master_host_name,\nnj.client_host_name,\nnp.policy_id,\nnp.policy_name, \nnp.policy_type_name,\nschedule_name,\nschedule_type_name,\nretention_days,\nCASE\n  WHEN ns.retention_days > 0    AND ns.retention_days <= 7     THEN '1 Week'\n  WHEN ns.retention_days > 7    AND ns.retention_days <= 14    THEN '2 Weeks'\n  WHEN ns.retention_days > 14   AND ns.retention_days <= 31    THEN '1 Month'\n  WHEN ns.retention_days > 31   AND ns.retention_days <= 90    THEN '3 Months'\n  WHEN ns.retention_days > 90   AND ns.retention_days <= 186   THEN '6 Months'\n  WHEN ns.retention_days > 186  AND ns.retention_days <= 365   THEN '1 Yr'\n  WHEN ns.retention_days > 365  AND ns.retention_days <= 1095  THEN '3 Yrs'\n  WHEN ns.retention_days > 1095 AND ns.retention_days <= 2555  THEN '7 Yrs'\n  WHEN ns.retention_days > 2555 AND ns.retention_days <= 5475  THEN '15 Yrs'\n  WHEN ns.retention_days > 5475 OR  ns.retention_days = 0 THEN 'Over 15 Yrs'\nEND retention_period,\ncount(nj.job_id) nbr_of_jobs,\nsum(nj.kilobytes/1024/1024) size_gb,\nREPLACE(aptStringConcat(DISTINCT pf.pathname),',','<br />') paths,\nREPLACE(aptStringConcat(DISTINCT ntm.media_name),',','<br />') tapes\nFROM apt_v_nbu_job nj, apt_v_nbu_policy np, apt_v_nbu_schedule ns,apt_v_nbu_policy_file pf, apt_v_nbu_job_tape_media jtm, apt_v_nbu_tape_media ntm\nWHERE nj.start_date BETWEEN ${startDate} AND ${endDate}\nAND nj.client_id IN (${hosts})\nAND nj.policy_id = np.policy_id\nAND nj.policy_id = pf.policy_id\nAND nj.schedule_id = ns.schedule_id (+)\nAND nj.job_id = jtm.job_id (+)\nAND jtm.tape_media_id = ntm.tape_media_id\nAND '${freeCombo1}' IN \nCASE \nWHEN '${freeCombo1}'     LIKE 'All' THEN '${freeCombo1}' \nWHEN np.policy_type_name LIKE 'NDMP' THEN 'NDMP'\nWHEN np.policy_type_name LIKE 'Standard' THEN 'Standard'\nWHEN np.policy_type_name LIKE 'MS-Windows' THEN 'MS-Windows'\nWHEN np.policy_type_name LIKE 'Oracle' THEN 'Oracle'\nWHEN np.policy_type_name LIKE 'Vault' THEN 'Vault'\nWHEN np.policy_type_name LIKE 'FlashBackup' THEN 'FlashBackup'\nWHEN np.policy_type_name LIKE 'MS-Exchange Server' THEN 'MS-Exchange Server'\nWHEN np.policy_type_name LIKE 'MS-SQL' THEN 'MS-SQL'\nWHEN np.policy_type_name LIKE 'MS-Sharepoint' THEN 'MS-Sharepoint'\nWHEN np.policy_type_name LIKE 'NBU-Catalog' THEN 'NBU-Catalog'\nEND\nGROUP BY\nnj.master_host_name,\nnj.client_host_name,\nnp.policy_id,\nnp.policy_name, \nnp.policy_type_name,\nschedule_name,\nschedule_type_name,\nretention_days,\nCASE\n  WHEN ns.retention_days > 0    AND ns.retention_days <= 7     THEN '1 Week'\n  WHEN ns.retention_days > 7    AND ns.retention_days <= 14    THEN '2 Weeks'\n  WHEN ns.retention_days > 14   AND ns.retention_days <= 31    THEN '1 Month'\n  WHEN ns.retention_days > 31   AND ns.retention_days <= 90    THEN '3 Months'\n  WHEN ns.retention_days > 90   AND ns.retention_days <= 186   THEN '6 Months'\n  WHEN ns.retention_days > 186  AND ns.retention_days <= 365   THEN '1 Yr'\n  WHEN ns.retention_days > 365  AND ns.retention_days <= 1095  THEN '3 Yrs'\n  WHEN ns.retention_days > 1095 AND ns.retention_days <= 2555  THEN '7 Yrs'\n  WHEN ns.retention_days > 2555 AND ns.retention_days <= 5475  THEN '15 Yrs'\n  WHEN ns.retention_days > 5475 OR  ns.retention_days = 0 THEN 'Over 15 Yrs'\nEND"
has_explanation: false
products: [{"slug": "backup-manager-veritas-netbackup", "name": "Veritas NetBackup"}]
categories: []
product_slugs: ["backup-manager-veritas-netbackup"]
category_slugs: []
---
