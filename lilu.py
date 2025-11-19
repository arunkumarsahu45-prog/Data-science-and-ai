import streamlit as st

# App Title
st.title("Doctor Consultation App")

# Doctor Info
st.header("Doctor Details")
st.write("👨‍⚕️ Doctor Name: **Dr. Sumit**")
st.write("📞 Mobile Number: +91-7847867019")  # Replace with actual number

# Patient Section
st.header("Patient Consultation")
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=120)
problem = st.text_area("Describe your health issue")

# Call Button (link to phone dialer)
if st.button("Call Doctor"):
    st.markdown(
        f"[📞 Click here to call Dr. Sumit](tel:+917847867019)"
    )

# Submit Consultation Request
if st.button("Submit Request"):
    st.success(f"Thank you {name}, your request has been sent to Dr. Sumit.")
