# s = 'Reverse this strings'
#
# for i in range(len(s)-1, -1, -1):
#     print(s[i], end='')

#####################################
# s = '123'
#
# def atoi(s):
#     i = 0
#     for x in s:
#         i = i*10 + ord(x)-ord('0')
#     return i

# print(atoi('123'))

# def itoa(i):
#
#     if i >= 0:
#         str = ''
#         while i > 0:
#             remain = i % 10
#             i = i // 10
#             str += chr(remain+48)
#         ans = str[::-1]
#         return ans
#
#     if i < 0:
#         str = ''
#         i = i * (-1)
#         while i > 0:
#             remain = i % 10
#             i = i // 10
#             str += chr(remain + 48)
#         str += chr(45)
#         ans = str[::-1]
#         return ans
#
# print(itoa(123))
# print(itoa(-123))

#############################################

p = "water" # 찾을 패턴
t = "waterbwaterbwater" # 전체 텍스트
M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

def BruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i == i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M: return i - M  #검색 성공
    else: return -1         #검색 실패

print(BruteForce(p, t))