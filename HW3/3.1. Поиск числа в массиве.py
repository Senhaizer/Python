n = int(input())
a = map(int, input().split())
x = int(input())
print(sum(map(lambda z: int(z == x), a)))
