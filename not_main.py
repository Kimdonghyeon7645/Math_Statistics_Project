from functions import *

content_li = []
for path in scan_xls_files("학교 급식/"):
    xls_file_path_li = xls_file_to_list(path)
    content_li.append(get_list_average(list_data_preprocessing(xls_file_path_li)))
print_average(content_li)
