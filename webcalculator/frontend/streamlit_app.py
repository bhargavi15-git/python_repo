#py -3.11 -m pip install streamlit
from webcalculator.backend.calculator_functions import CalCulator
import streamlit as st

st.title("🧮 Calculator App",help='This calculator helps to calculate two numbers and perform addition, subtraction, multiplication and division.')

calc = CalCulator()

number1 = st.number_input("Enter first number", value=0,help="Enter an integer")
number2 = st.number_input("Enter second number", value=0,help="Enter an integer")
result=0
operation = st.selectbox("Choose Operation to be performed", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        result = calc.sum_function(number1, number2)
    elif operation == "Subtract":
        result = calc.diff_function(number1, number2)
    elif operation == "Multiply":
        result = calc.multiply_function(number1, number2)
    elif operation == "Divide":
        result = calc.divide_function(number1, number2)

st.write(f'The Result is {result}')


