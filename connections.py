import random 
def gencat(category_file):
    f=open("wordbanks/" + category_file)
    thefile=f.read()
    #print(thefile)
    this_list=thefile.split("\n")
    #print(this_list)
    category_yellow=[]
    for i in range(0, 4):
        the_word=random.randint(0, len(this_list) - 1)
        this_actual_thing=(this_list[the_word])
        this_list.remove(this_actual_thing)
        category_yellow.append(this_actual_thing)
    return category_yellow


def actual_game():
    yellow_items = gencat("fruits")
    green_items = gencat("disney movies")
    your_guesses=[]
    for i  in range(0, 4):
        your_guess_word= input()
        if your_guess_word in yellow_items:
            print("i'")
            your_guesses.append(your_guess_word)
        else:
            print("uhhh lets circle back")
    print(your_guesses)
    if len(your_guesses)==4:
        print("This means you got it right. ")
    elif len(your_guesses)==3:
        print("One away")
    else:
        print("nope.")
        
        
    
actual_game()

def picking_words():
    




    #print(the_word)
# number_of_words=thefile.count("\n")
# new_list=[]
# new_list.append()
