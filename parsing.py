# n = '5 2 3 7 5 9 7 4 8 2 6 4 1 5 8 7 3 9 11 22 33 44 55 66 77 88 99'
# arEnd = []
# arStart = []
# count = 0
# n = [int(x) for x in n.split()]
# print(len(n))
# for i in range(len(n)//9):
#     if len(arEnd)!=0:
#         i+=8*count
#     while len(arStart)<9:                             СТРОКУ В ДВУМЕРНЫЙ МАССИВ
#         arStart.append(n[i])
#         i+=1
#     arEnd.append(arStart)
#     arStart = []
#     count+=1
# print(arEnd)

# ar = [[1,2,3],[4,5,6]]
# s = ''
# for i in range(len(ar)):                              ДВУМЕРНЫЙ МАССИВ В СТРОКУ
#     for j in ar[i]:
#         s+=str(j)+' '
# print(s)