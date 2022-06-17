def run():
    # squares = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i)
    # print(squares)

    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    print(squares)
    #Same result with a list comprehension

    #Multiples of 4, 6 and 9 with a maximum of 5 digits

    multiples = [i for i in range(1,100000) if i % 36 == 0]
    print(multiples)


if __name__ == '__main__':
    run()