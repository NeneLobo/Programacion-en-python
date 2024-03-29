# Import modules to use
from words import palabras,hangpics
import string
import random

# 1. Welcome
print("Welcome to the game hangman in Python")

# 2. Function to get word
def get_valid_word(palabras):
  word = random.choice(palabras)

  # Choose a good word
  while '-' in word or ' ' in word: # While - or ' '
    word = random.choice(palabras)

  return word.upper()


# Main function, init game
def hangman():

  word = get_valid_word(palabras) # SOL
  word_letters = set(word) # S, O , L
  alphabet = set(string.ascii_uppercase) # A, B, C, D, E,...
  used_letters = set()
  lives = 6



  print("La palabra es: ",word)

  while len(word_letters) > 0 and lives > 0:
    print(f"You have {lives} lives left and you have used these letters: ",' '.join(used_letters))

    # what letter you guess, example WORD (- - R D)
    word_list = [letter if letter in used_letters else '-' for letter in word]

    print("Current word: ", ' '.join(word_list),"\n")

    user_letter = input('Guess a letter:').upper() # S

    if user_letter in alphabet - used_letters: # si "S" esta en "A,B,C,D" - ""
      used_letters.add(user_letter) # S
      # print(used_letters,'\n',word_letters)

      if user_letter in word_letters: # S es parte de tu palabra
        word_letters.remove(user_letter) # S, O , L le quito la S = O, L
      else:
        lives = lives - 6
        print('Letter is not in word')
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')

    elif user_letter in used_letters:
      print("You have already used that character. Please try again")
      
      elif  lives = lives - 5
      print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')

  print("You have already used that character. Please try again.")
      elif  lives = lives - 4
      print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')

print("You have already used that character. Please try again.")
      elif  lives = lives - 3
      print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')

print("You have already used that character. Please try again.")
      elif  lives = lives - 2
      print( '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')

print("You have already used that character. Please try again.")
      elif  lives = lives - 1
      print( '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    else:
      print("Invalid character. Please try again.")

  if lives == 0:
    print("You died, The word was: ", word)
    print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
  else:
    print("You guessed the word: ", word,"!!! =)")


hangman()


