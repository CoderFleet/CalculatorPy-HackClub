def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
      return "Error! Division by zero."
  return x / y


# print(subtract(5, 3))
# print(multiply(4, 2))
# print(divide(10, 2))
# print(divide(10, 0))

def get_numbers():
  x = float(input("Enter first number: "))
  y = float(input("Enter second number: "))
  return x, y

def main():
  while True:
      print("Options:")
      print("1. Add")
      print("2. Subtract")
      print("3. Multiply")
      print("4. Divide")
      print("5. Exit")
      choice = input("Select an operation (1/2/3/4/5): ")

      if choice in ['1', '2', '3', '4']:
          x, y = get_numbers()
          if choice == '1':
              print(f"The result is: {add(x, y)}")
          elif choice == '2':
              print(f"The result is: {subtract(x, y)}")
          elif choice == '3':
              print(f"The result is: {multiply(x, y)}")
          elif choice == '4':
              print(f"The result is: {divide(x, y)}")
      elif choice == '5':
          print("Exiting the calculator. Goodbye!")
          break
      else:
          print("Invalid input. Please select a valid option.")

main()

