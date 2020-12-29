from functions import *

content_li = []
header = ['에너지(kcal)', '탄수화물(g)', '단백질(g)', '지방(g)', '비타민A(R.E)', '티아민(mg)', '리보플라빈(mg)', '비타민C(mg)',
          '칼슘(mg)', '철분(mg)']
for path in scan_xls_files("학교 급식/"):
    content_li.append(get_average(list_data_preprocessing(xls_file_to_list(path))))
for i, content in enumerate(list(zip(*content_li))):
    print(f"{header[i]} 평균 : {round(sum(content) / len(content), 3)}")
