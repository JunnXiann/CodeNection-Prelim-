num = "100 3 3\n40 75000\n50 35000\n10 45000\n40 76000\n20 30000\n40 40000"

input = input().splitlines()
line1 = input[0].split(" ")
T = int(line1[0])
N = int(line1[1])
M = int(line1[2])

Narray = []
Marray = []
for i in range(1,num.count('\n')+ 1):
    gametime = int(input[i].split(" ")[0])
    gamealtitude = int(input[i].split(" ")[1])
    if i in range(1,num.count('\n')+ 1 - M):
        Narray.append([gametime, gamealtitude])
    elif i in range(num.count('\n')+ 1 - M, num.count('\n')+ 1):
        Marray.append([gametime, gamealtitude])

highest = []
Ntime = 0
Mtime = 0

for n, m in zip(Narray, Marray):
    Ntime += n[0]
    Mtime += m[0]
    if Mtime <= Ntime:
        highest.append(m[1] - n[1])
    elif Mtime > Ntime:
        highest.append(m[1] - Narray[Narray.index(n) + 1][1])

print(max(highest))
        








            




