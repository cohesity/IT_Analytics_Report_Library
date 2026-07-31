---
title: "Avamar Schedules Summary"
report_id: 966
rtd_name: "Avamar Schedules Summary.rtd"
description: "Avamar Schedules Summary"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "\n--Author: rich.rose@aptare.com\n--Last Modified: 05/10/2012\nSELECT\ngsan_system_id, \ngsan_system_name, \nschedule_id, \navm_domain_id, \nschedule_name, \nis_enabled, \nis_link, \nis_override_endtime, \nis_read_only, \nis_fixed_interval, \ninterval_mod, \nparent_schedule_id, \nfirst_start_date, \nlast_check_date, \nlast_start_date, \nstart_duration, \nstart_date, \nend_date, \nrecurrence_counter, \nrecurrence_interval, \ntime_zone_id, \ntotal_duration\nend_policy, \nend_recurrence, \ndescription \nFROM apt_v_avm_schedules"
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
