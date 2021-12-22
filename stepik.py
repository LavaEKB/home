# put your python code here
k = input()
sh = 'abcdefgh'
j_n = int(sh.find(k[:1]))
i_n = 8 - int(k[1:])
 

r = 8
m = []

for i in range(r):
    m.append([None]*r)

for i in range(r):
    for j in range(r):
        if (i - j_n) ** 2 + (j - i_n) ** 2 == 5:
            m[i][j] = '*'
        elif i_n == i and j_n == j:
            m[i][j] = 'N'
        else:
            m[i][j] = '.'

for i in range(r):
    for j in range(r):
        print(str(m[i][j]), end=' ')
    print() 
# hard
