---
title: "EMC VNX Individual Pool Capacity Forecast"
report_id: 1174
rtd_name: "EMC VNX Individual Pool Capacity Linear Forecast.rtd"
description: "EMC VNX Individual Pool Capacity Forecast"
problem_statement: "Show me when my VNX pools will run out of capacity or how much capacity will be required in the future"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 04/13/2016\n--Computes the future capacity of an array based on \n--Linear Regression (Linear) Sum of squares linear algorithm y=mX+b\nWITH \nd0 AS (\nSELECT\nDECODE('${freeCombo1}','Day',1,'Week',10,'Month',31,'Quarter',93,'Year',365.24) nbr_of_days,\nTO_NUMBER('${freeCombo2}') forecast_periods,\n'${freeCombo3}' unit,\nDECODE('${freeCombo3}', 'GB',1,'TB',1024,'PB',(1024*1024)) div_by \nFROM apt_v_dual\n),\nt0 AS (--Get all indiviapt_v_dual pools for each period\nSELECT \narray_name||' - '||pool_name entity,\nTRUNC(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) log_date,\nMAX(total_subscribed_capacity_gb) subscribed,\nMAX(available_capacity_gb) + MAX(consumed_capacity_gb) capacity,\nMAX(consumed_capacity_gb) used,\nMAX(available_capacity_gb) available\nFROM aps_v_emc_cla_storage_pool_log\nWHERE log_date BETWEEN ${startDate} AND ${endDate}\nAND array_name||' - '||pool_name = '${queryCombo1}'\nGROUP BY array_name||' - '||pool_name,\nTRUNC(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY'))\n),\na0 AS (--Aggregate them \nSELECT \nentity,\nlog_date,\nROW_NUMBER() OVER (PARTITION BY entity  ORDER BY entity) row_number,\nsubscribed,\ncapacity,\nused,\navailable\nFROM t0\nORDER BY entity, log_date\n),\na1 AS (\nSELECT \nROWNUM period,\nlog_date,\nsubscribed,\ncapacity,\nused,\navailable,\nREGR_SLOPE(available,ROWNUM) OVER (PARTITION BY entity) a_slope,\nREGR_INTERCEPT(available, ROWNUM) OVER (PARTITION BY entity) a_y_intercept,\nREGR_SLOPE(used,ROWNUM) OVER (PARTITION BY entity) u_slope,\nREGR_INTERCEPT(used, ROWNUM) OVER (PARTITION BY entity) u_y_intercept\nFROM a0\nORDER BY 1,2\n),\np0 AS (--Find the last period so you can forecast past it\nSELECT \nMAX(period) last_period,\nMAX(log_date) last_date\nFROM a1\n)\nSELECT\nTO_CHAR(log_date,'MM/DD/YYYY') log_date,\nROUND(subscribed/div_by,2) subscribed,\nROUND(capacity/div_by,2) capacity,\nROUND(available/div_by,2) available,\n0 future_available,\nROUND(((period*a_slope)+a_y_intercept)/div_by,2) a_trend_line,\nROUND(used/div_by,2) used,\n0 future_used,\nROUND(((period*u_slope)+u_y_intercept)/div_by,2) u_trend_line,\nunit\nFROM a1, p0, d0\nUNION ALL --Future\nSELECT \nTO_CHAR(TRUNC(the_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')),'MM/DD/YYYY') log_date,\nROUND(subscribed/div_by,2) subscribed,\nROUND(capacity/div_by,2) capacity,\n0 available,\nROUND(((period+ROWNUM)*a_slope+a_y_intercept)/div_by,2) future_available,\nROUND(((period+ROWNUM)*a_slope+a_y_intercept)/div_by,2) a_trend_line,\n0 used,\nROUND(((period+ROWNUM)*u_slope+u_y_intercept)/div_by,2) future_used,\nROUND(((period+ROWNUM)*u_slope+u_y_intercept)/div_by,2) u_trend_line,\nunit\nFROM a1, p0, d0, \nTABLE(rtd.APTlistOfDates(p0.last_date+d0.nbr_of_days,p0.last_date+(d0.forecast_periods*d0.nbr_of_days),DECODE('${freeCombo1}','Day',11,'Week',12,'Month',13,'Quarter',14,'Year',15))) the_dates\nWHERE period = p0.last_period\nAND ROUND((period+ROWNUM)*a_slope+a_y_intercept,2) > 0"
has_explanation: false
products: [{"slug": "capacity-manager-emc-reports", "name": "EMC Reports"}]
categories: []
product_slugs: ["capacity-manager-emc-reports"]
category_slugs: []
---
