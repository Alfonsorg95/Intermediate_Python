from itertools import count
import random
import unidecode
import os

def random_word():
    with open("./text_documents/data.txt","r", encoding = "utf-8") as list:
        word_list = [word.replace("\n","") for word in list]
    return normalize(random.choice(word_list))


def normalize(word):
    return unidecode.unidecode(word)


def welcome():
    os.system("clear")
    print("""    Bienvenido al juego del ahorcado 
    Presiona \"enter\" para continuar""")
    input()


def print_state(dict, failures):
    os.system("clear")
    hidden = " "
    for i in range(1, len(dict)+1):
        hidden = hidden + str(dict[i] + " ")
    print(hidden)
    print("Intentos fallidos: " + str(failures))
    


def game(word):
    word_dict = {key: char for key, char in enumerate(word, 1)}
    guess_dict = {key : "_" for key in range(1, len(word_dict) + 1)}
    game_over = False
    win = False
    failures = 0
    count = 0
    while game_over == False:
        print_state(guess_dict, failures)
        try:
            guess = input("Ingresa una letra y presiona enter \n")

            if len(guess) != 1 or guess.isnumeric():
                raise TypeError
            guess = normalize(guess)

            for i in range(1, len(word_dict) + 1):
                if guess == word_dict[i] and guess != guess_dict[i]:
                    guess_dict[i] = guess
                else:
                    count += 1

            if count == len(guess_dict):
                failures += 1
            count = 0

            if failures == 15:
                game_over = True
            
            if word_dict == guess_dict:
                game_over = True
                win = True

        except TypeError:
            print(" Debes ingresar solo un caracter no numerico \n Enter para continuar")
            input()
    os.system("clear")
    if win == False:
        print("Superaste el maximo de fallas permitidas \n Game Over")
    else:
        print("Descubriste la palabra \n Felicidades ganaste el juego")




def run():
    word = random_word()
    welcome()
    game(word)


if __name__ == '__main__':
    run()