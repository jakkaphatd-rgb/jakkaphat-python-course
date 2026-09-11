import random

def get_parity_hint(number):
   if number % 2 == 0:
       return "HINT: The number is even"
   else:
       return "HINT: The number is odd"

def get_divisibility_hint(number):
   if number % 3 == 0:
       return "HINT: The number is divisible by 3"
   elif number % 5 == 0:
       return "HINT: The number is divisible by 5"
   else:
       return "HINT: The number is NOT divisible by 3 or 5"

def get_range_hint(number, current_min=1, current_max=100):
   hint_min = max(1, number - 12)
   hint_max = min(100, number + 12)
   return f"HINT: The number is between {hint_min} and {hint_max}"

def get_thefirst_digit_hint(number):
   first_digit = str(number)[0]
   return f"HINT: The first digit is {first_digit}"

def guessing_game():
   target_number = random.randint(1, 100)
   attempt = 0
   wrong_guesses = 0
   print("=== Enhanced GUESSING GAME ===")
   print("Guess my number between 1 and 100!")
   print("You have unlimited attempts.")
   print()
   while True:
       attempt += 1
       guess = int(input(f"Attempt {attempt} - Enter your guess: "))
       if guess < target_number:
           print("Too low! Try again.")
           wrong_guesses += 1
       elif guess > target_number:
           print("Too high! Try again.")
           wrong_guesses += 1
       else:
           print(f"Congratulations! You won in {attempt} attempts!")
           break
       # หลังทายผิด 3 ครั้ง
       if wrong_guesses == 3:
           print(get_parity_hint(target_number))
       # หลังทายผิด 5 ครั้ง
       if wrong_guesses == 5:
           print(get_divisibility_hint(target_number))
       # หลังทายผิด 7 ครั้ง
       if wrong_guesses == 7:
           print(get_range_hint(target_number))
       # หลังทายผิด 10 ครั้ง
       if wrong_guesses == 10:
           print(get_thefirst_digit_hint(target_number))

guessing_game()
has context menu