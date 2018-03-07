# -*- coding: utf-8 -*-
__version__ = '0.16.0'
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

Str1 = ["マークス", "デカルシファイヤー（1L）", "デカルシファイヤー（1L）", "デカルシファイヤー（１Ｌ）", "マークス胴張紙", "HH"]
Str2 = ["マークス", "デカルシファイヤー（1L）", "デカルシファイヤー（1L）", "デカルシファイヤー（１Ｌ）", "マークス胴張紙", "HH"]
Group = list()
for i in range(len(Str1)):
    Group.append("Null")
# print(Group)
for Index1 in range(len(Str1)):
    MaxSimilarity = 0
    MaxIndex = 0
    for Index2 in range(len(Str2)):
        if Index1 == Index2:
            continue
        else:
            # Similarity = fuzz.partial_ratio(Str1[Index1], Str2[Index2])
            Similarity = fuzz.ratio(Str1[Index1], Str2[Index2])
            if Similarity == 100:
                MaxSimilarity = Similarity
                MaxIndex = Index2
                Group[Index1] = MaxIndex
                break

            if (Similarity >= 60 and Similarity > MaxSimilarity):
                MaxSimilarity = Similarity
                MaxIndex = Index2
                Group[Index1] = MaxIndex

    if MaxSimilarity < 60:
        MaxSimilarity = 0
        MaxIndex = Index1
        Group[Index1] = MaxIndex

    for i in range(len(Group)):
        if Index1 == Group[i]:
            Group[i] = Group[MaxIndex]

    print(Index1, Str1[Index1], Str2[MaxIndex], MaxIndex, MaxSimilarity, Group[Index1])
