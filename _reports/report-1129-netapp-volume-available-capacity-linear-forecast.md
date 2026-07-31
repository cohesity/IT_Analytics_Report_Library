---
title: "NetApp Volume Available Capacity Linear Forecast"
report_id: 1129
rtd_name: "NetApp Volume Available Capacity Linear Forecast.rtd"
description: "NetApp Volume Available Capacity Linear Forecast"
problem_statement: "Shows when a NetApp Volume will run out of capacity using a Linear Regression algorithm."
author: "rich.rose@aptare.com"
modified_date: "2023-07-14"
download_count: 0
has_video: false
video_url: ""
thumbnail: true
has_sample: true
has_sql: true
sql_query: "--Author: rich.rose@aptare.com\n--Last Modified: 05/22/2014\n--Computes the future capacity of Data Domain based on \n--Linear Regression (Linear) Sum of squares linear algorithm y=mX+b\nWITH \nd0 AS (\nSELECT\nDECODE('${freeCombo1}','Day',1,'Week',7,'Month',31,'Quarter',93,'Year',365.24) nbr_of_days,\nto_number('${freeCombo2}') forecast_periods,\nDECODE('${freeCombo3}',\n'KB',1,'MB',(1024),'GB',(1024*1024),'TB',(1024*1024*1024),'PB',(1024*1024*1024*1024)) div_by \nFROM apt_v_dual\n),\na0 AS (--Get all the capacity merics for each period\nSELECT \nvl.nap_volume_id,\nTRUNC(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) log_date,\nROW_NUMBER() OVER (PARTITION BY vl.nap_volume_id ORDER BY vl.nap_volume_id) row_number,\nROUND(MAX((vl.total_size_kb - vl.used_size_kb)/div_by),2) available\nFROM aps_v_nap_volume_log vl, aps_v_nap_volume v, d0 \nWHERE log_date BETWEEN ${startDate} AND ${endDate}\nAND vl.nap_volume_id = v.nap_volume_id\nAND v.system_name|| '-' ||v.volume_name = '${queryCombo1}'\nGROUP BY vl.nap_volume_id, trunc(log_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY'))\n),\na1 AS (\nSELECT \nROWNUM period,\nlog_date,\navailable,\nREGR_SLOPE(available,ROWNUM) OVER (PARTITION BY nap_volume_id) slope,\nREGR_INTERCEPT(available, ROWNUM) OVER (PARTITION BY nap_volume_id) y_intercept\nFROM a0\nORDER BY 1\n),\np0 AS (--Find the last period so you can forecast past it\nSELECT \nMAX(period) last_period,\nMAX(log_date) last_date\nFROM a1\n)\nSELECT\nlog_date,\nround(available,2) available,\n0 future_available,\nperiod*slope+y_intercept trend_line--Future values can be determined for any period using this formula\nFROM a1, p0\nUNION ALL --Future\nSELECT \nTRUNC(the_date,DECODE('${freeCombo1}','Day','DD','Week','WW','Month','MM','Quarter','Q','Year','YY')) log_date,\n0 available,\nROUND((period+ROWNUM)*slope+y_intercept,2) future_available,\n(period+ROWNUM)*slope+y_intercept trend_line\nFROM a1,p0,d0, TABLE(rtd.APTlistOfDates(p0.last_date+d0.nbr_of_days,p0.last_date+(d0.forecast_periods*d0.nbr_of_days),DECODE('${freeCombo1}','Day',11,'Week',12,'Month',13,'Quarter',14,'Year',15))) the_dates\nWHERE period = p0.last_period"
has_explanation: false
products: [{"slug": "capacity-manager-general-all-storage-vendors", "name": "General (All Storage Vendors)"}]
categories: []
product_slugs: ["capacity-manager-general-all-storage-vendors"]
category_slugs: []
---
