#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing 2 modules
# Random module is used generate a random 'animal' in the main part of the game
# Time module is used to add delays throughout the game for effect

import random

import time

# The following dictionaries contain the characteristics of 15 different animals
turtle = {'iam': 'slow', 'ilive': 'in the sea', 'ihave': 'a shell', 'ilike': 'to swim', 'ieat': 'seaweed'}

goldfish = {'iam': 'forgetful', 'ilive': 'in ponds', 'ihave': 'fins', 'ilike': 'swimming in circles', 'ieat': 'fish food'}

penguin = {'iam': 'black and white', 'ilive': 'in the south', 'ihave': 'flippers', 'ilike': 'to dive', 'ieat': 'fish'}  

chameleon = {'iam': 'able to change colour', 'ilive': 'in rainforests and deserts', 'ihave': 'a long tongue', 
             'ilike': 'to rest', 'ieat': 'insects'}
             
python = {'iam': 'very long', 'ilive': 'in rainforests', 'ihave': 'beautifully patterned skin', 'ilike': 'to constrict my prey',
          'ieat': 'rodents and small animals most of the time...'}
         
pangolin = {'iam': 'scaly', 'ilive': 'in a variety of habitats fromn tropical forests to deserts', 'ihave': 'a long snout', 
            'ilike': 'to close my nose and ears when I eat', 'ieat': 'ants and termites'}

sloth = {'iam': 'very slow', 'ilive': 'in treetops', 'ihave': 'long arms', 'ilike': 'to sleep', 'ieat': 'leaves'}

platypus = {'iam': 'an egg laying mammal', 'ilive': 'in Australia', 'ihave': 'a bill', 'ilike': 'to hunt at night',
            'ieat': 'insects and crustaceans'}

capybara = {'iam': 'a large rodent', 'ilive': 'in South America', 'ihave': 'continuously growing teeth', 'ilike': 'to swim',
            'ieat': 'grasses and aquatic plants'}

giraffe = {'iam': 'tall', 'ilive': 'in savannas', 'ihave': 'unique spots', 'ilike': 'to use my neck to fight', 
           'ieat': 'acacia leaves'}

duck =  {'iam': 'able to change gender', 'ilive': 'on ponds, streams and rivers', 'ihave': 'feathers', 'ilike': 'to paddle',
         'ieat': 'pondweed, seeds and insects'}

hummingbird = {'iam': 'very fast', 'ilive': 'wherever there is an abundance of flowers', 'ihave': 'the ability to fly backwards',
               'ilike': 'to eat all day', 'ieat': 'nectar and small insects'}

crab = {'iam': 'a crustacean', 'ilive': 'in marine environments', 'ihave': '10 legs', 'ilike': 'to use my pincers', 
        'ieat': 'algae, planktons and fungi'}

koala = {'iam': 'a marsupial', 'ilive': 'in Australia', 'ihave': 'fuzzy ears', 'ilike': 'to swim', 'ieat': 'eucalyptus leaves'}
         
fox = {'iam': 'very agile', 'ilive': 'in forests, mountains, deserts and urban area', 'ihave': 'whiskers on my face and legs',
      'ilike': 'to hunt alone', 'ieat': 'rabbits, rats, birds, berries and fruit'}

# Nesting the dictionaries in a list
# Then converting the 'nested' animals into a list to that the randomly generated animal can be recalled throughout the game
animal = [turtle, goldfish, penguin, chameleon, python, pangolin, sloth, platypus, 
          capybara, giraffe, duck, hummingbird, crab, koala, fox]
animal_selection = ["turtle", "goldfish", "penguin", "chameleon", "python", "pangolin", "sloth", "platypus",
            "capybara", "giraffe", "duck", "hummingbird", "crab", "koala", "fox"]

# Accessing the data in the animal list      
animals = len(animal)

# Generating a random animal for the player to guess 
# Use .randint because each animal within the list is assigned an integer position e.g. turtle - 0, penguin = 2
# The characteristics for the randomly generated chosen_animal are accessed using the trait variable
random_animal = random.randint(0,animals-1)
chosen_animal = animal_selection[random_animal]
trait = animal[random_animal]

# The InGame variable is set to True before and at the start of the maingame() function 
# The Attempt variable is set to 0 so that when the playagain() function is recalled, the random generation of an animal is 'reset'
    # Otherwise, the maingame() function would keep using the same animal on subsequent plays
InGame = True
Attempt = 0

# Game intro
print ("Hello! What is your name?")
Name = input()
time.sleep(1.5)
print()

print ("Okay, " + Name + ", try to guess what animal I am..." )
time.sleep(2)
print()

print ("I will give you five clues. Every time I give you a clue, have a guess!")
time.sleep(3)
print()

# This function is the main part of the game
# The number of guesses the player can make is limited to 5 using guess_limit = 5
    # This corresponds with the number of trait values available for each animal (5)
def maingame(current_attempt,chosen_animal,trait):
    InGame = True
    current_attempt += current_attempt
    guess = ""
    guess_count = 0
    guess_limit = 5

# The while loop states that whilst the player's is not correct, the game will continue providing clues
    while guess != chosen_animal: 
        if guess_count == 0:
            print("Your first clue...I am " + trait['iam'])
            guess = input("Have a guess: ")
            print()
            guess_count += 1
        elif guess_count == 1:
            print("I live " + trait['ilive'])
            guess = input("Have another guess: ")
            print()
            guess_count += 1
        elif guess_count == 2:
            print("I have " + trait['ihave'])
            guess = input("Have another guess: ")
            print()
            guess_count += 1
        elif guess_count == 3:
            print("I like " + trait['ilike'])
            guess = input("Have another guess: ")
            print()
            guess_count += 1
        elif guess_count == 4:
            print("Just one more clue...I eat " + trait['ieat'])
            guess = input("Your last guess: ")
            print()
            guess_count += 1  

# If the player guesses the correct animal at any stage of the game then the player wins
        if guess_count != guess_limit:
            if guess == chosen_animal:            
                print("Well done, you're right! I am a " + chosen_animal + "!")

# If the player does not guess correctly after 5 guesses then they lose
        if guess_count == guess_limit:
            if guess != chosen_animal:                 
                print("Sorry, you're out of guesses! I am a...")
                time.sleep(2) 
                print()
                print(chosen_animal + "!")
                break

# If the player guesses correctly on the 5th guess then they will win 
            else:
                if guess == chosen_animal:
                    print("Well done, you're right! I am a " + chosen_animal + "!")
                    print()

# After the main part of the game is played once, InGame is set to False as to not recall the maingame() function again but rather move onto playagain()                                                       
    InGame = False
    guess = ""
    guess_count = 0
    playagain(current_attempt)

# This function allows the player to play the game again
def playagain(Attempt_2):
    time.sleep(2.5)
    print()
    print()
    play_again = input("Do you want to play again? (type yes or no) ")
    if play_again == "yes":
        print()
        print("Okay, great!")
        time.sleep(2.5)
        print()
        random_animal_2 = random.randint(0,animals-1)
        chosen_animal_2 = animal_selection[random_animal_2]
        traits_2 = animal[random_animal_2]
        maingame(Attempt_2,chosen_animal_2,traits_2)
    else:
        print()
        print("Okay, thanks for playing!")

maingame(Attempt,chosen_animal,trait)

