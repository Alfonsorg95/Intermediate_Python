def read():
    numbers = []
    with open("./text_documents/numbers.txt", "r",encoding = "utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Alfonso", "Leonardo", "Pedro", "Miguel"]
    # "r" = read
    # "w" = write, overwrites the document
    # "a" = append, writes at the end of the document
    with open("./text_documents/names.txt", "w",encoding = "utf-8") as f:
        for name in names:
            f.write(name + "\n")


def run():
    read()
    write()


if __name__ == '__main__':
    run()