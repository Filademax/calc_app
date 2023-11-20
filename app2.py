import streamlit as st
from PIL import Image

st.title("calculator app")
img = Image.open("IMG_0866.jpg")
st.sidebar.image(img)

col1, col2, col3 =st.columns(3)
def add(a,b):
 c = a + b 
 return c

def sub(a,b):
    c = a - b
    return c

def mul(a,b):
    c = a * b 
    return c

x = st.number_input("input your first number")
y = st.number_input("input your second number")

with col1:
    if st.button("Add"):
        st.write(add(x,y))

with col2:
    if st.button("Substraction"):
        st.write(sub(x,y))

with col3:
    if st.button("Multiply"):
        st.write(mul(x,y))