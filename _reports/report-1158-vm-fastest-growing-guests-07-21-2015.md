---
title: "VM Fastest Growing Guests 07/21/2015"
report_id: 1158
rtd_name: "VM Fastest Growing Guests.rtd"
description: "VM Fastest Growing Guests"
problem_statement: "I need to know which guests are burning through my Tier 1 storage at the fastest rate."
author: ""
modified_date: "2023-07-14"
download_count: 0
has_video: true
video_url: "https://www.youtube.com/watch?v=ibsDToYk04U"
cohesity_supported: false
ita_versions: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 10/19/2015\nWITH \nvar AS (\nSELECT\nROUND((${endDate} - ${startDate}),2) nbrOfDays,\nDECODE('${freeCombo1}',\n'KB',1,'MB',1024,'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\nt1 AS (\nSELECT\np.partition_id,\nTRUNC(l.log_date,DECODE('${freeCombo2}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) log_date,\nROW_NUMBER() OVER (PARTITION BY p.partition_id ORDER BY p.partition_id) row_number,\nROUND(MAX(l.total_size_kb/div_by),2) total_size\nFROM apt_v_vmw_virtual_machine_log l, apt_v_partition p, var\nWHERE p.partition_id = l.partition_id\nAND l.log_date BETWEEN ${startDate} AND ${endDate}\nAND p.collection_status != 3\nAND p.host_id IN (${hosts})\nAND l.total_size_kb > 0\n--FIXME this table has both guests and ESX servers. filter out ESX Servers\nGROUP BY \np.partition_id, \nTRUNC(l.log_date,DECODE('${freeCombo2}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY'))\n),\nlin1 AS (--Get the Linear Growth statistics\nSELECT \npartition_id,\nROUND(REGR_SLOPE(total_size,row_number),2) linear_trend,\nREGR_R2(total_size,row_number) r2_value,\nREGR_AVGX(total_size,row_number) avex,\nREGR_AVGY(total_size,row_number)  avey,\nREGR_INTERCEPT(total_size,row_number) y_intercept,\nREGR_COUNT(total_size,row_number) period_count,\nSTDDEV(total_size)  stddev\nFROM t1\nGROUP BY \npartition_id\n),\npop1 AS (--Get the Period over Period Numbers\nSELECT\nt1.partition_id, \nSUM(DECODE(t1.row_number,1,t1.total_size,0)) first_period_total_size,\nSUM(DECODE(t1.row_number,lin1.period_count,t1.total_size,0)) last_period_total_size\nFROM t1, lin1\nWHERE\nt1.partition_id = lin1.partition_id\nAND t1.row_number IN (1,lin1.period_count) --Only get the first and last period numbers\nGROUP BY\nt1.partition_id \n),\ng1 AS (--Calculate Growth\nSELECT\nlin1.partition_id,\nvm.partition_name,\nvm.host_name,\npop1.first_period_total_size,\npop1.last_period_total_size,\n(pop1.last_period_total_size - pop1.first_period_total_size) total_change,\n(pop1.last_period_total_size - pop1.first_period_total_size) / DECODE(pop1.first_period_total_size,0,NULL,pop1.first_period_total_size) simple_growth_rate,\nlinear_trend,\nr2_value,\navex,\navey,\ny_intercept,\nstddev,\nlin1.period_count,\nROUND((pop1.last_period_total_size - pop1.first_period_total_size ) / DECODE(lin1.period_count,0,NULL,lin1.period_count),2) pop_trend,\nPOWER((pop1.last_period_total_size / DECODE(pop1.first_period_total_size,0,NULL,pop1.first_period_total_size)),(1/DECODE(lin1.period_count,0,NULL,lin1.period_count))) - 1 compound_growth_rate\nFROM pop1, lin1, apt_v_vmw_virtual_machine vm\nWHERE pop1.partition_id = lin1.partition_id\nAND lin1.partition_id = vm.partition_id\n)\nSELECT \npartition_id,\npartition_name,\nhost_name,\nfirst_period_total_size,\nlast_period_total_size,\ntotal_change,\nsimple_growth_rate,\ncompound_growth_rate,\nDENSE_RANK() OVER (ORDER BY compound_growth_rate DESC) compound_growth_rank,\nperiod_count, \npop_trend,\nlinear_trend,\nr2_value,\navex,\navey,\ny_intercept,\nstddev\nFROM g1\nWHERE \ntotal_change > 0\nORDER BY compound_growth_rate DESC"
has_explanation: false
products: [{"slug": "virtualization-vmware", "name": "VMware"}]
categories: []
product_slugs: ["virtualization-vmware"]
category_slugs: []
---
