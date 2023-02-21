n = int(input("Введите число монеток: "))
k = 0 
for i in range(n):
    v = int(input("Жми 1, если орел, и жми 0, если решка - "))
    if v == 1:
        k += 1
print(k if k<n/2 else n - k)
