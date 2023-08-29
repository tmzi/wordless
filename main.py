import random
import json
from tkinter import WORD

class Words:
    def __init__(self, length):
        with open('words.json', 'r', encoding='utf-8') as f:
            word_list = json.load(f)
        wordle_list = []
        for word in range(len(word_list)):
            if len(word_list[word])==5:
                wordle_list.append(word_list[word])
        self.words = wordle_list

game = Words(5)

def eliminator(guess):
    letter_1 = guess[0].lower()
    letter_2 = guess[1].lower()
    letter_3 = guess[2].lower()
    letter_4 = guess[3].lower()
    letter_5 = guess[4].lower()
    #LETTER ONE
    answer_1 = input("Letter one: [{}] - is this Black (B), Yellow (Y), or Green (G), or Not in Word List (N)?".format(guess[0].lower()))
    if answer_1.lower()=="n":
        pass
    elif answer_1.lower() == "b":
        try:
            remove1 = []
            for word in range(len(game.words)):
                if game.words[word].lower().find(letter_1)!=-1:
                    remove1.append(game.words[word])
            x_for_x = [x for x in game.words if x not in remove1]
            game.words = x_for_x
        except:
            print('nah wtf')
    elif answer_1.lower() =="y":
        try:
            remove1 = []
            for word in range(len(game.words)):
                if (game.words[word].lower())[0]==letter_1.lower():
                    remove1.append(game.words[word])
                if (game.words[word].lower()).find(letter_1)==-1:
                    remove1.append(game.words[word])
            x_for_x = [x for x in game.words if x not in remove1]
            game.words = x_for_x
        except:
            pass
    elif answer_1.lower()=="g":
        try:
            remove1 = []
            for word in range(len(game.words)):
                if (game.words[word].lower())[0]!=letter_1.lower():
                    remove1.append(game.words[word])
            x_for_x = [x for x in game.words if x not in remove1]
            game.words = x_for_x
        except:
            pass
    #LETTER TWO
    if answer_1.lower() !="n":
        answer_2 = input("Letter two: [{}] - is this Black (B), Yellow (Y), or Green (G)?".format(guess[1].lower()))
        if answer_2.lower() == "b":
            try:
                remove2 = []
                for word in range(len(game.words)):
                    if game.words[word].lower().find(letter_2) != -1:
                        remove2.append(game.words[word])
                x_for_x = [x for x in game.words if x not in remove2]
                game.words = x_for_x
            except:
                print('nah wtf')
        elif answer_2.lower() == "y":
            try:
                remove1 = []
                for word in range(len(game.words)):
                    if (game.words[word].lower())[1] == letter_2.lower():
                        remove1.append(game.words[word])
                    if (game.words[word].lower()).find(letter_2)==-1:
                        remove1.append(game.words[word])
                x_for_x = [x for x in game.words if x not in remove1]
                game.words = x_for_x
            except:
                pass
        elif answer_2.lower() == "g":
            try:
                remove1 = []
                for word in range(len(game.words)):
                    if (game.words[word].lower())[1] != letter_2.lower():
                        remove1.append(game.words[word])
                x_for_x = [x for x in game.words if x not in remove1]
                game.words = x_for_x
            except:
                pass
    #LETTER THREE
    if answer_1.lower() != "n":
        answer_3 = input("Letter three: [{}] - is this Black (B), Yellow (Y), or Green (G)?".format(guess[2].lower()))
        if answer_3.lower() == "b":
            try:
                remove3 = []
                for word in range(len(game.words)):
                    if game.words[word].lower().find(letter_3) != -1:
                        remove3.append(game.words[word])
                x_for_x = [x for x in game.words if x not in remove3]
                game.words = x_for_x
            except:
                print('nah wtf')
        elif answer_3.lower() == "y":
            try:
                remove1 = []
                for word in range(len(game.words)):
                    if (game.words[word].lower())[2] == letter_3.lower():
                        remove1.append(game.words[word])
                    if (game.words[word].lower()).find(letter_3)==-1:
                        remove1.append(game.words[word])
                x_for_x = [x for x in game.words if x not in remove1]
                game.words = x_for_x
            except:
                pass
        elif answer_3.lower() == "g":
            try:
                remove1 = []
                for word in range(len(game.words)):
                    if (game.words[word].lower())[2] != letter_3.lower():
                        remove1.append(game.words[word])
                x_for_x = [x for x in game.words if x not in remove1]
                game.words = x_for_x
            except:
                pass
    #LETTER FOUR
    if answer_1.lower() !="n":
        answer_4 = input("Letter four: [{}] - is this Black (B), Yellow (Y), or Green (G)?".format(guess[3].lower()))
        if answer_4.lower() == "b":
            try:
                remove4 = []
                for word in range(len(game.words)):
                    if game.words[word].lower().find(letter_4) != -1:
                        remove4.append(game.words[word])
                x_for_x = [x for x in game.words if x not in remove4]
                game.words = x_for_x
            except:
                print('nah wtf')
        elif answer_4.lower() == "y":
            try:
                remove1 = []
                for word in range(len(game.words)):
                    if (game.words[word].lower())[3] == letter_4.lower():
                        remove1.append(game.words[word])
                    if (game.words[word].lower()).find(letter_4)==-1:
                        remove1.append(game.words[word])
                x_for_x = [x for x in game.words if x not in remove1]
                game.words = x_for_x
            except:
                pass
        elif answer_4.lower() == "g":
            try:
                remove1 = []
                for word in range(len(game.words)):
                    if (game.words[word].lower())[3] != letter_4.lower():
                        remove1.append(game.words[word])
                x_for_x = [x for x in game.words if x not in remove1]
                game.words = x_for_x
            except:
                pass
    # LETTER FIVE
    if answer_1.lower() != "n":
        answer_5 = input("Letter four: [{}] - is this Black (B), Yellow (Y), or Green (G)?".format(guess[4].lower()))
        if answer_5.lower() == "b":
            try:
                remove5 = []
                for word in range(len(game.words)):
                    if game.words[word].lower().find(letter_5) != -1:
                        remove5.append(game.words[word])
                x_for_x = [x for x in game.words if x not in remove5]
                game.words = x_for_x
            except:
                print('nah wtf')
        elif answer_5.lower() == "y":
            try:
                remove1 = []
                for word in range(len(game.words)):
                    if (game.words[word].lower())[4] == letter_5.lower():
                        remove1.append(game.words[word])
                    if (game.words[word].lower()).find(letter_5)==-1:
                        remove1.append(game.words[word])
                x_for_x = [x for x in game.words if x not in remove1]
                game.words = x_for_x
            except:
                pass
        elif answer_5.lower() == "g":
            try:
                remove1 = []
                for word in range(len(game.words)):
                    if (game.words[word].lower())[4] != letter_5.lower():
                        remove1.append(game.words[word])
                x_for_x = [x for x in game.words if x not in remove1]
                game.words = x_for_x
            except:
                pass
    print('The list of remaining words has been updated. {} possibilities left.'.format(len(game.words)))


def start():
    guess_1 = (random.choice(game.words))
    print("Please try the word '{}'.".format(guess_1))
    eliminator(guess_1)
    while len(game.words)!=1:
        another_guess = (random.choice(game.words))
        print("Please try the word '{}'.".format(another_guess))
        eliminator(another_guess)
    print("Finished. Can you try '{}'?".format(game.words))
    input("Enter ANYTHING to terminate application:")
    #Now, call possible words at any time using game.words

start()
