import pandas as pd
import gpt4all
from dash import *
from analysis_generator import data_delta
import plotly.express as px
import plotly.graph_objects as go


#next steps:
#add comparison metric, to allow for selection of QoQ/YoY
#connect data deltas to llama and pipe in analysis


quarterly_df_2023 = pd.read_csv('2023-quarterly.csv')
quarterly_df_2024 = pd.read_csv('2024-quarterly.csv')
quarterly_df_2025 = pd.read_csv('2025-quarterly.csv')
quarterly_df_2026 = pd.read_csv('2026-quarterly.csv')

quarterly_df_2023['year'] = '2023'
quarterly_df_2024['year'] = '2024'
quarterly_df_2025['year'] = '2025'
quarterly_df_2026['year'] = '2026'

quarterly_df = pd.concat([quarterly_df_2023, quarterly_df_2024])
quarterly_df = pd.concat([quarterly_df, quarterly_df_2025])
quarterly_df = pd.concat([quarterly_df, quarterly_df_2026])

print(quarterly_df.head())

monthly_df_2023 = pd.read_csv('2023-monthly.csv')
monthly_df_2024 = pd.read_csv('2024-monthly.csv')
monthly_df_2025 = pd.read_csv('2025-monthly.csv')
monthly_df_2026 = pd.read_csv('2026-monthly.csv')

monthly_df_2023['year'] = '2023'
monthly_df_2024['year'] = '2024'
monthly_df_2025['year'] = '2025'
monthly_df_2026['year'] = '2026'

months = [
    "January", "February", "March", "April", "May",
    "June", "July", "August", "September", "October",
    "November", "December"
]
monthly_df_2023['month'] = months
monthly_df_2024['month'] = months
monthly_df_2025['month'] = months
monthly_df_2026['month'] = months

quarters = [
    1, 1, 1, 2, 2,
    2, 3, 3, 3, 4,
    4, 4
]
monthly_df_2023['quarter'] = quarters
monthly_df_2024['quarter'] = quarters
monthly_df_2025['quarter'] = quarters
monthly_df_2026['quarter'] = quarters

monthly_df = pd.concat([monthly_df_2023, monthly_df_2024])
monthly_df = pd.concat([monthly_df, monthly_df_2025])
monthly_df = pd.concat([monthly_df, monthly_df_2026])

# print(monthly_df.head())
# print(monthly_df['conv_rate'][monthly_df['year'] == '2023'].unique())
# print(monthly_df_2023['conv_rate'].unique())



app = Dash()

app.layout = [
    html.H1(children='Test Dashboard', style={'textAlign':'center'}),
    dcc.Checklist(options=[{'label': 'Q1', 'value': 1}, {'label': 'Q2', 'value': 2}, {'label': 'Q3', 'value': 3}, {'label': 'Q4', 'value': 4}], value=[1], id='quarter-selection'),
    dcc.Dropdown(['2024', '2025', '2026'], value='2024', id='year-selection'),
    # dcc.Dropdown(['YoY', 'QoQ'], 'YoY', id='comparison-selection'),
    dcc.Graph(id='graph-content'),
    dcc.Textarea(id='textarea', value='Test'),
]

@callback(
    Output('graph-content', 'figure'),
    Input('year-selection', 'value'),
    Input('quarter-selection', 'value'),
    Input('comparison-selection', 'value'),
)
def update_graph(year, quarters, comparison):
    dff = monthly_df[(monthly_df['year'] == year) & (monthly_df['quarter'].isin(quarters))]
    dff1 = monthly_df[(monthly_df['year'] == str(int(year) - 1)) & (monthly_df['quarter'].isin(quarters))]
    fig = px.line(dff, x='month', y='conversions')
    fig.add_trace(go.Scatter(
            x=dff1['month'],
            y=dff1['conversions'],
            mode='lines+markers',
            name='Comparison Metric',
            line=dict(color='red', dash='dash')  # Style the comparison line
        ))
    return fig


if __name__ == '__main__':
    app.run(debug=True)
