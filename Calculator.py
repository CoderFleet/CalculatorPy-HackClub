# Must Do Before use for you guys:- pip install colorama

import time
from math import sqrt
from colorama import Back, Fore, Style, init

init(autoreset=True)

calculation_history = []
memory = None
custom_labels = {
    '1': 'Add',
    '2': 'Subtract',
    '3': 'Multiply',
    '4': 'Divide',
    '5': 'Modulus',
    '6': 'Power',
    '7': 'Square Root',
    '8': 'Percentage',
}
custom_operations = {}
welcome_message = """
*****************************
*                           *
*    Welcome to the         *
*    Command Line           *
*    Calculator!            *
*                           *
*****************************
"""

def set_custom_labels():
    print(Fore.YELLOW + "\nSet custom labels for operations:")
    for key in custom_labels.keys():
        label = input(Fore.LIGHTGREEN_EX + f"Enter label for {custom_labels[key]} (or press Enter to keep current): ")
        if label:
            custom_labels[key] = label

def add_custom_operation():
    name = input(Fore.LIGHTGREEN_EX + "Enter the name of the custom operation: ")
    operation = input(Fore.LIGHTGREEN_EX + "Enter the operation in terms of x and y (e.g., x + y * y): ")
    custom_operations[name] = operation
    print(Fore.GREEN + f"Custom operation '{name}' added.")

def list_custom_operations():
    if not custom_operations:
        print(Fore.YELLOW + "No custom operations defined.")
        return
    print(Fore.YELLOW + "Custom operations:")
    for name, operation in custom_operations.items():
        print(Fore.CYAN + f"{name}: {operation}")

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

def modulus(x, y):
    if y == 0:
        return "Error! Division by zero."
    result = x % y
    calculation_history.append(f"{x} % {y} = {result}")
    return result

def power(x, y):
    result = x ** y
    calculation_history.append(f"{x} ^ {y} = {result}")
    return result

def square_root(x):
    result = sqrt(x)
    calculation_history.append(f"sqrt({x}) = {result}")
    return result

def percentage(x, y):
    result = (x / y) * 100
    calculation_history.append(f"({x} / {y}) * 100 = {result}%")
    return result

def execute_custom_operation(name, x, y):
    operation = custom_operations.get(name)
    if operation:
        try:
            result = eval(operation)
            calculation_history.append(f"{name}({x}, {y}) = {result}")
            return result
        except Exception as e:
            return f"Error in custom operation: {e}"
    else:
        return "Custom operation not found."

def print_history():
    print(Fore.YELLOW + "\nCalculation History:")
    if not calculation_history:
        print("No calculations yet.")
    for calculation in calculation_history:
        print(Fore.CYAN + calculation)

def clear_history():
    global calculation_history
    calculation_history = []
    print(Fore.YELLOW + "\nCalculation history cleared.")

def store_memory(value):
    global memory
    memory = value
    print(Fore.YELLOW + f"\nStored {value} in memory.")

def recall_memory():
    if memory is None:
        return "No value stored in memory."
    return memory

def print_welcome():
    print(Fore.YELLOW + welcome_message)

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

def get_numbers():
    while True:
        try:
            x = float(input(Fore.CYAN + "Enter first number: "))
            y = float(input(Fore.CYAN + "Enter second number: "))
            return x, y
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter numeric values.")

def get_single_number():
    while True:
        try:
            x = float(input(Fore.CYAN + "Enter a number: "))
            return x
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a numeric value.")

operations = {
    '1': ('Add', add),
    '2': ('Subtract', subtract),
    '3': ('Multiply', multiply),
    '4': ('Divide', divide),
    '5': ('Modulus', modulus),
    '6': ('Power', power),
    '7': ('Square Root', square_root),
    '8': ('Percentage', percentage),
}

def main():
    print_welcome()
    time.sleep(1)
    print(Fore.BLUE + "You can perform basic arithmetic operations: addition, subtraction, multiplication, and division.... in this")
    time.sleep(1)
    set_custom_labels()
    while True:
        print(Fore.CYAN + "\nOptions:")
        for key, (name, _) in operations.items():
            print(Fore.CYAN + f"{key}. {custom_labels[key]}")
        print(Fore.CYAN + "9. Calculation History")
        print(Fore.CYAN + "10. Clear Calculation History")
        print(Fore.CYAN + "11. Store Memory")
        print(Fore.CYAN + "12. Recall Memory")
        print(Fore.CYAN + "13. Set Custom Labels")
        print(Fore.CYAN + "14. Add Custom Operation")
        print(Fore.CYAN + "15. List Custom Operations")
        for i, custom_name in enumerate(custom_operations.keys(), start=16):
            print(Fore.CYAN + f"{i}. {custom_name}")
        print(Fore.CYAN + f"{len(custom_operations) + 16}. Exit")
        choice = input(Fore.LIGHTGREEN_EX + "Select an operation: ")

        if choice in operations:
            if choice == '7':  # Square Root
                x = get_single_number()
                result = operations[choice][1](x)
                print(Fore.GREEN + f"\n{result} is the square root of {x}")
            elif choice == '8':  # Percentage
                x, y = get_numbers()
                result = operations[choice][1](x, y)
                print(Fore.GREEN + f"\n{result}% is the percentage of {x} relative to {y}")
            else:
                x, y = get_numbers()
                result = operations[choice][1](x, y)
                if result == "Error! Division by zero.":
                    print(Fore.RED + f"\n{result}")
                else:
                    print(Fore.GREEN + f"\n{result} is the result of {custom_labels[choice].lower()}ing {x} and {y}")
        elif choice == '9':
            print_history()
        elif choice == '10':
            clear_history()
        elif choice == '11':
            value = get_single_number()
            store_memory(value)
        elif choice == '12':
            result = recall_memory()
            print(Fore.GREEN + f"\nRecalled value from memory: {result}")
        elif choice == '13':
            set_custom_labels()
        elif choice == '14':
            add_custom_operation()
        elif choice == '15':
            list_custom_operations()
        elif choice.isdigit() and int(choice) in range(16, 16 + len(custom_operations)):
            x, y = get_numbers()
            custom_operation_name = list(custom_operations.keys())[int(choice) - 16]
            result = execute_custom_operation(custom_operation_name, x, y)
            if "Error" in str(result):
                print(Fore.RED + f"\n{result}")
            else:
                print(Fore.GREEN + f"\n{result} is the result of {custom_operation_name} with {x} and {y}")
        elif choice == str(len(custom_operations) + 16):
            print_goodbye()
            break
        else:
            print(Fore.RED + "Invalid input. Please select a valid option.")

# Run the main loop
main()
