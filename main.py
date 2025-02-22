"""
Exercise 1: Guess the number
Exercise 2: Multiplication table
Exercise 3: Basic calculator
"""

import random

def guess_the_number():
  target_number = random.randint(1, 10)

  attempts = 0
  while True:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1

    if guess < target_number:
      print("Too low. Try Again")
    elif guess > target_number:
      print("Too high. Try Again")
    else:
      print(f"Congratulations! You guessed the number ({target_number}) in {attempts} attempts.")
      break


def multiplication_table():
  number = int(input("Enter an integer: "))

  print(f"Multiplication Table for {number}:")
  # Fix code
  # implement a for loop
  i = 1 # fix code
  for i in range(11):
    result = number * i # fix code
    print(f"{number} x {i} = {result}")
    


def basic_calculator():
  num1 = float(input("Enter the first number: "))
  operator = input("Enter an operator (+, -, *, /): ")
  num2 = float(input("Enter the second number: "))

  if operator == "+" :
    result = num1 + num2
  elif operator == "-" :
    result = num1 - num2 
  elif operator == "*":
    result = num1 * num2
  elif operator == "/" :
    result = num1 / num2 
  else:
    result = "Invalid operator"
  print("Result:", result)
 


def main():
  # input choice between 1-3 function
  # call the function
  choice = int(input(f"""
    1. Guess the number
    2. Multiplication table
    3. Basic calculator
    Enter a number (1-3): """))
  if choice == 1:
    guess_the_number()
  elif choice == 2:
    multiplication_table()
  elif choice == 3:
    basic_calculator()
  else:
    print("Invalid choice.")

main()