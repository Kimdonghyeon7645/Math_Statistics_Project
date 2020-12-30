import os
import xlrd


def scan_xls_files(path: str) -> list:
    """
    해당 경로(:param path:) 안의
    xls 파일들 경로를 리스트로 반환(:return:)하는 함수
    """
    path += '' if path[-1] == '/' else '/'
    return [path+i for i in os.listdir(path) if i.split('.')[-1] == 'xls']


def xls_file_to_list(path: str):
    """
    xls 파일의 경로(:param path:)를 받아
    2차원 리스트로 변환해서 반환(:return:)하는 함수
    """
    load_wb = xlrd.open_workbook(path)
    load_ws = load_wb.sheet_by_index(0)

    return [load_ws.row_values(i) for i in range(load_ws.nrows)]


def list_data_preprocessing(sheet: list, add_row_header: bool = False):
    """
    2차원 리스트(:param sheet:)를 받아
    날짜별 식단과 그의 영양소만 추출해 반환(:return:)하는 함수
    (:param add_row_header:가 참일시, 각 행을 식별하는 이름이 붙음)
    """
    result_list = [[] for i in range(12)]
    sheet_len, i = len(sheet), 0

    if add_row_header:
        headers = ['날짜', '식단', '에너지(kcal)', '탄수화물(g)', '단백질(g)', '지방(g)', '비타민A(R.E)', '티아민(mg)',
         '리보플라빈(mg)', '비타민C(mg)', '칼슘(mg)', '철분(mg)']
        for j in range(len(headers)):   # DANGER! : 변수를 같은이름인 i로 쓰면, 지역변수 i값이 변동되어 유지!!
            result_list[j].append(headers[j])

    while True:
        while sheet[i][0] != '주간\n학교급식 영양량':
            i += 1
            if i >= sheet_len:  return result_list
        result_list[0].extend(sheet[i][4:])
        result_list[1].extend(sheet[i+1][4:])

        while sheet[i][0] != '에너지(kcal)':   i += 1
        for plus in range(10):
            result_list[2+plus].extend(sheet[i+plus][4:])


def get_list_average(content_li: list):
    """
    영양소 값 배열(:param content_li:)을 받아
    영양소의 평균을 반환(:return:)하는 함수
    """
    result_li = []

    if type(content_li[2][0]) == type("문자열"):
        for row in content_li:
            row.pop(0)

    for i in range(2, len(content_li)):
        result_li.append(get_average(content_li[i]))
    return result_li


def get_average(target_li: list):
    """
    원하는 리스트(:param target_li:)를 전달받아
    숫자만 추려 평균을 소수점 둘째자리로 반올림한 값을 반환(:return:)하는 함수
    """
    nums = [i for i in target_li if i]
    return round(sum(nums) / len(nums), 2)


def print_average(li_li: list):
    """
    평균을 계산할 리스트(:param li_li:)를 전달받아
    내용과 수치의 평균을 출력한 값을 반환(:return:)하는 함수
    """
    header = ['에너지(kcal)', '탄수화물(g)', '단백질(g)', '지방(g)', '비타민A(R.E)', '티아민(mg)', '리보플라빈(mg)', '비타민C(mg)',
              '칼슘(mg)', '철분(mg)']
    for i, content in enumerate(li_li):
        print(f"{header[i]} 평균 : {get_average(content)}")


if __name__ == '__main__':
    # print(scan_xls_files(r"C:\Users\user\Documents\Math_Statistics_Project\학교 급식"))
    # li = xls_file_to_list(r"C:\Users\user\Documents\Math_Statistics_Project\학교 급식\12_1월 학교급식 원산지 및 영양표시제.xls")
    li = xls_file_to_list(r"C:\Users\user\Documents\Math_Statistics_Project\학교 급식\10월 학교급식 식재료 원산지 및 영양표시제.xls")
    # print(*li, sep="\n")
    re_li = list_data_preprocessing(li)
    # print(*re_li, sep="\n")
