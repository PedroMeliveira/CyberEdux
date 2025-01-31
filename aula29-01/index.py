from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Planilha Exemplo"
ws.append(['Nome', 'Idade', 'Cidade'])
ws.append(['João', 30, 'São Paulo'])
ws.append(['Maria', 25, 'Rio de Janeiro'])
wb.save('exemplo.xlsx')