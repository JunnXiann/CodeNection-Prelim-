def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x: return "Yes"
        elif arr[mid] > x: return binary_search(arr, low, mid - 1, x)
        else: return binary_search(arr, mid + 1, high, x)
    else:
        return "No"
    
N, Q = map(int, input().split())

ids = input().split()
idd = []
for id in ids:
    idd.append(int(id))
idd.sort()
for i in range(Q):
    print(binary_search(idd, 0, len(idd)-1, int(input())))