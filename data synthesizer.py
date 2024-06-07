import pandas as pd
import random


years = ['2023', '2024', '2025', '2026']

for year in years:
    yearly_budget = 100000
    january_budget      = 0.03333333333 * 100000
    february_budget     = 0.08333333333 * 100000
    march_budget        = 0.1333333333 * 100000
    april_budget        = 0.1333333333 * 100000
    may_budget          = 0.1033333333 * 100000
    june_budget         = 0.1033333333 * 100000
    july_budget         = 0.08833333333 * 100000
    august_budget       = 0.08833333333 * 100000
    september_budget    = 0.07833333333 * 100000
    october_budget      = 0.07833333333 * 100000
    november_budget     = 0.04333333333 * 100000
    december_budget     = 0.03333333333 * 100000

    monthly_budgets = [january_budget, february_budget, march_budget, april_budget, may_budget, june_budget, july_budget,
                       august_budget, september_budget, october_budget, november_budget, december_budget]

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    on_season_months = ["March", "April", "May", "June",
              "July", "August", "September"]

    cpm = []
    ctr = []
    cpc = []
    conv_rate = []
    impr = []
    conversions = []
    cpa = []
    clicks = []

    counter = 0
    for month in months:
        if month not in on_season_months:
            cpm.append(random.randrange(200, 700) / 1000)
            ctr.append(random.randrange(200, 700) / 10000)
            conv_rate.append(random.randrange(200, 700) / 10000)
        if month in on_season_months:
            cpm.append(random.randrange(100, 200) / 10000)
            ctr.append(random.randrange(100, 200) / 1000)
            conv_rate.append(random.randrange(100, 200) / 1000)
        impr.append(round(monthly_budgets[counter] / cpm[counter]) * 1000)
        clicks.append(round(impr[counter] * ctr[counter]))
        conversions.append(clicks[counter] * conv_rate[counter])
        cpc.append(monthly_budgets[counter] / clicks[counter])
        cpa.append(monthly_budgets[counter] / conversions[counter])
        counter += 1

    print(cpm)

    monthly_data = {
        'spend': monthly_budgets,
        'impr': impr,
        'clicks': clicks,
        'conversions': conversions,
        'cpm': cpm,
        'ctr': ctr,
        'conv_rate': conv_rate,
        'cpa': cpa,
        'cpc': cpc
    }

    quarter1_cost = monthly_budgets[0] + monthly_budgets[1] + monthly_budgets[2]
    quarter2_cost = monthly_budgets[3] + monthly_budgets[4] + monthly_budgets[5]
    quarter3_cost = monthly_budgets[6] + monthly_budgets[7] + monthly_budgets[8]
    quarter4_cost = monthly_budgets[9] + monthly_budgets[10] + monthly_budgets[11]
    quarterly_cost = [quarter1_cost, quarter2_cost, quarter3_cost, quarter4_cost]

    quarter1_impr = impr[0] + impr[1] + impr[2]
    quarter2_impr = impr[3] + impr[4] + impr[5]
    quarter3_impr = impr[6] + impr[7] + impr[8]
    quarter4_impr = impr[9] + impr[10] + impr[11]
    quarterly_impr = [quarter1_impr, quarter2_impr, quarter3_impr, quarter4_impr]

    quarter1_clicks = clicks[0] + clicks[1] + clicks[2]
    quarter2_clicks = clicks[3] + clicks[4] + clicks[5]
    quarter3_clicks = clicks[6] + clicks[7] + clicks[8]
    quarter4_clicks = clicks[9] + clicks[10] + clicks[11]
    quarterly_clicks = [quarter1_clicks, quarter2_clicks, quarter3_clicks, quarter4_clicks]

    quarter1_conversions = conversions[0] + conversions[1] + conversions[2]
    quarter2_conversions = conversions[3] + conversions[4] + conversions[5]
    quarter3_conversions = conversions[6] + conversions[7] + conversions[8]
    quarter4_conversions = conversions[9] + conversions[10] + conversions[11]
    quarterly_conversions = [quarter1_conversions, quarter2_conversions, quarter3_conversions, quarter4_conversions]

    quarter1_ctr = quarter1_clicks / quarter1_impr
    quarter2_ctr = quarter2_clicks / quarter2_impr
    quarter3_ctr = quarter3_clicks / quarter3_impr
    quarter4_ctr = quarter4_clicks / quarter4_impr
    quarterly_ctr = [quarter1_ctr, quarter2_ctr, quarter3_ctr, quarter4_ctr]

    quarter1_conv_rate = quarter1_conversions / quarter1_clicks
    quarter2_conv_rate = quarter2_conversions / quarter2_clicks
    quarter3_conv_rate = quarter3_conversions / quarter3_clicks
    quarter4_conv_rate = quarter4_conversions / quarter4_clicks
    quarterly_conv_rate = [quarter1_conv_rate, quarter2_conv_rate, quarter3_conv_rate, quarter4_conv_rate]

    quarter1_cpm = (quarter1_cost / quarter1_impr) * 1000
    quarter2_cpm = (quarter2_cost / quarter2_impr) * 1000
    quarter3_cpm = (quarter3_cost / quarter3_impr) * 1000
    quarter4_cpm = (quarter4_cost / quarter4_impr) * 1000
    quarterly_cpm = [quarter1_cpm, quarter2_cpm, quarter3_cpm, quarter4_cpm]

    quarter1_cpa = (quarter1_cost / quarter1_conversions)
    quarter2_cpa = (quarter2_cost / quarter2_conversions)
    quarter3_cpa = (quarter3_cost / quarter3_conversions)
    quarter4_cpa = (quarter4_cost / quarter4_conversions)
    quarterly_cpa = [quarter1_cpa, quarter2_cpa, quarter3_cpa, quarter4_cpa]

    quarter1_cpc = (quarter1_cost / quarter1_clicks)
    quarter2_cpc = (quarter2_cost / quarter2_clicks)
    quarter3_cpc = (quarter3_cost / quarter3_clicks)
    quarter4_cpc = (quarter4_cost / quarter4_clicks)
    quarterly_cpc = [quarter1_cpc, quarter2_cpc, quarter3_cpc, quarter4_cpc]

    quarterly_data = {
        'impr': quarterly_impr,
        'clicks': quarterly_clicks,
        'ctr': quarterly_ctr,
        'cost': quarterly_cost,
        'conversions': quarterly_conversions,
        'cpa': quarterly_cpa,
        'cpc': quarterly_cpc,
        'conv rate': quarterly_conv_rate,
        'cpm': quarterly_cpm
    }

    monthly = pd.DataFrame(monthly_data)
    monthly.to_csv(f'{year}-monthly.csv', index=False)

    quarterly = pd.DataFrame(quarterly_data)
    quarterly.to_csv(f'{year}-quarterly.csv', index=False)

#
# print('x')
