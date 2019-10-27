import random
import os
import time

with open("countries_and_capitals.txt" , "r") as f:    
    lines_list = f.readlines()

line = random.choice(lines_list)

country_and_capital = line.splitlines()
capital = country_and_capital [1].upper()
country = country_and_capital[0]
start_time = time.time()
lifes = 8
not_in_word = []
counter_of_letters = 0
hangmanpics = ['''
  +---+
      |
      |
      |
      |
      |
========= ''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
hangmanpics.reverse()

hidden_capital = ""
for letter in range(len(capital)):
    hidden_capital = hidden_capital + "_"


while lifes>0 and hidden_capital != capital:
    os.system("clear")
    print('''
    ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ 
   ▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
   ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
   ░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
   ░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
    ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
    ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ 
    ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░ 
    ''')
    print("Answer (only for debugging)", capital) 
    print("What is the capital of" + " " + country + "?")
    print(" ".join(list(hidden_capital)))
    #print(hidden_capital)
    print("lifes:", lifes)
    print("not in word: ", not_in_word)
    
    
    if lifes<8:
      print(hangmanpics[lifes])
    
    guessed_letter_or_word = input("letter: ")
    guessed_letter_or_word = guessed_letter_or_word.upper()

    if len(guessed_letter_or_word) == 1:
        counter_of_letters += 1
    
    if guessed_letter_or_word in capital and len(guessed_letter_or_word)==1:
        for index in range(len(capital)):
            if capital[index] == guessed_letter_or_word:
                hidden_capital_list = list(hidden_capital)
                hidden_capital_list[index] = guessed_letter_or_word
                hidden_capital = "".join(hidden_capital_list)  
    elif guessed_letter_or_word == capital:
        break
    else:
        if len(guessed_letter_or_word) == 1:
          lifes -= 1
        else:
          lifes -= 2  
        not_in_word.append(guessed_letter_or_word)

os.system("clear")
if lifes>0:
   end_time=time.time()
   game_time=int(end_time-start_time)
   print('''
 ▓██   ██▓ ▒█████   █    ██     █     █░ ▒█████   ███▄    █  ▐██▌ 
  ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓█░ █ ░█░▒██▒  ██▒ ██ ▀█   █  ▐██▌ 
   ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒█░ █ ░█ ▒██░  ██▒▓██  ▀█ ██▒ ▐██▌ 
   ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░█░ █ ░█ ▒██   ██░▓██▒  ▐▌██▒ ▓██▒ 
   ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░░██▒██▓ ░ ████▓▒░▒██░   ▓██░ ▒▄▄  
    ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ░▀▀▒ 
  ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░      ▒ ░ ░    ░ ▒ ▒░ ░ ░░   ░ ▒░ ░  ░ 
  ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░   ░  ░ ░ ░ ▒     ░   ░ ░     ░ 
  ░ ░         ░ ░     ░            ░        ░ ░           ░  ░    
  ░ ░
  ''')
   print("Capital of " + country, "is " + capital + "!" + " You guessed the right answer in: " + str(game_time) + "s", "and after " + str(counter_of_letters) + " letters." )
else:
   print('''
  ▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████   ▒█████    ██████ ▓█████  ▐██▌ 
   ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██    ▒ ▓█   ▀  ▐██▌ 
    ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒▒██░  ██▒░ ▓██▄   ▒███    ▐██▌ 
    ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░▒██   ██░  ▒   ██▒▒▓█  ▄  ▓██▒ 
    ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░░ ████▓▒░▒██████▒▒░▒████▒ ▒▄▄  
     ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ░▀▀▒ 
   ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░ ░  ░ 
   ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░  ░  ░     ░       ░ 
   ░ ░         ░ ░     ░            ░  ░    ░ ░      ░ ░        ░     ░  ░ ░    
   ░ ░
   ''')
   print("The right answer is:", capital)
   print(hangmanpics[0]) 

