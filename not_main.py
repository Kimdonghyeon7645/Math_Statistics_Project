import pandas as pd

# xlrd 라이브러리 다운받기!
path = r"C:\Users\user\Documents\Math_Statistics_Project\학교 급식"
data = pd.read_excel(path + r"\12_1월 학교급식 원산지 및 영양표시제.xls", sheet_name=0)
