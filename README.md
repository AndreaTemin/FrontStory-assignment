ServerSide - TEST
#################
# Campaign Cost & Revenue Daily Report
## Data
This test contains two files located in a public s3 bucket.
For each file, each line represents a campaign's cost or revenue.
* cost https://s3.amazonaws.com/frontstory-test-data/server-side/cost_1.csv
* revenue https://s3.amazonaws.com/frontstory-test-data/server-side/revenue_1.csv
## Instructions
Go over the entire instructions before you start coding. Write a script in python (or your preferred language) to
aggregate the data to a single output file.
1. Aggregate the data in the files daily per campaign.
2. Enrich the data with the following calculated fields:
a. UV = revenue / clicks
b. CPC = cost / clicks
c. ROI = UV / CPC
d. Profit = revenue - cost
3. For these files the timezones are in EST. Since our system is global and might get data from other timezones, it
is required to convert them to UTC.
4. Allow date_from and date_to parameters to get the data on a specific time frame.
5. Final columns expected in the report:
a. date (YYYY/MM/DD)
b. campaign_id
c. campaign_name
e. total_revenue
f. total_cost
g. total_profit
h. total_clicks
i. total_roi
j. avg_cpc
6. (Optional) Add the following columns as well:
k. hourly_avg_revenue (Average revenue of the campaign per hour)
l. positive_profit_hours (Amount of hours where profit > 0)
Example final row:
tal_revenue total_cost total_profit total_clicks total_roi avg_cpc hourly_avg_revenue positive_profit_hours
339 0.770 -0.430 11 0.440 0.07 0.048 7
7. Imagine the data from the s3 files were in 2 tables: cost_report and revenue_report. Write an SQL query that
returns the same output as the python script.
Good luck!