import streamlit as st
import random
import string

st.title("🤖 Smart Assistant")

menu = st.sidebar.selectbox(
    "Choose Feature",
    ["Calculator", "Guess Game", "To-Do List", "Password Generator"]
)

# ---------------- CALCULATOR ----------------
if menu == "Calculator":
    st.subheader("Calculator")

    a = st.number_input("Enter first number")
    b = st.number_input("Enter second number")
    op = st.selectbox("Operation", ["+", "-", "*", "/"])

    if st.button("Calculate"):
        if op == "+":
            st.success(a + b)
        elif op == "-":
            st.success(a - b)
        elif op == "*":
            st.success(a * b)
        elif op == "/":
            st.success(a / b if b != 0 else "Cannot divide by zero")

# ---------------- GUESS GAME ----------------
elif menu == "Guess Game":
    st.subheader("Guess Game")

    num = random.randint(1, 10)
    guess = st.number_input("Guess number (1-10)", 1, 10)

    if st.button("Check"):
        if guess == num:
            st.success("Correct 🎉")
        else:
            st.error(f"Wrong ❌ number was {num}")

# ---------------- TODO ----------------
elif menu == "To-Do List":
    st.subheader("To-Do List")

    task = st.text_input("Enter task")

    if st.button("Add Task"):
        with open("tasks.txt", "a") as f:
            f.write(task + "\n")
        st.success("Task added ✔️")

    if st.button("Show Tasks"):
        try:
            with open("tasks.txt", "r") as f:
                st.text(f.read())
        except:
            st.error("No tasks found")

# ---------------- PASSWORD ----------------
elif menu == "Password Generator":
    st.subheader("Password Generator")

    length = st.number_input("Length", 4, 20)

    if st.button("Generate"):
        chars = string.ascii_letters + string.digits
        password = "".join(random.choice(chars) for _ in range(int(length)))
        st.success(password)