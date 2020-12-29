# from openpyxl import load_workbook    (load_workbook 으로 xlsx 불러오기)
import xlrd

load_wb = xlrd.open_workbook("학교 급식/12_1월 학교급식 원산지 및 영양표시제.xls")
load_ws = load_wb.sheet_by_index(0)

for i in range(load_ws.nrows):
    print(load_ws.row_values(i))
