import json
import xlsxwriter
import requests

response = requests.get(url, params)
d = json.loads(response.text)

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for key in d.keys():
    row += 1
    worksheet.write(row, col, json.dumps(key))
    for item in d[key]:
        worksheet.write(row, col + 1, json.dumps(item))
        row += 1

workbook.close()
