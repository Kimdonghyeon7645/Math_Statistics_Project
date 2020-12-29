from functions import *

for path in scan_xls_files("학교 급식/"):
    get_average(list_data_preprocessing(xls_file_to_list(path)))

