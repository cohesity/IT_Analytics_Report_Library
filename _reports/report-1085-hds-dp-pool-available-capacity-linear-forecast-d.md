---
title: "HDS DP Pool Available Capacity Linear Forecast.D"
report_id: 1085
rtd_name: "HDS DP Pool Available Capacity Linear Forecast.D.rtd"
description: "HDS DP Pool Available Capacity Linear Forecast"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 10/31/2012\n--Computes the future capacity of an array based on \n--Linear Regression (Linear) Sum of squares linear algorithm y=mX+b\n--This is a drill down report that can't run stand alone\n--TemplateName: HDSDPPoolAvailableCapacityLinearForecastD\nWITH \nd0 AS (\nSELECT\nDECODE('${TheGroupBy}','Day',1,'Week',7,'Month',31,'Quarter',93,'Year',365.24) nbr_of_days,\n--Limit the forecasting periods to 48\nCASE \nWHEN to_number('${TheForecastPeriods}') > 48 THEN 48 \nELSE to_number('${TheForecastPeriods}') END forecast_periods\nFROM dual\n),\na0 AS (--Get all the capacity merics for each period\nSELECT \narray_name,\npool_id,\nTRUNC(log_date,DECODE('${TheGroupBy}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) log_date,\nROW_NUMBER() over (PARTITION BY array_name, pool_id ORDER BY array_name, pool_id) row_number,\nMAX(available_kb/1024/1024) available\nFROM aps_v_hds_journal_pool_log\nWHERE log_date BETWEEN ${startDate} AND ${endDate}\nAND array_name = '${TheArrayName}'\nAND pool_id = '${ThePoolID}'\nAND pool_function = 5\nGROUP BY array_name, pool_id, trunc(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY'))\n),\na1 AS (\nSELECT \nROWNUM period,\nlog_date,\navailable,\nREGR_SLOPE(available,ROWNUM) OVER (PARTITION BY array_name) slope,\nREGR_INTERCEPT(available, ROWNUM) OVER (PARTITION BY array_name) y_intercept\nFROM a0\nORDER BY 1\n),\np0 AS (--Find the last period so you can forecast past it\nSELECT \nMAX(period) last_period,\nMAX(log_date) last_date\nFROM a1\n)\nSELECT\nlog_date,\nround(available,2) available,\n0 future_available,\nperiod*slope+y_intercept trend_line--Future values can be determined for any period unsing this formula\nFROM a1, p0\nUNION ALL --Future\nSELECT \nTRUNC(the_date,DECODE('${TheGroupBy}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) log_date,\n0 available,\nROUND((period+ROWNUM)*slope+y_intercept,2) future_available,\n(period+ROWNUM)*slope+y_intercept trend_line\nFROM a1,p0,d0, TABLE(rtd.APTlistOfDates(p0.last_date+d0.nbr_of_days,p0.last_date+(d0.forecast_periods*d0.nbr_of_days),DECODE('${TheGroupBy}','Day',11,'Week',12,'Month',13,'Quarter',14,'Year',15))) the_dates\nWHERE period = p0.last_period"
has_explanation: false
products: []
categories: []
product_slugs: []
category_slugs: []
---
