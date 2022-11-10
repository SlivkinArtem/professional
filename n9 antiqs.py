n = int(input())
arr = []
for i in range(n):
    arr.append(i+1)
for i in range(2, n):
    arr[i], arr[i//2] = arr[i//2], arr[i]
print(*arr)