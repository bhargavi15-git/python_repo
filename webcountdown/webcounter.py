#py -3.11 -m pip install streamlit
import time as t
import streamlit as st



st.markdown(
    "<h1 style='text-align: center;'>Countdown!</h1>",
    unsafe_allow_html=True
)

number1 = st.number_input("Enter the countdown seconds", value=0,help="Enter number of seconds to count down")
number2=number1
result=0

if st.button("Start countdown"):

    placeholder = st.empty()  # creates an empty container that can be updated

    for i in range(number1, -1, -1):


        placeholder.markdown(
            f"""
            <h1 style='font-size:120px; text-align:center; color:#000000;'>
                {i}
            </h1>
            """,
            unsafe_allow_html=True
        )
        t.sleep(1)






