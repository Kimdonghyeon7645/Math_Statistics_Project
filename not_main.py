from functions import *

sum_li = []
time_slice_li = [[[] for _ in range(10)] for _ in range(3)]
for path in scan_xls_files("학교 급식/"):
    xls_file_path_li = xls_file_to_list(path)
    sheet_li = list_data_preprocessing(xls_file_path_li)
    sum_li.append(get_list_average(sheet_li))

    week_len = len(sheet_li[0]) // 3
    for i in range(3):
        for j, li in enumerate(sheet_li[2:]):
            time_slice_li[i][j].extend(li[i * week_len : (i+1) * week_len+1])

print("- 전체 평균 -")
print_average(list(zip(*sum_li)))

print("\n- 시간대별 평균 -")
for index, time in enumerate(['아침', '점심', '저녁']):
    print(f"\n* {time}")
    print_average(time_slice_li[index])
