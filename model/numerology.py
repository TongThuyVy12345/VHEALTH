import pandas as pd
from datetime import datetime


def numerology(date):
    df = pd.read_csv("C:\\Users\ADMIN\PycharmProjects\ModelQA_NCKH\VHealth\data\CSV\ThanSoHoc.csv")

    # Lấy ngày hiện tại
    # date_str = date.strftime("%d-%m-%Y")  # Chuyển đổi sang chuỗi theo định dạng dd/mm/yyyy
    date_list = list(date.replace("-", ""))
    date_array = []
    # Tính tổng của mảng
    for char in date_list:
        date_array.append(char)

    while len(date_array) > 1:
        total = sum([int(i) for i in date_array])
        date_array = list(str(total))
    # print("Số thần số học:", date_array[0])
    numberology = date_array[0]
    numberology = int(numberology) - 2
    # print(numberology)
    return (df.loc[numberology]["General meaning"])
