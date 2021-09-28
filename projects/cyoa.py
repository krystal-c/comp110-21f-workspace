"""PJ00 - Code Your Own Game Project."""

__author__ = "730482618"


global player
player = input("Welcome to the Disney Princess Buzzfeed Quiz! In this quiz, we'll be testing the question of which of the Disney Princess are you! What is your name?: ")


def greet(player):
    print(f"Alright, it seems like you're ready {player}. If that's the case, then lets begin! Remember to type answers word for word!")


def main():
    """This is the main function for PJ00."""
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
    points = points_Ariel + points_Belle + points_Cinderella + points_Rapunzel + points_Tiana

    print("Alright, it seems like you're ready. If that's the case, then lets begin! Remember to type answers word for word!")


def procedure_1(player) -> None:
    global points_Tiana
    points_Tiana = 0 + points_Tiana
    global points_Ariel
    points_Ariel = 0 + points_Ariel
    global points_Rapunzel
    points_Rapunzel = 0 + points_Rapunzel
    global points_Cinderella
    points_Cinderella = 0 + points_Cinderella
    global points_Belle
    points_Belle = 0 + points_Belle
    global points
    points = points_Ariel + points_Belle + points_Cinderella + points_Rapunzel + points_Tiana

    print("Alright, it seems like you're ready. If that's the case, then lets begin! Remember to type answers word for word!")
    print(f"""First things first, {player}, which personality trait do you like best about yourself?
        My curiosity
        My hardworking attitude
        My free spirit
        My intellegence
        My desire to help others""")

    answer1_Ariel = "My curiosity"
    answer1_Tiana = "My hardworking attitude"
    answer1_Rapunzel = "My free spirit"
    answer1_Belle = "My intellegence"
    answer1_Cinderella = "My desire to help others"
    response1 = input("Your answer is: ")

    if (response1 == answer1_Ariel):
        points_Ariel = points_Ariel + 1 
        print(f"Hey {player} you just got an Ariel point!")
    if (response1 == answer1_Belle):
        points_Belle = points_Belle + 1
        print(f"Hey {player} you just got an Belle point!")
    if (response1 == answer1_Cinderella):
        points_Cinderella = points_Cinderella + 1
        print(f"Hey {player} you just got an Cinderella point!")
    if (response1 == answer1_Rapunzel):
        points_Rapunzel = points_Rapunzel + 1 
        print(f"Hey {player} you just got an Rapunzel point!")
    if (response1 == answer1_Tiana):
        points_Tiana = points_Tiana + 1 
        print(f"Hey {player} you just got an Tiana point!")
    print(f"So far you've gotten {points} points in total!")
    
    procedure_1(player)


def procedure_2(player) -> None:
    global points_Tiana
    points_Tiana = 0 + points_Tiana
    global points_Ariel
    points_Ariel = 0 + points_Ariel
    global points_Rapunzel
    points_Rapunzel = 0 + points_Rapunzel
    global points_Cinderella
    points_Cinderella = 0 + points_Cinderella
    global points_Belle
    points_Belle = 0 + points_Belle
    global points
    points = points_Ariel + points_Belle + points_Cinderella + points_Rapunzel + points_Tiana
    print(f"""Good job, {player}, now, what is your favorite color?
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
        print(f"Hey {player} you just got an Ariel point!")
    if (response2 == answer2_Belle):
        points_Belle = points_Belle + 1
        print(f"Hey {player} you just got an Belle point!")
    if (response2 == answer2_Cinderella):
        points_Cinderella = points_Cinderella + 1
        print(f"Hey {player} you just got an Cinderella point!")
    if (response2 == answer2_Rapunzel):
        points_Rapunzel == points_Rapunzel + 1
        print(f"Hey {player} you just got an Rapunzel point!")
    if (response2 == answer2_Tiana):
        points_Tiana = points_Tiana + 1 
        print(f"Hey {player} you just got an Tiana point!")
    
    print(f"So far you've gotten {points} points in total!")  

    procedure_2(player)


def procedure_3(player) -> None:
    global points_Tiana
    points_Tiana = 0 + points_Tiana
    global points_Ariel
    points_Ariel = 0 + points_Ariel
    global points_Rapunzel
    points_Rapunzel = 0 + points_Rapunzel
    global points_Cinderella
    points_Cinderella = 0 + points_Cinderella
    global points_Belle
    points_Belle = 0 + points_Belle
    global points
    points = points_Ariel + points_Belle + points_Cinderella + points_Rapunzel + points_Tiana

    print(f"""Okay, {player}, lets relax a bit... Which activity would you do during your freetime? 
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
        print(f"Hey {player} you just got an Ariel point!")
    if (response3 == answer3_Belle):
        points_Belle = points_Belle + 1
        print(f"Hey {player} you just got an Belle point!")
    if (response3 == answer3_Cinderella):
        points_Cinderella = points_Cinderella + 1
        print(f"Hey {player} you just got an Cinderella point!")
    if (response3 == answer3_Rapunzel):
        points_Rapunzel == points_Rapunzel + 1
        print(f"Hey {player} you just got an Rapunzel point!")
    if (response3 == answer3_Tiana):
        points_Tiana = points_Tiana + 1 
        print(f"Hey {player} you just got an Tiana point!")
        
    print(f"So far you've gotten {points} points in total!")

    procedure_3(player)


def procedure_4(player) -> None:
    global points_Tiana
    points_Tiana = 0 + points_Tiana
    global points_Ariel
    points_Ariel = 0 + points_Ariel
    global points_Rapunzel
    points_Rapunzel = 0 + points_Rapunzel
    global points_Cinderella
    points_Cinderella = 0 + points_Cinderella
    global points_Belle
    points_Belle = 0 + points_Belle

    print(f"""Alrighty, {player}, what is your biggest fear/pet peeve?
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
        print(f"Hey {player} you just got an Ariel point!")
    if (response4 == answer4_Belle):
        points_Belle = points_Belle + 1
        print(f"Hey {player} you just got an Belle point!")
    if (response4 == answer4_Cinderella):
        points_Cinderella = points_Cinderella + 1
        print(f"Hey {player} you just got an Cinderella point!")
    if (response4 == answer4_Rapunzel):
        points_Rapunzel == points_Rapunzel + 1
        print(f"Hey {player} you just got an Rapunzel point!")
    if (response4 == answer4_Tiana):
        points_Tiana = points_Tiana + 1 
        print(f"Hey {player}, you just got an Tiana point!")
        
    global points
    points = points_Ariel + points_Belle + points_Cinderella + points_Rapunzel + points_Tiana

    print(f"So far you've gotten {points} points!")

    procedure_4(player)


def procedure_5(player) -> None:
    global points_Tiana
    points_Tiana = 0 + points_Tiana
    global points_Ariel
    points_Ariel = 0 + points_Ariel
    global points_Rapunzel
    points_Rapunzel = 0 + points_Rapunzel
    global points_Cinderella
    points_Cinderella = 0 + points_Cinderella
    global points_Belle
    points_Belle = 0 + points_Belle
    global points
    points = points_Ariel + points_Belle + points_Cinderella + points_Rapunzel + points_Tiana

    print(f"""Lastly, {player} , what personality trait are you looking for in a soulmate (choose your top pick)?
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
        print(f"Hey {player} you just got an Ariel point!")
    if (response5 == answer5_Belle):
        points_Belle = points_Belle + 1
        print(f"Hey {player} you just got an Belle point!")
    if (response5 == answer5_Cinderella):
        points_Cinderella = points_Cinderella + 1
        print(f"Hey {player} you just got an Cinderella point!")
    if (response5 == answer5_Rapunzel):
        points_Rapunzel == points_Rapunzel + 1
        print(f"Hey {player} you just got an Rapunzel point!")
    if (response5 == answer5_Tiana):
        points_Tiana = points_Tiana + 1 
        print(f"Hey {player} you just got an Tiana point!")

    print(f"You've finally gotten {points} points! That's all of them!")

    print(f"Congratulations {player}, you've finished the game! Now it's time to reveal which Disney princess you are! \U0001F451")
    
    procedure_5(player)


def pick_princess() -> None:
    global points_Tiana
    points_Tiana = 0 + points_Tiana
    global points_Ariel
    points_Ariel = 0 + points_Ariel
    global points_Rapunzel
    points_Rapunzel = 0 + points_Rapunzel
    global points_Cinderella
    points_Cinderella = 0 + points_Cinderella
    global points_Belle
    points_Belle = 0 + points_Belle
    global points
    points = points_Ariel + points_Belle + points_Cinderella + points_Rapunzel + points_Tiana
    if points_Ariel >= points:
        print("""You are Ariel! Ariel is a fun, headstrong, spunky mermaid princess with an adventurous spirit.""")
    if points_Tiana >= points:
        print("You are Tiana! Tiana is a princesss who takes charge, believes in hard work and determination, and has a strong sense of family and prosperity.")
    if points_Belle >= points: 
        print("You are Belle! Belle is an intellegence, opinionated book-worm who has a passion for learning")
    if points_Cinderella >= points:
        print("You are Cinderella! Cinderella is a princess whose entire perspective on life is built around kindess but also optimism for a better future.")
    if points_Rapunzel >= points:
        print("You are Rapunzel! Rapunzel is a creative, adventurous teenage princess who has always been a bit naive, but has proven herself to be very clever despite this.")

    pick_princess()


if __name__ == "__main__":
    main()