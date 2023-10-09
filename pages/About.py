import streamlit as st

st.set_page_config(page_title = "About Page", layout="wide")



st.title("About")
with st.container():
    st.write("##")
    image_column, text_column = st.columns((2,3))
    
    with image_column:
        st.image("images/myimg.png")
        
    with text_column:
        st.write("##")
        st.write("##")
        st.write(
        """
        
        
        
        Phishing attacks are a type of cyberattack where malicious actors impersonate trustworthy entities or create deceptive websites or emails to trick individuals into 
        revealing sensitive information, such as login credentials, personal identification numbers (PINs), credit card numbers, or other confidential data. This Machine Learning based System helps you to identify the Phishing URLs 
        and Legitimate URLs to detect and prevent in any kind of URL-based Phishing attempts.
        
        """
        )

#st.background-image("images/shutterstock_593626601.jpg")

st.markdown(
        """
        <style>
        body {
            background-image: url("shutterstock_593626601.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
