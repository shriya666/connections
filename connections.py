import random 
import os
def gencat(category_file):
    f=open("wordbanks/" + category_file)
    thefile=f.read()
    this_list=thefile.split("\n")
    category_yellow=[]
    for i in range(0, 4):
        the_word=random.randint(0, len(this_list) - 1)
        this_actual_thing=(this_list[the_word])
        this_list.remove(this_actual_thing)
        category_yellow.append(this_actual_thing)
    return category_yellow
yellow_random=random.choice(os.listdir("wordbanks/yellow"))
green_random=random.choice(os.listdir("wordbanks/green"))
blue_random=random.choice(os.listdir("wordbanks/blue"))
purple_random=random.choice(os.listdir("wordbanks/purple"))


def actual_game():
    print("Welcomne to today's connections!!!!!!! ")
    categories={
        "yellow": gencat("yellow/"+yellow_random),
        "green": gencat("green/"+green_random),
        "blue": gencat("blue/"+blue_random), 
        "purple":gencat("purple/"+purple_random)
        }
    correct_guesses={
        "yellow": [],
        "green" : [],
        "blue": [],
        "purple": []
    }
    s=[
    *categories["yellow"],
    *categories["green"],
    *categories["blue"],
    *categories["purple"],
    ]
    random.shuffle(s)
    print(s)
    lives=4
    previousCount = 0
    
    while lives>0:
        for i  in range(0, 4):
            your_guess_word= input().lower()
            for color in categories:
                if your_guess_word in categories[color]:
                    correct_guesses[color].append(your_guess_word)
        counter=0
        for color in correct_guesses:
            if len(set(correct_guesses[color]))==4:
                counter += 1
                print("This means you did it for "+color)
                print(lives)
                if color=="yellow":
                    print("The catageory was: "+yellow_random)
                elif color=="green":
                    print("The category was: "+ green_random)
                elif color=="blue":
                    print("The category was: " + blue_random)
                elif color=="purple":
                    print("The category was: " + purple_random)
                else:
                    print("huh? ")
            elif len(correct_guesses[color])==3:
                print("1 away for "+ color)
            else:
                print("nope, for "+color)

        if previousCount==counter:
            lives-=1
            print("Chances ", lives)
        previousCount = counter
        if counter==4:
            print("All answers: "+ str(categories))
    
    print("All answers: "+ str(categories))
actual_game()






