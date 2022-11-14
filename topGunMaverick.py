T, N, M = map(int, input().split())
time_N, alt_N = [0] * N, [0] * N
time_M, alt_M = [0] * M, [0] * M
print(time_N)

max_diff = 0

for i in range(N):    
    time_N[i], alt_N[i] = map(int, input().split())
    
for i in range(M):
    time_M[i], alt_M[i] = map(int, input().split())

i, j = 0, 0
timeframe_N, timeframe_M = time_N[i], time_M[j]

while (timeframe_N < T) or (timeframe_M < T):
    
    if (timeframe_M == timeframe_N):
        max_diff = max(max_diff, alt_M[j] - alt_N[i])
        if i < len(time_N) - 1: i += 1; timeframe_N += time_N[i]
        if j < len(time_M) - 1: j += 1; timeframe_M += time_M[j]
    elif (timeframe_M > timeframe_N):
        max_diff = max(max_diff, alt_M[j] - alt_N[i])
        if i < len(time_N) - 1: i += 1; timeframe_N += time_N[i]
    else:
        max_diff = max(max_diff, alt_M[j] - alt_N[i])
        if j < len(time_M) - 1: j += 1; timeframe_M += time_M[j]
    
print(max_diff)