---
title: "Array Allocated Linear Forecast.D"
report_id: 1089
rtd_name: "Array Allocated Linear Forecast.D.rtd"
description: "Array Allocated Linear Forecast"
problem_statement: ""
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
cohesity_supported: false
ita_versions: ""
thumbnail: false
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 03/30/2012\n--Computes the future capacity of an array based on \n--Linear Regression (Linear) Sum of squares linear algorithm y=mX+b\nWITH \nd0 AS (\nSELECT\nDECODE('${TheGroupBy}','Day',1,'Week',7,'Month',31,'Quarter',93,'Year',365.24) nbr_of_days,\n--Limit the forecasting periods to 48\nCASE \nWHEN to_number('${TheForecastPeriods}') > 48 THEN 48 \nELSE to_number('${TheForecastPeriods}') END forecast_periods\nFROM dual\n),\na0 as (\nSELECT \narray_name,\ntrunc(log_date,DECODE('${TheGroupBy}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) log_date,\nmax(allocated_gb) allocated_gb,\nmax(capacity_gb) capacity_gb,\nmax(capacity_gb) - max(allocated_gb) available_gb\nFROM aps_v_storage_array_log\nWHERE log_date BETWEEN ${startDate} AND ${endDate}\nAND array_name = '${TheArrayName}' \nAND array_name is not null\nGROUP BY array_name,trunc(log_date,DECODE('${TheGroupBy}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY'))\n),\na1 AS (\nSELECT \nrownum period,\nlog_date,\nallocated_gb,\ncapacity_gb,\nREGR_SLOPE(allocated_gb,rownum) over (partition by array_name) slope,\nREGR_INTERCEPT(allocated_gb, rownum) over (partition by array_name) y_intercept\nFROM a0\nORDER BY 1\n),\nMP AS (--Find the last period so you can forecast past it\nSELECT \nmax(period) last_period,\nmax(log_date) last_date\nFROM a1\n)\nSELECT\nlog_date,\nround(allocated_gb,2) allocated_gb,\n0 future_allocated,\nround(capacity_gb-allocated_gb,2) available_gb,\n0 future_available,\nperiod*slope+y_intercept trend_line--Future values can be determined for any period unsing this formula\nFROM a1, mp\nUNION ALL --Future\nSELECT \ntrunc(the_date,DECODE('${TheGroupBy}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) log_date,\n0 allocated_gb,\nround((period+rownum)*slope+y_intercept,2) future_allocated,\n0 available_gb,\nround(capacity_gb - ((period+rownum)*slope+y_intercept),2) future_available,\n(period+rownum)*slope+y_intercept trend_line\nFROM a1,mp,d0, TABLE(rtd.APTlistOfDates(mp.last_date+d0.nbr_of_days,mp.last_date+(d0.forecast_periods*d0.nbr_of_days),DECODE('${TheGroupBy}','Day',11,'Week',12,'Month',13,'Quarter',14,'Year',15))) the_dates\nWHERE period = mp.last_period"
has_explanation: false
products: []
categories: []
product_slugs: []
category_slugs: []
---
