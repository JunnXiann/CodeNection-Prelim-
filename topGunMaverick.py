T,N,M = map(int, input().split())
Ntime, Nalt = [0] * N, [0] * N
Mtime, Malt = [0] * M, [0] * M

for i in range(N):
    Ntime[i], Nalt[i] = map(int, input().split())
    
for i in range(M):
    Mtime[i], Malt[i] = map(int, input().split())
    
maxdiff = 0
i, j = 0, 0
Ntimeframe, Mtimeframe = Ntime[i], Mtime[j]

while Ntimeframe < T or Mtimeframe < T:
    maxdiff = max(maxdiff, Malt[j] - Nalt[i])
    if Ntimeframe == Mtimeframe:
        if i < len(Ntime) - 1: i += 1; Ntimeframe += Ntime[i];
        if j < len(Mtime) - 1: j += 1; Mtimeframe += Mtime[j];
    elif Ntimeframe > Mtimeframe:
        if j < len(Mtime) - 1: j += 1; Mtimeframe += Mtime[j];
    else:
        if i < len(Ntime) - 1: i += 1; Ntimeframe += Ntime[i];
            
print(maxdiff)