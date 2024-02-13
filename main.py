import random
logo="""
 $$$$$$\                                                $$$$$$$$\ $$\                       $$\   $$\                         $$\                                 
$$  __$$\                                               \__$$  __|$$ |                      $$$\  $$ |                        $$ |                                
$$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\          $$ |   $$$$$$$\   $$$$$$\        $$$$\ $$ |$$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\        
$$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|         $$ |   $$  __$$\ $$  __$$\       $$ $$\$$ |$$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\       
$$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\           $$ |   $$ |  $$ |$$$$$$$$ |      $$ \$$$$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|      
$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\          $$ |   $$ |  $$ |$$   ____|      $$ |\$$$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |            
\$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |         $$ |   $$ |  $$ |\$$$$$$$\       $$ | \$$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |            
 \______/  \______/  \_______|\_______/ \_______/          \__|   \__|  \__| \_______|      \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|            
"""
#from art import logo
#Number Guessing Game Objectives:
# Include an ASCII art logo.
#-->>Text to ASCII Art Generator (TAAG)-->>Web-Site.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
#########################################
print(logo)
correct_Answer = random.randint(1,100)
easy_attempts = 10
hard_attempts = 5
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#print(f"Pssst, the correct answer is {correct_Answer}")
choose_Difficult=str(input("Choose a difficulty. Type 'easy' or 'hard': "))
if choose_Difficult=='easy':
    while True:
        print(f"You have {easy_attempts} attempts remaining to guess the number.")
        make_Guess=int(input("Make a guess: "))
        if make_Guess==correct_Answer:
            print(f"You got it! The answer was {correct_Answer}.")
            break
        elif easy_attempts==1:
            print("You've run out of guesses, you lose.")
            break
        elif make_Guess<correct_Answer:
            print("Too low.")
            print("Guess again.")
            easy_attempts=easy_attempts-1
        elif make_Guess>correct_Answer:
            print("Too high.")
            print("Guess again.")
            easy_attempts=easy_attempts-1
elif choose_Difficult=='hard':
    while True:
        print(f"You have {hard_attempts} attempts remaining to guess the number.")
        make_Guess = int(input("Make a guess: "))
        if make_Guess == correct_Answer:
            print(f"You got it! The answer was {correct_Answer}.")
            break
        elif hard_attempts == 1:
            print("You've run out of guesses, you lose.")
            break
        elif make_Guess < correct_Answer:
            print("Too low.")
            print("Guess again.")
            hard_attempts = hard_attempts - 1
        elif make_Guess > correct_Answer:
            print("Too high.")
            print("Guess again.")
            hard_attempts = hard_attempts - 1
else:
    print("The choose is Error.")
################################
################################
