import tkinter as tk
import random
import string

def calculator():
    calc_win = tk.Toplevel()
    calc_win.title("Calculator")
    calc_win.geometry("300x300")

    tk.Label(calc_win, text="Enter first number").pack()
    num1 =tk.Entry(calc_win)
    num1.pack()

    tk.Label(calc_win, text="Enter second number").pack()
    num2 = tk.Entry(calc_win)
    num2.pack()
    label_result = tk.Label(calc_win, text="Result: ")
    label_result.pack(pady=10)

    def add():
        try:
            result = float(num1.get()) + float(num2.get())
            label_result.config(text="Result: " + str(result))
        except:
            label_result.config(text="Invalid input ❌")

    def sub():
        try:
            result = float(num1.get()) - float(num2.get())
            label_result.config(text="Result: " + str(result))
        except:
            label_result.config(text="Invalid input ❌")

    def mul():
        try:
            result = float(num1.get()) * float(num2.get())
            label_result.config(text="Result: " + str(result))
        except:
            label_result.config(text="Invalid input ❌") 

    def div():
        try:
            n1 = float(num1.get())
            n2 = float(num2.get())
            if n2 == 0:
                label_result.config(text="Cannot divide by zero ❌")
            else:
                result = n1 / n2
                label_result.config(text="Result: " + str(result))
        except:
            label_result.config(text="Invalid input ❌")           

            
    tk.Button(calc_win, text="Add", command=add).pack(pady=5) 
    tk.Button(calc_win, text="Subtract", command=sub).pack(pady=5) 
    tk.Button(calc_win, text="Multiply", command=mul).pack(pady=5) 
    tk.Button(calc_win, text="Divide", command=div).pack(pady=5) 

def game():
    game_win = tk.Toplevel()
    game_win.title("Guess Game")
    game_win.geometry("300x300")

    target = random.randint(1, 50)
    attempts = 5

    tk.Label(game_win, text="Guess number (1-50)").pack(pady=5)

    entry = tk.Entry(game_win)
    entry.pack(pady=5)

    result_label = tk.Label(game_win, text="")
    result_label.pack(pady=5)

    attempts_label = tk.Label(game_win, text="Attempts left: 5")
    attempts_label.pack(pady=5)

    def check():
        nonlocal attempts
        try:
            guess = int(entry.get())

            attempts -= 1
            attempts_label.config(text=f"Attempts left: {attempts}")

            if guess < target:
                result_label.config(text="Too Low")
            elif guess > target:
                result_label.config(text="Too High")
            else:
                result_label.config(text="Correct  🎉 ")

            if attempts == 0:
                result_label.config(text=f"Game Over ! Number was {target} ")

        except:
            result_label.config(text="Invalid input ❌")
    
    def reset():
        nonlocal target, attempts
        target = random.randint(1,50)
        attempts = 5
        entry.delete(0, tk.END)
        result_label.config(text="")
        attempts_label.config(text="Attempts left: 5")

    tk.Button(game_win, text="Guess", command=check).pack(pady=5) 
    tk.Button(game_win, text="Reset", command=reset).pack(pady=5) 


def todo():
    todo_win = tk.Toplevel()
    todo_win.title("To-Do List")
    todo_win.geometry("300x350")

    tk.Label(todo_win, text="Enter Task").pack(pady=5)

    entry_task = tk.Entry(todo_win, width=25)
    entry_task.pack(pady=5)

    listbox = tk.Listbox(todo_win, width=30)
    listbox.pack(pady=10)

    # Load existing tasks
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())

    except:
        pass

    def add_task():
        task = entry_task.get()
        if task != "":
            listbox.insert(tk.END, task)

            with open("tasks.txt", "a") as f:
                f.write(task + "\n")

            entry_task.delete(0, tk. END)

    def delete_task():
        selected = listbox.curselection()
        if selected:
            listbox.delete(selected)

            # Update file
            tasks = listbox.get(0, tk.END)
            with open("tasks.txt", "w") as f:
                for t in tasks:
                    f.write(t + "\n")

    tk.Button(todo_win, text="Add Task", command=add_task).pack(pady=5)
    tk.Button(todo_win, text="Delete Selected", command=delete_task).pack(pady=5)


def password():
    pass_win = tk.Toplevel()
    pass_win.title("Password Generator")
    pass_win.geometry("300x250")

    tk.Label(pass_win, text="Enter Password Length"). pack(pady=5)

    entry_len = tk.Entry(pass_win)
    entry_len.pack(pady=5)

    result_label = tk.Label(pass_win, text="")
    result_label.pack(pady=10)

    def generate():
        try:
            length = int(entry_len.get())

            chars = string.ascii_letters + string.digits
            password = ""

            for i in range(length):
                password += random.choice(chars)

            result_label.config(text="Password: " + password)

        except:
            result_label.config(text="Invalid input ❌")

    tk.Button(pass_win, text="Generate", command=generate).pack(pady=10)


root = tk.Tk()
root.title("Smart Asssistant")
root.geometry("300x400")

label = tk.Label(root, text="Smart Assistant", font=("Arial", 16))
label.pack(pady=10)

btn1 = tk.Button(root, text="Calculator", command=calculator)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Guess Game", command=game)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="To-Do List", command=todo)
btn3.pack(pady=5)

btn4 = tk.Button(root, text="Password Generator", command=password)
btn4.pack(pady=5)

root.mainloop()

