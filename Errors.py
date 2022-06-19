def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    try:
        num = int(input('Ingresa un número: '))
        if num <= 0:
            raise ValueError
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingesar un numero entero positivo")


if __name__ == '__main__':
    run()