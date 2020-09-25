# 삽입정렬

n = int(input())

list = []

for _ in range(1, n+1):
	list.append(int(input()))

for i in range(1, n):
    for j in range(i, 0, -1):
        if (list[j] < list[j-1]):
            tmp = list[j-1]
            list[j-1] = list[j]
            list[j] = tmp

        else:
            break

print(list)
