n=int(input())
arr1 = list(map(int, input().split()))
m=int(input())
arr2 = list(map(int, input().split()))
merged = arr1 + arr2
merged.sort()
print(*merged)
