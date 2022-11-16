"""
This is the code for the frontend of the program. It is a web app built using streamlit
"""
from calorie import Calorie
from temperature import Temperature
import streamlit as st


st.title("BMR Calculator")
st.image("kcal.png")

message = """
Hi there! Welcome to this free BMR calculator. BMR is the number of calories your body burns when it is at rest. 
BMR can be dependent on temperature, the colder the temperature in your area, the more calories you will burn. 
In order to accurately calculate your BMR, please provide your accurate physical dimensions and the city and country
where you are located. Then, sit back, relax, and leave the calculations to us. 
"""
st.info(message)

age = st.text_input("How old are you? ")
height = st.number_input("What is your height in cm? ")
weight = st.number_input("What is your weight in kg? ")
country = st.text_input("What country are you in? ")
city = st.text_input("What city are you in? ")

if city:

    # Scrape the temperatures
    location_temp = Temperature(country,city)
    location_temp = location_temp.get()

    # Calculate the calories
    cals = Calorie(weight=weight,height=height,age=float(age),temperature=location_temp)
    output_cals = str(cals.calculate())
    st.write(f"Your BMR is {output_cals} calories")