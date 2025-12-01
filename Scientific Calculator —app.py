import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮")

st.title("🧮 Scientific Calculator")
st.write("A full scientific calculator built using Streamlit.")

# Input number
expression = st.text_input("Enter expression", value="", 
                           placeholder="Example: sin(30) + sqrt(9) * 5")

# Allowed functions
allowed_funcs = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "sqrt": math.sqrt,
    "log": math.log10,
    "ln": math.log,
    "pi": math.pi,
    "e": math.e,
    "pow": math.pow,
    "factorial": math.factorial,
    "abs": abs
}

# Safe evaluation
def safe_eval(expr):
    try:
        # Replace deg → rad for trig functions
        expr = expr.replace("sin(", "math.sin(math.radians(")
        expr = expr.replace("cos(", "math.cos(math.radians(")
        expr = expr.replace("tan(", "math.tan(math.radians(")

        # Evaluate using allowed names only
        return eval(expr, {"__builtins__": None, "math": math}, allowed_funcs)
    except Exception as e:
        return f"Error: {str(e)}"

# Calculate button
if st.button("Calculate"):
    result = safe_eval(expression)
    st.success(f"Result: {result}")

# Example instructions
st.write("### Supported Functions")
st.write("""
- **sin(x), cos(x), tan(x)** → angle in degrees  
- **sqrt(x)** → square root  
- **log(x)** → log base 10  
- **ln(x)** → natural log  
- **pi, e** → constants  
- **pow(a, b)** → a^b  
- **factorial(x)**  
- You can combine expressions:  
  `sin(30) + sqrt(16) * 3`
""")
