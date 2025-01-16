import random

#9.1
for i in range(0,5):
  print(random.randint(1,100))

#9.2
def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = random.randint(1, 100)
print("Random number:", number)
print("Is prime:", isprime(number))

#9.3
print("Rolled a die ", random.randint(1, 6))

#9.4
nums=[1, 2, 3, 4, 5]
random.shuffle(nums)
print("Shuffled list ",nums)

#9.5
stud = ["Reema","Seema","Jeevan"]
print("Randomly selected ", random.choice(stud))

#9.6
import random
import string

length = int(input("Enter password length "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password ",password)

#9.7
import random
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = [f"{rank} of {suit}" for rank in ranks for suit in suits]
print("Randomly picked card ",random.choice(deck))










