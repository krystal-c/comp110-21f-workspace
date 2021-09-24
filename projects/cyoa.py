# Greeting the player and asking player for their name

def greet():
    print("""The Disney princess line up are recognized from all across the world, 
    symbolizing kindness, courage, and strength, while also providing us with unique sets of stories 
    and personalities! In this quiz, we'll be testing the question of which of the Disney Princess are you?""")
    global player
    player = (input("What's your name?: "))
    print("Well, nice to meet you! " + player)
    print("none")

    # Count points and mention players name


def main():
    global player

    global points_Tiana
    points_Tiana = 0

    global points_Ariel
    points_Ariel = 0

    global points_Rapunzel
    points_Rapunzel = 0

    global points_Cinderella
    points_Cinderella = 0

    global points_Belle
    points_Belle = 0 

    global points
    points = 0
    points = int(points_Belle + points_Cinderella + points_Rapunzel + points_Ariel + points_Tiana)

    playgame = True

    while playgame is True:         
        print("Alright " + player + ", it seems like you're ready. If that's the case, then lets begin! Remember to type answers word for word!")
            
        again = str(input("Thank you so much for playing! Do you want to play again? Type yes or no"))
        if (again == "yes"):
            procedure_1() 
            procedure_2
            procedure_3
            procedure_4
            procedure_5
            playgame = True
        if (again == "no"): 
            playgame = False  


def procedure_1():
    global player

    global points_Tiana
    global points_Ariel
    global points_Belle
    global points_Cinderella
    global points_Rapunzel
    global points

    print("First things first, " + player + """, which personality trait do you like best about yourself?
        My curiosity
        My hard working attitude
        My free spirit
        My intellegence
        My desire to help others""")
    answer1_Ariel = "My curiosity"
    answer1_Tiana = "My hardworking spirit"
    answer1_Rapunzel = "My free spirit"
    answer1_Belle = "My intellegence"
    answer1_Cinderella = "My desire to help others"
    response1 = input("Your answer is: ")
    if (response1 == answer1_Ariel):
        points_Ariel = points_Ariel + 1
        print("Hey " + player + " you just got an Ariel point!")
    if (response1 == answer1_Belle):
        points_Belle = points_Belle + 1
        print("Hey " + player + " you just got an Belle point!")
    if (response1 == answer1_Cinderella):
        points_Cinderella = points_Cinderella + 1
        print("Hey " + player + " you just got an Cinderella point!")
    if (response1 == answer1_Rapunzel):
        points_Rapunzel == points_Rapunzel + 1
        print("Hey " + player + " you just got an Rapunzel point!")
    if (response1 == answer1_Tiana):
        points_Tiana = points_Tiana + 1 
        print("Hey " + player + " you just got an Tiana point!")
    print("So far you've gotten " + str(points) + " points!")


def procedure_2():
    global player

    global points_Tiana
    global points_Ariel
    global points_Belle
    global points_Cinderella
    global points_Rapunzel
    global points

    print("Good job, " + player + """, now, what is your favorite color?
        Red
        Green
        Purple
        Yellow
        Blue""")
    answer2_Ariel = "Red"
    answer2_Tiana = "Green"
    answer2_Rapunzel = "Purple"
    answer2_Belle = "Yellow"
    answer2_Cinderella = "Blue"

    response2 = input("Your answer is: ")

    if (response2 == answer2_Ariel):
        points_Ariel = points_Ariel + 1
        print("Hey " + player + " you just got an Ariel point!")
    if (response2 == answer2_Belle):
        points_Belle = points_Belle + 1
        print("Hey " + player + " you just got an Belle point!")
    if (response2 == answer2_Cinderella):
        points_Cinderella = points_Cinderella + 1
        print("Hey " + player + " you just got an Cinderella point!")
    if (response2 == answer2_Rapunzel):
        points_Rapunzel == points_Rapunzel + 1
        print("Hey " + player + " you just got an Rapunzel point!")
    if (response2 == answer2_Tiana):
        points_Tiana = points_Tiana + 1 
        print("Hey " + player + " you just got an Tiana point!")
        
    print("So far you've gotten " + str(points) + " points!")


def procedure_3():
    global player

    global points_Tiana
    global points_Ariel
    global points_Belle
    global points_Cinderella
    global points_Rapunzel
    global points

    print("Okay, " + player + """, lets relax a bit... Which activity would you do during your freetime? 
        Collecting random objects
        Cooking while singing a tune
        Painting pretty pictures
        Reading while people watching
        Cleaning...""")

    answer3_Ariel = "Collecting random objects"
    answer3_Tiana = "Cooking while singing a tune"
    answer3_Rapunzel = "Painting pretty pictures"
    answer3_Belle = "Reading while people watching"
    answer3_Cinderella = "Cleaning..."

    response3 = input("Your answer is: ")

    if (response3 == answer3_Ariel):
        points_Ariel = points_Ariel + 1
        print("Hey " + player + " you just got an Ariel point!")
    if (response3 == answer3_Belle):
        points_Belle = points_Belle + 1
        print("Hey " + player + " you just got an Belle point!")
    if (response3 == answer3_Cinderella):
        points_Cinderella = points_Cinderella + 1
        print("Hey " + player + " you just got an Cinderella point!")
    if (response3 == answer3_Rapunzel):
        points_Rapunzel == points_Rapunzel + 1
        print("Hey " + player + " you just got an Rapunzel point!")
    if (response3 == answer3_Tiana):
        points_Tiana = points_Tiana + 1 
        print("Hey " + player + " you just got an Tiana point!")
        
    print("So far you've gotten " + str(points) + " points!")


def procedure_4():
    global player

    global points_Tiana
    global points_Ariel
    global points_Belle
    global points_Cinderella
    global points_Rapunzel
    global points

    print("Alrighty, " + player + """, what is your biggest fear/pet peeve?
        Overprotective parents
        Faliure
        Small confined spaces 
        Ignorance
        Mistreatment""")

    answer4_Ariel = "Overprotective parents"
    answer4_Tiana = "Faliure"
    answer4_Rapunzel = "Small confined spaces"
    answer4_Belle = "Ignorance"
    answer4_Cinderella = "Mistreatment"

    response4 = input("Your answer is: ")

    if (response4 == answer4_Ariel):
        points_Ariel = points_Ariel + 1
        print("Hey " + player + " you just got an Ariel point!")
    if (response4 == answer4_Belle):
        points_Belle = points_Belle + 1
        print("Hey " + player + " you just got an Belle point!")
    if (response4 == answer4_Cinderella):
        points_Cinderella = points_Cinderella + 1
        print("Hey " + player + " you just got an Cinderella point!")
    if (response4 == answer4_Rapunzel):
        points_Rapunzel == points_Rapunzel + 1
        print("Hey " + player + " you just got an Rapunzel point!")
    if (response4 == answer4_Tiana):
        points_Tiana = points_Tiana + 1 
        print("Hey " + player + " you just got an Tiana point!")
        
    print("So far you've gotten " + str(points) + " points!")


def procedure_5():
    global player

    global points_Tiana
    global points_Ariel
    global points_Belle
    global points_Cinderella
    global points_Rapunzel
    global points

    print("Lastly, " + player + """, what personality trait are you looking for in a soulmate (choose your top pick)?
        Adventurous
        Ambitious
        Charismatic
        Gentleness 
        Romantic""")

    answer5_Ariel = "Adventurous"
    answer5_Tiana = "Ambitious"
    answer5_Rapunzel = "Charismatic"
    answer5_Belle = "Gentleness"
    answer5_Cinderella = "Romantic"

    response5 = input("Your answer is: ")

    if (response5 == answer5_Ariel):
        points_Ariel = points_Ariel + 1
        print("Hey " + player + " you just got an Ariel point!")
    if (response5 == answer5_Belle):
        points_Belle = points_Belle + 1
        print("Hey " + player + " you just got an Belle point!")
    if (response5 == answer5_Cinderella):
        points_Cinderella = points_Cinderella + 1
        print("Hey " + player + " you just got an Cinderella point!")
    if (response5 == answer5_Rapunzel):
        points_Rapunzel == points_Rapunzel + 1
        print("Hey " + player + " you just got an Rapunzel point!")
    if (response5 == answer5_Tiana):
        points_Tiana = points_Tiana + 1 
        print("Hey " + player + " you just got an Tiana point!")
    
    print("So far you've gotten " + str(points) + " points!")


def function():
    global player

    global points_Tiana
    global points_Ariel
    global points_Belle
    global points_Cinderella
    global points_Rapunzel
    global points

    print("Congratulations, you've finished the game! Now it's time to reveal which Disney princess you are!")
    if (points_Ariel > points):
        print("You are Ariel! ___")
    if (points_Tiana > points):
        print("You are Tiana! ___")
    if (points_Belle > points): 
        print("You are Belle! ___")
    if (points_Cinderella > points):
        print("You are Cinderella! ___")
    if (points_Rapunzel > points):
        print("You are Rapunzel! ___")

# Learn how to add up all points and get an output that results in whichever has the most points (9/23/2021)


if __name__ == "__main__":
    main()