import pandas as pd
import streamlit as st
df = pd.read_csv("https://docs.google.com/spreadsheets/d/12-hdqmjPtVBrzYfiD-W3WivGLLQnnBwqpyh0Z9uMOhs/export?format=csv&gid=0",
                 index_col="Student Number")
st.title('Student Report')
df[df.index == st.text_input("Enter your student number: ")].T

