---
title: "Avamar Node Available Capacity Linear Forecast"
report_id: 975
rtd_name: "Avamar Node Available Capacity Linear Forecast.rtd"
description: "Avamar Node Available Capacity Linear Forecast"
problem_statement: "I need to be able to see when I will run out of capacity on my Avamar nodes."
author: "rich.rose@aptare.com\n"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 12/07/2012\n--Computes the future capacity of an Avamar Node based on \n--Linear Regression (Linear) Sum of squares linear algorithm y=mX+b\n--This is a drill down report that can't run stand alone\n--TemplateName: AvamarNodeAvailableCapacityLinearForecastD\nWITH \nd0 AS (\nSELECT\nDECODE('${freeCombo1}','Day',1,'Week',7,'Month',31,'Quarter',93,'Year',365.24) nbr_of_days,\nto_number('${freeCombo2}') forecast_periods\nFROM dual\n),\na0 AS (--Get all the capacity merics for each period\nSELECT \nmaster_server_id,\nnode_id,\nTRUNC(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) log_date,\nROW_NUMBER() over (PARTITION BY master_server_id, node_id ORDER BY master_server_id, node_id) row_number,\nROUND(MAX((capacity_mb - used_mb)/1024),2) available\nFROM apt_v_avm_node_space_log ansl, apt_v_server s \nWHERE log_date BETWEEN ${startDate} AND ${endDate}\nAND master_server_id = s.server_id\nAND s.hostname||' - '||node_id = '${queryCombo1}'\nGROUP BY master_server_id, node_id, trunc(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY'))\n),\na1 AS (\nSELECT \nROWNUM period,\nlog_date,\navailable,\nREGR_SLOPE(available,ROWNUM) OVER (PARTITION BY master_server_id) slope,\nREGR_INTERCEPT(available, ROWNUM) OVER (PARTITION BY master_server_id) y_intercept\nFROM a0\nORDER BY 1\n),\np0 AS (--Find the last period so you can forecast past it\nSELECT \nMAX(period) last_period,\nMAX(log_date) last_date\nFROM a1\n)\nSELECT\nlog_date,\nround(available,2) available,\n0 future_available,\nperiod*slope+y_intercept trend_line--Future values can be determined for any period using this formula\nFROM a1, p0\nUNION ALL --Future\nSELECT \nTRUNC(the_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) log_date,\n0 available,\nROUND((period+ROWNUM)*slope+y_intercept,2) future_available,\n(period+ROWNUM)*slope+y_intercept trend_line\nFROM a1,p0,d0, TABLE(rtd.APTlistOfDates(p0.last_date+d0.nbr_of_days,p0.last_date+(d0.forecast_periods*d0.nbr_of_days),DECODE('${freeCombo1}','Day',11,'Week',12,'Month',13,'Quarter',14,'Year',15))) the_dates\nWHERE period = p0.last_period"
has_explanation: false
products: [{"slug": "backup-manager-emc-avamar", "name": "EMC Avamar"}]
categories: []
product_slugs: ["backup-manager-emc-avamar"]
category_slugs: []
---
