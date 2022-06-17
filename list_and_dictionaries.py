def run():
    my_list = [1, "hello", True, 4.5]
    my_dictionary = {"firstname":"Alfonso", "lastname":"Rodriguez"}

    super_list = [
        {"firstname":"Alfonso", "lastname":"Rodriguez"},
        {"firstname":"Leonardo", "lastname":"Solorzano"},
        {"firstname":"Jose", "lastname":"Ruiz"},
        {"firstname":"Pedro", "lastname":"Sanchez"}
    ]

    super_dictionary = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-2,-1,0,1,2],
        "floating_nums":[1.1,1.2,1.3,1.4,1.5]
    }

    for key,value in super_dictionary.items():
        print(key, " ", value)

    for item in super_list:
        print(item)


if __name__ == '__main__':
    run()