import pandas as pd
from gpt4all import GPT4All

#next steps:
#feed the data into the LLM and generate some analysis from the synthetic data.
#create a multi-shot format to give it a template to follow

def data_delta(current_quarter, qoq_quarter, yoy_quarter, current_month, qoq_month, yoy_month, quarter_columns):
    qoq_quarter_delta = []
    yoy_quarter_delta = []
    qoq_month_delta = []
    yoy_month_delta = []
    counter = 0
    for i in quarter_columns:
        qoq_delta = (current_quarter[counter] - qoq_quarter[counter]) / qoq_quarter[counter]
        qoq_delta = round(qoq_delta * 10000)
        qoq_delta = qoq_delta / 100
        yoy_delta = (current_quarter[counter] - yoy_quarter[counter]) / yoy_quarter[counter]
        yoy_delta = round(yoy_delta * 10000)
        yoy_delta = yoy_delta / 100
        qoq_quarter_delta.append(
            {i: qoq_delta}
        )
        yoy_quarter_delta.append(
            {i: yoy_delta}
        )
        counter += 1

    for i in range(len(current_month['impr'])):
        spend_delta = (current_month['spend'][i] - qoq_month['spend'][i]) / qoq_month['spend'][i]
        spend_delta = round(spend_delta * 10000)
        spend_delta = spend_delta / 100
        impr_delta = (current_month['impr'][i] - qoq_month['impr'][i]) / qoq_month['impr'][i]
        impr_delta = round(impr_delta * 10000)
        impr_delta = impr_delta / 100
        clicks_delta = (current_month['clicks'][i] - qoq_month['clicks'][i]) / qoq_month['clicks'][i]
        clicks_delta = round(clicks_delta * 10000)
        clicks_delta = clicks_delta / 100
        conversions_delta = (current_month['conversions'][i] - qoq_month['conversions'][i]) / qoq_month['conversions'][i]
        conversions_delta = round(conversions_delta * 10000)
        conversions_delta = conversions_delta / 100
        cpm_delta = (current_month['cpm'][i] - qoq_month['cpm'][i]) / qoq_month['cpm'][i]
        cpm_delta = round(cpm_delta * 10000)
        cpm_delta = cpm_delta / 100
        ctr_delta = (current_month['ctr'][i] - qoq_month['ctr'][i]) / qoq_month['ctr'][i]
        ctr_delta = round(ctr_delta * 10000)
        ctr_delta = ctr_delta / 100
        conv_rate_delta = (current_month['conv_rate'][i] - qoq_month['conv_rate'][i]) / qoq_month['conv_rate'][i]
        conv_rate_delta = round(conv_rate_delta * 10000)
        conv_rate_delta = conv_rate_delta / 100
        cpa_delta = (current_month['cpa'][i] - qoq_month['cpa'][i]) / qoq_month['cpa'][i]
        cpa_delta = round(cpa_delta * 10000)
        cpa_delta = cpa_delta / 100
        cpc_delta = (current_month['cpc'][i] - qoq_month['cpc'][i]) / qoq_month['cpc'][i]
        cpc_delta = round(cpc_delta * 10000)
        cpc_delta = cpc_delta / 100
        qoq_month_delta.append({
            'spend': spend_delta,
            'impr': impr_delta,
            'clicks': clicks_delta,
            'conversions': conversions_delta,
            'cpm': cpm_delta,
            'ctr': ctr_delta,
            'conv_rate': conv_rate_delta,
            'cpa': cpa_delta,
            'cpc': cpc_delta
        })

    for i in range(len(current_month['impr'])):
        spend_delta = (current_month['spend'][i] - yoy_month['spend'][i]) / yoy_month['spend'][i]
        spend_delta = round(spend_delta * 10000)
        spend_delta = spend_delta / 100
        impr_delta = (current_month['impr'][i] - yoy_month['impr'][i]) / yoy_month['impr'][i]
        impr_delta = round(impr_delta * 10000)
        impr_delta = impr_delta / 100
        clicks_delta = (current_month['clicks'][i] - yoy_month['clicks'][i]) / yoy_month['clicks'][i]
        clicks_delta = round(clicks_delta * 10000)
        clicks_delta = clicks_delta / 100
        conversions_delta = (current_month['conversions'][i] - yoy_month['conversions'][i]) / yoy_month['conversions'][i]
        conversions_delta = round(conversions_delta * 10000)
        conversions_delta = conversions_delta / 100
        cpm_delta = (current_month['cpm'][i] - yoy_month['cpm'][i]) / yoy_month['cpm'][i]
        cpm_delta = round(cpm_delta * 10000)
        cpm_delta = cpm_delta / 100
        ctr_delta = (current_month['ctr'][i] - yoy_month['ctr'][i]) / yoy_month['ctr'][i]
        ctr_delta = round(ctr_delta * 10000)
        ctr_delta = ctr_delta / 100
        conv_rate_delta = (current_month['conv_rate'][i] - yoy_month['conv_rate'][i]) / yoy_month['conv_rate'][i]
        conv_rate_delta = round(conv_rate_delta * 10000)
        conv_rate_delta = conv_rate_delta / 100
        cpa_delta = (current_month['cpa'][i] - yoy_month['cpa'][i]) / yoy_month['cpa'][i]
        cpa_delta = round(cpa_delta * 10000)
        cpa_delta = cpa_delta / 100
        cpc_delta = (current_month['cpc'][i] - yoy_month['cpc'][i]) / yoy_month['cpc'][i]
        cpc_delta = round(cpc_delta * 10000)
        cpc_delta = cpc_delta / 100
        yoy_month_delta.append({
            'spend': spend_delta,
            'impr': impr_delta,
            'clicks': clicks_delta,
            'conversions': conversions_delta,
            'cpm': cpm_delta,
            'ctr': ctr_delta,
            'conv_rate': conv_rate_delta,
            'cpa': cpa_delta,
            'cpc': cpc_delta
        })

    # qoq_quarter_delta = pd.DataFrame(qoq_quarter_delta)
    # yoy_quarter_delta = pd.DataFrame(yoy_quarter_delta)
    qoq_month_delta = pd.DataFrame(qoq_month_delta)
    yoy_month_delta = pd.DataFrame(yoy_month_delta)

    return {'qoq_quarter_delta': qoq_quarter_delta,
            'yoy_quarter_delta': yoy_quarter_delta,
            'qoq_month_delta': qoq_month_delta,
            'yoy_month_delta': yoy_month_delta}


current_quarter = pd.read_csv('2024-quarterly.csv')
quarter_columns = current_quarter.columns
current_quarter = current_quarter.iloc[0]

current_month = pd.read_csv('2024-monthly.csv')
month_columns = current_month.columns
current_month = current_month.iloc[:3]

yoy_quarter = pd.read_csv('2023-quarterly.csv')
yoy_quarter = yoy_quarter.iloc[0]

yoy_month = pd.read_csv('2023-monthly.csv')
yoy_month = yoy_month.iloc[:3]

qoq_quarter = pd.read_csv('2023-quarterly.csv')
qoq_quarter = qoq_quarter.iloc[0]


qoq_month = pd.read_csv('2023-monthly.csv')
qoq_month = qoq_month.iloc[-3:]
qoq_month.reset_index(inplace=True)



deltas = data_delta(current_quarter, qoq_quarter, yoy_quarter, current_month, qoq_month, yoy_month, quarter_columns)
print(f"{deltas['yoy_month_delta']}")


model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf", device='gpu')
response = model.generate(prompt=f'Please describe this table of deltas: {deltas}')
print(response)