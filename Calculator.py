# pip install colorama

import time

from colorama import Back, Fore, Style, init

init(autoreset=True)

calculation_history = []

def add(x, y):
  result = x + y
  calculation_history.append(f"{x} + {y} = {result}")
  return result

def subtract(x, y):
  result = x - y
  calculation_history.append(f"{x} - {y} = {result}")
  return result

def multiply(x, y):
  result = x * y
  calculation_history.append(f"{x} * {y} = {result}")
  return result

def divide(x, y):
  if y == 0:
      return "Error! Division by zero."
  result = x / y
  calculation_history.append(f"{x} / {y} = {result}")
  return result

# Code for Getting History
def print_history():
  print(Fore.YELLOW + "\nCalculation History:")
  if not calculation_history:
      print("No calculations yet.")
  for calculation in calculation_history:
      print(Fore.CYAN + calculation)


def print_welcome():
  print(Fore.YELLOW + """
  *****************************
  *                           *
  *    Welcome to the         *
  *    Command Line           *
  *    Calculator!            *
  *                           *
  *****************************
  """)

def print_goodbye():
  print(Fore.YELLOW + """
  *****************************
  *                           *
  *    Thank you for using    *
  *    the Calculator!        *
  *    Goodbye!               *
  *                           *
  *****************************
  """)

# print(subtract(5, 3))
# print(multiply(4, 2))
# print(divide(10, 2))
# print(divide(10, 0))

def get_numbers():
  while True:
      try:
          x = float(input(Fore.CYAN + "Enter first number: "))
          y = float(input(Fore.CYAN + "Enter second number: "))
          return x, y
      except ValueError:
          print(Fore.RED + "Invalid input. Please enter numeric values.")

def main():
  print_welcome()
  time.sleep(1)
  print(Fore.BLUE + "You can perform basic arithmetic operations: addition, subtraction, multiplication, and division.... in this")
  time.sleep(1)
  while True:
      print(Fore.CYAN + "\nOptions:")
      print(Fore.CYAN + "1. Add")
      print(Fore.CYAN + "2. Subtract")
      print(Fore.CYAN + "3. Multiply")
      print(Fore.CYAN + "4. Divide")
      print(Fore.CYAN + "5. Calculation History")
      print(Fore.CYAN + "6. Exit")
      choice = input(Fore.LIGHTGREEN_EX + "Select an operation (1/2/3/4/5/6): ")

      if choice in ['1', '2', '3', '4']:
          x, y = get_numbers()
          if choice == '1':
            print(Fore.GREEN + f"\n{add(x, y)} is the sum of {x} and {y}")
          elif choice == '2':
            print(Fore.GREEN + f"\n{subtract(x, y)} is the difference between {x} and {y}")
          elif choice == '3':
            print(Fore.GREEN + f"\n{multiply(x, y)} is the product of {x} and {y}")
          elif choice == '4':
            result = divide(x, y)
            if result == "Error! Division by zero.":
                print(Fore.RED + f"\n{result}")
            else:
                print(Fore.GREEN + f"\n{result} is the quotient of {x} divided by {y}")

      elif choice == '5':
          print_history()
      elif choice == '6':
          print_goodbye()
          break
      else:
          print(Fore.RED + "Invalid input. Please select a valid option.")

# Run the main loop
main()


