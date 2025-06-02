import os
import subprocess

def fun1():
    print("\n--- Feature 1: Dynamic Expression Evaluation ---")
    user_expression = input("Enter a Python expression to evaluate (e.g., 2+2 or os.system('ls')): ")
    try:
        result = eval(user_expression)
        print(f"Result of your expression: {result}")
    except Exception as e:
        print(f"Error evaluating expression: {e}")

def fun2():
    print("\n--- Feature 2: Shell Command Execution ---")
    filename = input("Enter a filename to display (e.g., test.txt or '; rm -rf /'): ")
    print(f"Attempting to display content of: {filename}")
    try:
        subprocess.run(f"cat {filename}", shell=True, check=True)
        print("Command executed successfully (if file exists).")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    except FileNotFoundError:
        print("Error: 'cat' command not found or file does not exist.")

HARDCODED_API_KEY = "SUPER_SECRET_API_KEY_12345"
HARDCODED_PASSWORD = "adminpassword123"

def fun3():
    print("\n--- Feature 3: Embedded Configuration Data ---")
    print(f"API Key: {HARDCODED_API_KEY}")
    print(f"Password: {HARDCODED_PASSWORD}")
    print("These are directly accessible within the script.")

def fun4():
    print("\n--- Feature 4: Basic Numeric Processing ---")
    user_number_str = input("Enter a number: ")
    try:
        number = int(user_number_str)
        result = number * 2
        print(f"Your number doubled: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def fun5():
    print("\n--- Feature 5: Simple Data Obfuscation (Conceptual) ---")
    print("This module represents a basic method for data transformation, not robust encryption.")
    print("It uses a straightforward approach for illustrative purposes.")


if __name__ == "__main__":
    print("--- Demonstration Project ---")

    fun1()
    fun2()
    fun3()
    fun4()
    fun5()

    print("\n--- End of Demonstration ---")
