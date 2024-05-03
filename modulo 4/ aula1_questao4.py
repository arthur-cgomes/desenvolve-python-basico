maior = int(0)
n = int(input("1:"))

if not n > 0:
    print("Maior")

x = int(input("2: "))

while n > 0:

    if x > maior:
        maior = x
        n -= 1

    else:
        n -= 1

    if not n > 0:
        print("Maior")