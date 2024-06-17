from pptx import Presentation
from pptx.util import Inches, Pt
import pprint
import pandas as pd
from analysis_generator import data_delta

prs = Presentation('E:/LibreOffice/test presi.pptx')

slide = prs.slides[0]
slide1 = prs.slides[1]
slide2 = prs.slides[2]


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
qoq_quarter = qoq_quarter.iloc[3]


qoq_month = pd.read_csv('2023-monthly.csv')
qoq_month = qoq_month.iloc[-3:]
qoq_month.reset_index(inplace=True)

deltas = data_delta(current_quarter, qoq_quarter, yoy_quarter, current_month, qoq_month, yoy_month, quarter_columns)

#the asset tree of a slide, from top-down order
for i in slide1.shapes:
    print(i)


#how to access the title of a slide
title = slide1.shapes.title
print('title', title.text)

#How to access and change cells on a table
table = slide1.shapes[1]
print(table.table.cell(0, 0).text)
table.table.cell(0, 0).text = 'Year'
table.table.cell(1, 0).text = '2024'
table.table.cell(2, 0).text = '2023'
table.table.cell(3, 0).text = 'YoY'

table.table.cell(0, 1).text = 'Spend'
table.table.cell(1, 1).text = str(current_quarter['spend'])
table.table.cell(2, 1).text = str(yoy_quarter['spend'])

table.table.cell(0, 1).text = 'Impressions'
table.table.cell(1, 1).text = str(current_quarter['impr'])
table.table.cell(2, 1).text = str(yoy_quarter['impr'])

table.table.cell(0, 2).text = 'Clicks'
table.table.cell(1, 2).text = str(current_quarter['clicks'])
table.table.cell(2, 2).text = str(yoy_quarter['clicks'])

table.table.cell(0, 3).text = 'CTR'
table.table.cell(1, 3).text = str(current_quarter['ctr'])
table.table.cell(2, 3).text = str(yoy_quarter['ctr'])

table.table.cell(0, 4).text = 'CPC'
table.table.cell(1, 4).text = str(current_quarter['cpc'])
table.table.cell(2, 4).text = str(yoy_quarter['cpc'])

table.table.cell(0, 5).text = 'Conversions'
table.table.cell(1, 5).text = str(current_quarter['conversions'])
table.table.cell(2, 5).text = str(yoy_quarter['conversions'])

table.table.cell(0, 6).text = 'Conv. Rate'
table.table.cell(1, 6).text = str(current_quarter['conv rate'])
table.table.cell(2, 6).text = str(yoy_quarter['conv rate'])



#how to access the text box,
text = slide1.shapes[2]
print('text', text.text)

prs.save('pull_test.pptx')