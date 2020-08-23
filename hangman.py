import random

print("H A N G M A N")

word_list = ['python', 'java', 'kotlin', 'javascript']
random.seed()
guess_word = random.choice(word_list)
solved_word = "-" * len(guess_word)
letters = set()
count = 8
string = ""
while string != "exit":
    string = input('Type "play" to play the game, "exit" to quit: ')
    if string == "play":
        while count > 0:
            print()
            print(solved_word)
        #    print()
            letter = input("Input a letter: ")
            if letter in letters:
                print("You already typed this letter")
            elif len(letter) != 1:
                print("You should input a single letter")
            elif letter not in "abcdefghijklmnopqrstuvwxyz":
                print("It is not an ASCII lowercase letter")
            elif letter in guess_word:
                letters.add(letter)
                temp_word = guess_word
                for _ in range(guess_word.count(letter)):
                    solved_word = solved_word[:temp_word.find(letter)] + letter + solved_word[temp_word.find(letter)+1:]
                    temp_word = temp_word.replace(letter, "-", 1)
                if guess_word == solved_word:
                    print("You guessed the word " + solved_word + "!")
                    print("You survived!")
                    break
            else:
                letters.add(letter)
                print("No such letter in the word")
                count -= 1
        else:
            print("You are hanged!")
