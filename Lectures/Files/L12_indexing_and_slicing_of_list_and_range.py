l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
l = list( range(16) )

print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(l[4:15:2])
# [4, 6, 8, 10, 12, 14]
print(l[4:15:-2])
# []
print(l[4:15:-1])
# []
print(l[4:15:-3])
# []

print('----------------------')

word = "TEST"
print(word[::-1])
# TSET
print(word[::-2])
# TE
word = ['T','E','S','T']
print(word[::-1])
# ['T', 'S', 'E', 'T']
print(word[::-2])
# ['T', 'E']

print('----------------------')

for number in range(4, 15, 2):
    print(number, end=' ')
# 4 6 8 10 12 14

for number in range(4, 15, -2):
    print(number, end=' ')
# (no output)
