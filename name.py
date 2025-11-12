import streamlit as st

# Title and description
st.title("🎨 Welcome to My First Streamlit App!")
st.write("This app greets you and lets you pick your favorite color.")

# User input
name = st.text_input("Enter your name:")
color = st.selectbox("Choose your favorite color:", ["Red", "Green", "Blue", "Yellow"])

# Display output
if name:
    st.success(f"Hello, {name}! Your favorite color is {color}.")
    st.markdown(f"<h3 style='color:{color.lower()}'>Nice to meet you, {name}!</h3>", unsafe_allow_html=True)
