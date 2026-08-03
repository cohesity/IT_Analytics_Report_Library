---
title: "HDS DP Pool Available Capacity POP Forecast.D"
report_id: 1088
rtd_name: "HDS DP Pool Available Capacity POP Forecast.D.rtd"
description: "HDS DP Pool Available Capacity POP Forecast"
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
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 03/30/2012\n--Computes the future capacity of an array based on \n--a Period over Period forecasting method\n--This is a drill down report that can't run stand alone\n--TemplateName: HDSDPPoolAvailableCapacityPOPForecast.D\nWITH \nd0 AS (--Convert the human readable date selection to numeric values\nSELECT\nDECODE('${TheGroupBy}','Day',1,'Week',7,'Month',31,'Quarter',93,'Year',365.24) nbr_of_days,\n--Limit the forecasting periods to 48\nCASE \nWHEN to_number('${TheForecastPeriods}') > 48 THEN 48 \nELSE to_number('${TheForecastPeriods}') END forecast_periods,\n'${TheGroupBy}' the_group_by --Need this for the drilldown\nFROM dual\n),\na0 AS (--Get all the capacity merics for each period\nSELECT \nstorage_array_id,\npool_id,\nTRUNC(log_date,DECODE('${TheGroupBy}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) log_date,\nROW_NUMBER() OVER (PARTITION BY storage_array_id,  pool_id ORDER BY storage_array_id,  pool_id) row_number,\nROUND(MAX(available_kb/1024/1024),2) available\nFROM aps_v_hds_journal_pool_log\nWHERE log_date BETWEEN ${startDate} AND ${endDate}\nAND array_name = '${TheArrayName}'\nAND pool_id = '${ThePoolID}'\nAND pool_function = 5\nGROUP BY storage_array_id,pool_id,trunc(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY'))\n),\np0 AS (--Get the first and last period number for each array & pool \nSELECT\nstorage_array_id,\npool_id,\nMIN(row_number) first_period_number, --First period will always be 1\nMAX(row_number) last_period_number, --Last period is the current period or last time data was collected\nmin(log_date) first_period_date,\nMAX(log_date) last_period_date,\nCOUNT(log_date) period_count\nFROM a0\nGROUP BY \nstorage_array_id,\npool_id\n),\npop1 AS (--Get the first and last period metrics based on the row number of the periods\nSELECT\na0.storage_array_id, a0.pool_id,\nMAX(last_period_number) nbr_of_periods,\nSUM(DECODE(a0.row_number,first_period_number,a0.available,0)) first_available,\nSUM(DECODE(a0.row_number,last_period_number,a0.available,0)) last_available\nFROM a0,p0\nWHERE a0.storage_array_id = p0.storage_array_id\nAND a0.pool_id = p0.pool_id\nGROUP BY a0.storage_array_id, a0.pool_id\n),\npop2 AS (--Calculate the Period Over Period Changes\nSELECT\nstorage_array_id, \npool_id,\nfirst_available,\nlast_available,\nROUND(last_available - first_available,2) pop_available_delta,\nROUND((last_available - first_available ) / DECODE(nbr_of_periods,0,null,nbr_of_periods),2) pop_available_trend\nFROM pop1\n) \nSELECT --Plot the prior history\na0.log_date, \na0.available,\n0 future_available,\npop2.last_available - (pop2.pop_available_trend*(period_count-ROWNUM)) available_trend_line\nFROM a0, p0, pop2\nWHERE a0.storage_array_id = pop2.storage_array_id\nAND a0.pool_id = pop2.pool_id\nAND a0.storage_array_id = p0.storage_array_id\nAND a0.pool_id = p0.pool_id\nUNION ALL --Future values\nSELECT \ntrunc(the_date,DECODE('${TheGroupBy}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) log_date,\n0 available,\npop2.last_available + (pop2.pop_available_trend*ROWNUM) future_available,\npop2.last_available + (pop2.pop_available_trend*ROWNUM) available_trend_line\nFROM a0, pop2, d0, p0, TABLE(rtd.APTlistOfDates(p0.last_period_date+d0.nbr_of_days,p0.last_period_date+(d0.forecast_periods*d0.nbr_of_days),DECODE('${TheGroupBy}','Day',11,'Week',12,'Month',13,'Quarter',14,'Year',15))) the_dates\nWHERE a0.storage_array_id = pop2.storage_array_id\nAND a0.pool_id = pop2.pool_id\nAND a0.storage_array_id = p0.storage_array_id\nAND a0.pool_id = p0.pool_id\nAND a0.row_number = p0.period_count --Only need the last row\nORDER BY 1"
has_explanation: false
products: []
categories: []
product_slugs: []
category_slugs: []
---
