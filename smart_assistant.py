import random
import string

def password_gen():
    length = int(input("Enter password length: "))

    chars = string.ascii_letters + string.digits
    password = ""

    for i in range(length):
        password += random.choice(chars)

    print("Your Password: ", password)


def guess_game():
    num = random.randint(1, 10)
    guess = int(input("Guess number (1-10): "))

    if guess == num:
        print("correct ")
    else:
        print("Wrong , number was", num)

tasks = []

def todo():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")

    ch = input("Enter choice: ")

    if ch == '1':
        task = input("Enter task: ")

        with open("tasks.txt", "a") as f:
            f.write(task + "\n")
     
        print("Task saved ✅")

    elif ch == '2':
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()

            print("Your Tasks:")
            for t in tasks:
                print("-", t.strip())

        except FileNotFoundError:
            print("No tasks found ❌")


    elif ch == '2':
        print("Your Tasks:")
        for t in tasks:
            print("-", t)

    elif ch == '3':
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()
            
            if not tasks:
                print("No tasks to delte ❌")
                return
            
            tasks.pop()

            with open("tasks.txt", "w") as f:
                f.writelines(tasks)

            print("Task deleted ✅")

        except FileNotFoundError:
            print("No tasks found ❌")


def calculator():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input ❌")
        return

    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        print("Result: ", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        print("Result:", a / b)
    else:
        print("Invalid operation")

while True:
    print("\n====== Smart Assistant ======")
    print("1. Calculator")
    print("2. Guess Game")
    print("3. To-Do List")
    print("4. Exit")
    print("5. Password Generator")

    choice = input("Enter your choice: ")

    if choice == '1':
        calculator()

    elif choice == '2':
        guess_game()

    elif choice == '3':
        todo()

    elif choice == '4':
        print("Program band ho gaya")
        break
    
    elif choice == '5':
        password_gen()

    else:
        print("Invalid choice")