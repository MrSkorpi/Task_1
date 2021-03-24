import math
import sys
def number(n):
    if n < 2:
        print("Число должно быть больше или рано 2")
        quit()
    elif n == 2:
        print(n, "- это простое число")
        quit()
    i = 2
    limit = int(math.sqrt(n))
    while i <= limit:
        if n % i == 0:
            print(n, "- это составное число")
            quit()
        i += 1
    print(n, "- это простое число")
if __name__ == "__main__":
    n = input("Введите число:")
    try:
        if (int(n) != float(n)):
            raise ValueError
        n = int(n)
    except ValueError:
        print("Ошибка ввода")
        sys.exit(1)
    number(n)