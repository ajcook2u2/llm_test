from pptx import Presentation
from pptx.util import Inches, Pt
import pprint

prs = Presentation('E:/LibreOffice/test presi.pptx')

slide = prs.slides[0]
slide1 = prs.slides[1]
slide2 = prs.slides[2]

#the asset tree of a slide, from top-down order
for i in slide1.shapes:
    print(i)


#how to access the title of a slide
title = slide1.shapes.title
print('title', title.text)

#How to access and change cells on a table
table = slide1.shapes[1]
print(table.table.cell(0, 0).text)
table.table.cell(0, 0).text = 'SPEND'

#how to access the text box,
text = slide1.shapes[2]
print('text', text.text)

prs.save('pull_test.pptx')