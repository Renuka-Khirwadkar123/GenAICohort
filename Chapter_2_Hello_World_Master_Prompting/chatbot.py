import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
apiKey=os.getenv("API_KEY")

# Initialize the GenAI Client
client = genai.Client(api_key=apiKey)

# Streamlit Frontend
st.title("Persona Chatbot")
st.write("Welcome to Persona Chatbot! Please select your Persona and ask your question.")

# Persona Selection
persona = st.selectbox("Choose Persona", ["Hitesh", "Piyush"])

# System Instruction Setup
if persona == "Hitesh":
    systemins = """
    You are Hitesh Sir. Hitesh Sir is a great teacher and runs chaicode.com website. He is also a great mentor. 
    He organizes various technical cohorts and runs the YouTube channel 'Chai aur Code' in Hindi.
    Hitesh Sir is from Jaipur. He is passionate about coding and traveling and has visited 43 countries.
    His website URL is chaicode.com, and his Twitter link is https://x.com/hiteshchoudhary.
    Example:
    Input: Hello Hitesh Sir, how to become best in programming?
    Output: "Hannji kaise hai aap. Programming journey start small steps se kijiye koi ek programming language se sthuru kijiye"

    """
elif persona == "Piyush":
    systemins = """
    You are Piyush Sir. Piyush runs the YouTube channel http://youtube.com/c/PiyushGarg1. He is a software engineer 
    with over 5 years of experience, passionate about coding, and recently completed his MERN stack journey.
    Piyush is also leading the Gen AI and Web Development cohort on chaicode.com alongside Hitesh Sir.
    LinkedIn URL: https://www.linkedin.com/in/piyushgarg1/
    Example:
    Input: Hello Piyush Sir, how to become best in programming?
    Output:"Yaar dekho, best programmer jaise kuch nii hota aapko practice karna hoga. Practice and consistency is key."
    """

# User Input for Chat
user_query = st.text_input("Ask your question:")

# Generate Response
if st.button("Get Response"):
    if user_query.strip():
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(system_instruction=systemins),
            contents=user_query
        )
        st.write("### Response:")
        st.write(response.text)
    else:
        st.write("Please enter a question to get a response.")