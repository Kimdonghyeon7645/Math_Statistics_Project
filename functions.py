import os
import xlrd

def scan_xls_files(path: str):
    """ 해당 경로 내의 xls 파일들을 스캔해서 리스트로 반환하는 함수 """
    return [path+i for i in os.listdir(path) if i.split('.')[-1] == 'xls']


def xls_file_to_list(path: str):
    load_wb = xlrd.open_workbook(path)
    load_ws = load_wb.sheet_by_index(0)

    return [load_ws.row_values(i) for i in range(load_ws.nrows)]


def list_data_preprocessing(sheet: list):
    result_list = [['날짜'], ['식단'],
                   ['에너지(kcal)'], ['탄수화물(g)'], ['단백질(g)'], ['지방(g)'], ['비타민A(R.E)'], ['티아민(mg)'],
                   ['리보플라빈(mg)'], ['비타민C(mg)'], ['칼슘(mg)'], ['철분(mg)']]
    sheet_len, i = len(sheet), 0

    while True:
        while sheet[i][0] != '주간\n학교급식 영양량':
            i += 1
            if i >= sheet_len:  return result_list
        result_list[0].extend(sheet[i][4:])
        result_list[1].extend(sheet[i+1][4:])

        while sheet[i][0] != '에너지(kcal)':   i += 1
        for plus in range(10):
            result_list[2+plus].extend(sheet[i+plus][4:])



if __name__ == '__main__':
    # print(scan_xls_files(r"C:\Users\user\Documents\Math_Statistics_Project\학교 급식"))
    li = xls_file_to_list(r"C:\Users\user\Documents\Math_Statistics_Project\학교 급식\12_1월 학교급식 원산지 및 영양표시제.xls")
    # print(*li, sep="\n")
    re_li = list_data_preprocessing(li)
    print(*re_li, sep="\n")
