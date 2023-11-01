import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Hi, I'm Adithya! I'm learning Python Programming")
    content1 = """"
    Python developers design, code, and deploy development projects in the Python language. They also work on debugging 
    those same projects to ensure they function as intended. As a python developer, you'll work closely with other 
    teams, including data collection and analytics, to help answer questions and provide insight. Some of the projects
    you could work on span everything from application development to machine learning and AI. Becoming proficient in 
    Python and its uses opens the door to job possibilities in various industries. Ultimately, your role and 
    responsibilities will likely vary depending upon the industry and organization that you find yourself working 
    within."""
    st.info(content1)

content2 = """
Below you can find some of the apps I have built in python... Please feel free to check on them..
"""
st.write(content2)
