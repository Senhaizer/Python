def sum(a,b):
    if b==0:
        return a
    return 1+sum(a,b-1)
  
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

print(sum(a,b))
