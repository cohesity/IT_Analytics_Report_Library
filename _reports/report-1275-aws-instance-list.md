---
title: "AWS Instance List"
report_id: 1275
rtd_name: "AWS Instance List.rtd"
description: "AWS Instance List"
problem_statement: "TBD"
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@veritas.com\n--Last Modified: 07/02/2020\nSELECT\n  i.via_account_id,\n  i.resource_id,\n  i.host_id,\n  i.account_id,\n  a.alias,\n  i.name,\n  i.scope_selector_name,\n  i.region_id,\n  r.name AS region,\n  i.availability_zone_id,\n  z.name AS availability_zone,\n  i.tenancy,\n  i.owner,\n  i.type,\n  i.virtualization,\n  i.hypervisor,\n  i.platform,\n  i.architecture,\n  i.monitoring,\n  i.launched,\n  i.state_code,\n  i.state,\n  i.instance_status,\n  i.system_status,\n  i.image_resource_id,\n  i.is_ebs_optimized,\n  i.key_pair_resource_id,\n  i.root_device,\n  i.root_device_type,\n  i.vpc_resource_id,\n  i.creation_date,\n  i.last_updated,\n  i.id,\n  i.marked_for_delete\nFROM\n  sdk_v_aws_account a, \n  sdk_v_aws_ec2_instance i, \n  sdk_v_aws_region r, \n  sdk_v_aws_availability_zone z\nWHERE\n  i.account_id = a.id\n  AND i.region_id = r.id\n  AND i.availability_zone_id = z.id"
has_explanation: false
products: [{"slug": "public-cloud-aws", "name": "AWS"}]
categories: []
product_slugs: ["public-cloud-aws"]
category_slugs: []
---
