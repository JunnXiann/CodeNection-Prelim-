_ = input()
s = input()
a = input()

s_freq = {}
a_freq = {}
result = ""

for i in s:
    if i in s_freq:
        s_freq[i] += 1
    else:
        s_freq[i] = 1
        
for i in a:
    if i in a_freq:
        a_freq[i] += 1
    else:
        a_freq[i] = 1
    
for i in a:
    if i in s:
        if a_freq[i] <= s_freq[i]:
            result = "YES"
        else:
            result = "NO"
    else:
        result = "NO"
        break
        
print(result)