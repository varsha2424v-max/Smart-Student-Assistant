import streamlit as st

st.title("🏦 Simple ATM Simulator")

# Session state (balance save रखने के लिए)
if "balance" not in st.session_state:
    st.session_state.balance = 5000

pin = st.text_input("Enter PIN", type="password")

if pin == "1234":
    st.success("Login Successful!")

    option = st.selectbox("Choose Option", ["Check Balance", "Deposit", "Withdraw"])

    if option == "Check Balance":
        st.write("💰 Balance:", st.session_state.balance)

    elif option == "Deposit":
        amount = st.number_input("Enter amount", min_value=0)
        if st.button("Deposit"):
            st.session_state.balance += amount
            st.success(f"Deposited {amount}")

    elif option == "Withdraw":
        amount = st.number_input("Enter amount", min_value=0)
        if st.button("Withdraw"):
            if amount <= st.session_state.balance:
                st.session_state.balance -= amount
                st.success(f"Withdrawn {amount}")
            else:
                st.error("Insufficient Balance")
else:
    st.warning("Enter correct PIN")