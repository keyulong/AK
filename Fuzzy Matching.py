# -*- coding: utf-8 -*-
__version__ = '0.16.0'
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
import os
import xlrd
import xlwt

# 从Excel 读数据
WorkBook = xlrd.open_workbook(r'D:\Test.xlsx')
WorkSheet = WorkBook.sheet_by_index(0)
File = xlwt.Workbook()
Table = File.add_sheet("Result", cell_overwrite_ok=True)
Str1 = WorkSheet.col_values(1)
Str2 = WorkSheet.col_values(2)

Group = list()
for i in range(len(Str1)):
    Group.append("Null")
for Index1 in range(len(Str1)):
    Num = 0
    for Index2 in range(len(Str2)):
        if Group[Index2] == "Null":
            # Similarity = fuzz.ratio(Str1[Index1], Str2[Index2])
            Similarity = fuzz.partial_ratio(Str1[Index1], Str2[Index2])
            if Similarity >= 60:
                Group[Index2] = Index1 + 1
                Num = Num + 1
    if Group[Index1] == "Null" and Num == 0:
        Group[Index1] = Index1 + 1

    print(Index1)
df = pd.read_excel(r'D:\Test.xlsx', header=None)
df[3] = pd.Series(Group)
df.to_excel(r'D:\Test.xlsx', sheet_name='Result', index=False, index_label=False, header=None)
