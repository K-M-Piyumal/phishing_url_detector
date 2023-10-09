import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title = "Contact Page", layout="wide")

        
st.header("Contact Us via mail 📭")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_v7gj8hb1.json")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
        
local_css("style.css")

with st.container():    
    contact_from = """
    <form action="https://formsubmit.co/kumanayakamp8@gmail.com" method="POST">
        <input type="hidden" name=_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Just Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_from, unsafe_allow_html=True)

    with right_column:
        st_lottie(lottie_coding, height=300, key="")
        

        
    
