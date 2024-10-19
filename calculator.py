import streamlit as st
import math

# Function definitions for calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def log(x, base=10):
    return math.log(x, base)

def ln(x):
    return math.log(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x < 0:
        return "Error: Negative number"
    return math.factorial(x)

# Streamlit app
st.title("Scientific Calculator")

st.sidebar.header("Choose Operation")
operation = st.sidebar.selectbox(
    "Select an operation:",
    ["Add", "Subtract", "Multiply", "Divide", "Power", "Square Root", 
     "Logarithm (base 10)", "Natural Logarithm (ln)", "Sine", 
     "Cosine", "Tangent", "Factorial"]
)

# Input fields for operations that require two numbers
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)
    
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        elif operation == "Power":
            result = power(num1, num2)
        st.success(f"Result: {result}")

# Input field for operations that require only one number
elif operation in ["Square Root", "Logarithm (base 10)", "Natural Logarithm (ln)", 
                   "Sine", "Cosine", "Tangent", "Factorial"]:
    num = st.number_input("Enter number", value=0.0 if operation != "Factorial" else 0)
    
    if st.button("Calculate"):
        if operation == "Square Root":
            result = sqrt(num)
        elif operation == "Logarithm (base 10)":
            result = log(num)
        elif operation == "Natural Logarithm (ln)":
            result = ln(num)
        elif operation == "Sine":
            result = sin(num)
        elif operation == "Cosine":
            result = cos(num)
        elif operation == "Tangent":
            result = tan(num)
        elif operation == "Factorial":
            result = factorial(int(num))
        st.success(f"Result: {result}")

st.sidebar.write("Powered by Streamlit")
