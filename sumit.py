import streamlit as st

# App title
st.title("Doctor SUMIT Consultation App 🩺")

# Sidebar for navigation
st.sidebar.title("Consultation Options")
option = st.sidebar.radio(
    "Choose how you want to consult:",
    ("Contact Doctor on Call", "Video Call", "Write Disease & Time")
)

# Option 1: Contact Doctor on Call
if option == "Contact Doctor on Call":
    st.header("📞 Contact Doctor on Call")
    st.write("Click the button below to initiate a call with the doctor.")
    if st.button("Call Doctor"):
        st.success("Calling the doctor... (simulation)")

# Option 2: Video Call
elif option == "Video Call":
    st.header("🎥 Video Call with Doctor")
    st.write("Click the button below to start a video consultation.")
    if st.button("Start Video Call"):
        st.success("Starting video call... (simulation)")

# Option 3: Write Disease & Time
elif option == "Write Disease & Time":
    st.header("📝 Write Your Disease & Preferred Time")
    
    disease = st.text_area("Describe your disease or symptoms:")
    time = st.time_input("Select preferred consultation time:")
    
    if st.button("Submit"):
        if disease.strip():
            st.success(f"Your request has been submitted!\n\nDisease: {disease}\nPreferred Time: {time}")
        else:
            st.error("Please enter your disease description before submitting.")
