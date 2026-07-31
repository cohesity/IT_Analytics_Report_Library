---
title: "Avamar Client Summary"
report_id: 970
rtd_name: "Avamar Client Summary.rtd"
description: "Avamar Client Summary"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nSELECT\nclient_id, \nc.hostname client,\nagent_version, \nos_type, \nplugin_backup, \nmaster_server_id, \ns.hostname master_server,\navm_domain_name, \nallow_overtime, \nallow_user_snapup, \nallow_user_snapup_filesel, \ncan_page, \noverride_dataset, \nenabled, \nhas_backups, \noverride_init_ret_policy, \nis_registered, \nrestore_only, \nis_override_ret_policy, \nbackup_date, \ncheckin_date, \ncreated_date, \nmodified_date, \nregistered_date, \ncid, \novertime_option, \npage_address, \npage_addr_locked,\npage_port, \noverride_retry_count, \nretry_count, \ncontact_email, \ncontact_location, \ncontact_name,\ncontact_notes, \ncontact_phone,\ntimeout, \noverride_timeout\nFROM apt_v_avm_clients avc, apt_v_server c, apt_v_server s\nWHERE client_id IN (${hosts})\nAND client_id = c.server_id\nAND master_server_id = s.server_id"
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
