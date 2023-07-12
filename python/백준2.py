# E, S, M = map(int, input().split())
# e, s, m = 1, 1, 1
# year = 1
#
# while True:
#     if e == E and s == S and m == M:
#         print(year)
#         break
#     e += 1
#     s += 1
#     m += 1
#
#     if e == 16:
#         e = 1
#     if s == 29:
#         s = 1
#     if m == 20:
#         m = 1
#     year += 1

Day = 0
arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x,y = map(int,input().split())

for i in range(x-1):
    Day = Day + arrList[i]
Day = (Day + y) % 7

print(weekList[Day])

