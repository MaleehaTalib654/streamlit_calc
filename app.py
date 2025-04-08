
import streamlit as st

st.set_page_config(page_title="Simple Calculator", layout="centered")

st.title("🧮 Simple Calculator")

# User inputs
num1 = st.number_input("Enter first number", format="%f")
num2 = st.number_input("Enter second number", format="%f")

# Operation
operation = st.selectbox("Choose operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Result
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("❌ Cannot divide by zero!")
            result = None
    if result is not None:
        st.success(f"✅ Result: {result}")
