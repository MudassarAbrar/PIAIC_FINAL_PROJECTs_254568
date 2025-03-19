import streamlit as st

# Title
st.title("BMI Calculator")

# Inputs
weight = st.text_input("Enter your weight in kg", key="weight")
height = st.text_input("Enter your height in meters", key="height")

# BMI Calculation Function
def bmi_calculator(weight, height):
    try:
        weight = float(weight)
        height = float(height)
        if height <= 0:
            return "Height must be greater than 0."
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ValueError:
        return "Please enter valid numerical values for weight and height."

# Calculate BMI on Button Click
if st.button("Calculate BMI"):
    if weight and height:
        result = bmi_calculator(weight, height)
        if isinstance(result, float):
            st.success(f"Your BMI is: {result}")
            # Determine Category
            if result < 18.5:
                st.info("Category: Underweight")
            elif 18.5 <= result < 24.9:
                st.info("Category: Normal weight")
            elif 25 <= result < 29.9:
                st.info("Category: Overweight")
            else:
                st.info("Category: Obesity")
        else:
            st.error(result)
    else:
        st.error("Please fill in both weight and height.")
