def run():
    nums = {i : i**3 for i in range(1,11)}
    print(nums)


    sqroots ={i : round(i**0.5,4) for i in range(1, 10)}
    print(sqroots)


if __name__ == '__main__':
    run()