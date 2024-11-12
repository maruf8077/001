import streamlit as st

# Title of the app
st.title("Simple Calculator")

# User Input
st.header("Enter Your Numbers and Select Operation")

num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")

operation = st.selectbox(
    "Choose the operation",
    ("Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)")
)

# Perform Calculation
result = None
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (*)":
        result = num1 * num2
    elif operation == "Division (/)":
        if num2 == 0:
            st.error("Division by zero is not allowed!")
        else:
            result = num1 / num2

# Display Result
if result is not None:
    st.success(f"The result is: {result}")
