n = int(input())
arr = list(map(int, input().split()))
current_sum = arr[0]
max_sum = arr[0]
for i in range(1, n):
    if arr[i] > arr[i-1]:
        current_sum += arr[i]
    else:
        current_sum = arr[i]
    max_sum = max(max_sum, current_sum)
print(max_sum)
