numOfStars, numOfNominate = map(int, input().split())
vis = input().split()
Visibility = [0] * numOfStars
map = {}
day = 0
for i in range(numOfStars):
    Visibility[i] = int(vis[i])
    map[Visibility[i]] = [Visibility[i], numOfNominate, True]

num = numOfStars * numOfNominate

while num != 0:
    day += 1
    tempvis = []
    for i in map:
        if map[i][2] == False:
            if map[i][0] == 0:
                map[i][0] = i
                map[i][2] = True
            elif map[i][0] > 0:
                map[i][0] -= 1
            
        elif map[i][2] == True:
            if map[i][0] == 0:
                map[i][0] = i
            elif map[i][0] > 0:
                map[i][0] -= 1
        if map[i][2] != False and map[i][1] != 0:
            tempvis.append(i)
    if len(tempvis) != 0:
        print(min(tempvis))
        map[min(tempvis)][0] -= 1
        map[min(tempvis)][1] -= 1
        map[min(tempvis)][2] == False
        num =- 1

print(day)