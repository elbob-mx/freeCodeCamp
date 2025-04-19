import random

# random number generator
def randint(min=0, max=100):
    winning_number = random.randint(min, max)
    return winning_number

# declare winning number
winning_number = randint()
# paid tickets & age
age = 37


# define raffle function & own number
def raffle(winning_number):
    
    global tickets_paid
    
    if age >= 18:
        
        #pay tickets
        print(f"Welcome! Please buy your lottery ticket(s).")
        tickets_paid = 2
        print(f"Thanks for buying {tickets_paid} tickets. Let's start!")
        
        #declare your number to play
        your_number = randint(1, 100)
        # print(f"You have {tickets_paid} chances to win.")
        print(f"Your number is: {your_number}")

        # each attempt removes one tickets_paid
        attempts = tickets_paid
        while attempts >= 1:
            # each attempt removes one tickets_paid
            attempts -= 1
            print("You have", attempts, "attempts left.")        

        for number in range(1,100):
            
            # check if winning number is equal to your number
            if your_number == winning_number:
                print("Your number is:", randint())
                print(f"The winning number is: {winning_number}")
                print("You have won the lottery!, go buy more tickets!")
                print(f"It took attempts: {attempts}")
                break
            else:
                print("You're a loser!, stop betting with your wife's money!")
                print(f"The winning number was: {winning_number}")
                print("Better luck next time!")
                break
        else:
            print("You have not paid for the ticket.")
    else:
        print("You are not old enough to play the lottery. You must be at least 18 years old.")
        print("Please come back when you are older.")        
                
raffle(winning_number)