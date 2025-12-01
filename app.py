import streamlit as st

st.set_page_config(page_title="Simple Calculator", page_icon="🧮")

st.title("🧮 Simple Calculator")
st.write("A basic calculator that works on Streamlit Cloud.")

# Inputs
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0)

with col2:
    num2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox(
    "Choose an operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

# Calculation logic
def calculate(a, b, op):
    if op == "Add":
        return a + b
    elif op == "Subtract":
        return a - b
    elif op == "Multiply":
        return a * b
    elif op == "Divide":
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

# Button & result
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f"Result: {result}")
