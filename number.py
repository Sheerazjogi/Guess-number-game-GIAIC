# project : Guess thr number Game By Computer
# 1 to 100 numbers.

import random  # Random number generate karne ke liye module import kiya

def guess_the_number():
    """Project: Guess The Number Game By Computer."""
    
    # 1 se 100 ke darmiyan ek random number generate karega
    number = random.randint(1, 100)
    
    guesses_left = 7  # Player ke paas 7 guesses hain
    
    # Welcome message
    print("Welcome to the number guessing game")
    print("I am thinking of a number between 1 to 100")

    # Jab tak guesses bachay hain, loop chalta rahega
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")  # Bacha hua guesses show karega
        
        try:
            guess = int(input("Take a guess: "))  # User se number input lega
        except ValueError:  # Agar user number ke ilawa kuch aur likhta hai toh error show karega
            print("Invalid input: Please enter a number.")
            continue  # Dobara input lene ke liye continue karega
        
        # Agar guess chhota hai toh ye message show hoga
        if guess < number:
            print("Too low! Try again.")
        
        # Agar guess bara hai toh ye message show hoga
        elif guess > number:
            print("Too high! Try again.")
        
        # Agar guess sahi hai toh jeetne ka message show hoga aur function exit karega
        else:
            print(f"Congratulations! You got the correct number in {7 - guesses_left + 1} tries.")
            return  # Game yahan end hoga
        
        guesses_left -= 1  # Har guess ke baad ek chance kam ho jayega

    # Agar sare guesses khatam ho jayein toh ye message show hoga
    print(f"\nYou ran out of guesses. The number was {number}.")

# Function ko call kiya gaya taake game start ho
guess_the_number()