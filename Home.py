import streamlit as st
import requests
import pandas as pd
import numpy as np
import re
import sklearn
import nltk
nltk.download('stopwords')
import pickle
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from nltk.corpus import stopwords
from urllib.parse import urlparse
import socket
import idna
from tld import get_tld
import tldextract
from xgboost import XGBClassifier
import whois
import datetime





model = pickle.load(open('tr_pickel_xgb.pkl', 'rb'))


st.set_page_config(page_title = "Home Page", layout="wide")


st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                }
                
        </style>
        """, unsafe_allow_html=True)

image_contact_form1 = Image.open("images/phishlogo.png")

st.image(image_contact_form1, width=200)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_3rwasyjy.json")


with st.container():
    st.title("---Phishing Alert!!!---")
    st.title("Made by K.M.Piyumal - CS/2017/026")

    
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Let's Scan 🔍")
        
    
   # with right_column:
    #    st_lottie(lottie_coding, height=300, key="coding")
        
    




urlname_input = st.text_input("Input Your URL")
if urlname_input:
    urlname = urlname_input.lower()
else:
    urlname = "https://www.example.com"


#Length of URL

length = len(urlname)

#Host name Size

parsed_url = urlparse(urlname)
hostname = parsed_url.hostname
counthostname = len(hostname)


#Check the IP availability
def has_ip_address(urlname):
    parsed_url = urlparse(urlname)
    hostname_x = parsed_url.hostname
    try:
        ip_address = socket.gethostbyname(hostname_x)
        return True
    except socket.gaierror:
        return False


has_ip = has_ip_address(urlname)
    
if has_ip:
    ip_availability = 1
else:
    ip_availability = 0

#check the Number of dots

dot_count = 0
for char in urlname:
    if char == '.':
        dot_count += 1

#check the Number of hyphens count

hyphens_count = 0
for char2 in urlname:
    if char2 == '-':
        hyphens_count += 1
        
#check the Number of at count

at_count = 0
for char3 in urlname:
    if char3 == '@':
        at_count += 1
        
#check the Number of qm count

qm_count = 0
for char4 in urlname:
    if char4 == '?':
        qm_count += 1

#check the Number of and count        
and_count = 0
for char5 in urlname:
    if char5 == '&':
        and_count += 1

#check the Number of or count       
or_count = urlname.count('||')
        
#check the Number of eq count
eq_count = 0
for char7 in urlname:
    if char7 == '=':
        eq_count += 1


#check the Number of unders count
unders_count = 0
for char8 in urlname:
    if char8 == '_':
        unders_count += 1
        
#check the Number of unders count
tilde_count = 0
for char9 in urlname:
    if char9 == '~':
        tilde_count += 1
        
#check the Number of percentage mark count
percent_count = 0
for char10 in urlname:
    if char10 == '%':
        percent_count += 1
        
#check the Number of percentage mark count
percent_count = 0
for char11 in urlname:
    if char11 == '%':
        percent_count += 1
        
#check the Number of slash mark count
slash_count = 0
for char12 in urlname:
    if char12 == '/':
        slash_count += 1
        
#check the Number of star mark count
star_count = 0
for char13 in urlname:
    if char13 == '*':
        star_count += 1

#check the Number of colon mark count
colon_count = 0
for char14 in urlname:
    if char14 == ':':
        colon_count += 1 

#check the Number of comma mark count
comma_count = 0
for char15 in urlname:
    if char15 == ',':
        comma_count += 1 

#check the Number of semi colon mark count
semicolon_count = 0
for char16 in urlname:
    if char16 == ';':
        semicolon_count += 1  

#check the Number of doller mark count
doller_count = 0
for char17 in urlname:
    if char17 == '$':
        doller_count += 1   

#check the Number of spaces count
spaces_count = 0
for char18 in urlname:
    if char18 == ' ':
        spaces_count += 1  

#check the Number of www count
url_www_count = urlname.count('www') 

#check the Number of com count
url_com_count = urlname.count('com')  

#check the Number of double slash count
url_dslash_pr = urlname.count('//')
if url_dslash_pr > 1:
    url_dslash_prob = 1
else:
    url_dslash_prob = 0
        
#check the presence of HTTP
url_http = urlname.count('http')
if url_http >= 1:
    url_http_pr = 0
else:
    url_http_pr = 1        

#check the presence of HTTPS
url_https = urlname.count('https')
if url_https >= 1:
    url_https_pr = 0
else:
    url_https_pr = 1 
    
#ratio of digits in hostname
digit_count_hostname = 0

for char19 in hostname:
    if char19.isdigit():
        digit_count_hostname += 1


digits_ratio_host = digit_count_hostname/counthostname

#ratio of digits in urlname
digit_count_url = 0
for char20 in urlname:
    if char20.isdigit():
        digit_count_url += 1

digits_ratio_url = digit_count_url/length

#check the presence of punycodeurl
punyurl1 = urlname.count('http://xn--')
punyurl2 = urlname.count('http://xn--')
Totpuny = punyurl1+punyurl2

if Totpuny >= 1:
    punycodeurl = 1
else:
    punycodeurl = 0 
    
#check the port availability

port_availability = parsed_url.port

if port_availability:
    port_av = 1
else:
    port_av = 0 
    
#check the tld availability

tld_check = tldextract.extract(urlname).suffix
if tld_check:
    tld_checker = 1
else:
    tld_checker = 0
 
#check the tld in subdomain tld availability 
get_subdom = tldextract.extract(urlname)

subdomews = get_subdom.subdomain

if tldextract.extract(subdomews).subdomain:
    tld_checker_sub = 1
else:
    tld_checker_sub = 0

#Check the URL abnormality

def is_subdomain_abnormal(url):
    extracted = tldextract.extract(url)
    subdomain = extracted.subdomain.lower()
    
    #Define your own criteria for abnormal subdomains
    abnormal_indicators = ["test", "sandbox", "phishing", "malware"]
    
    for indicator in abnormal_indicators:
        if indicator in subdomain:
            return True
    
    return False
    
url_abnormility_text = is_subdomain_abnormal(urlname)
    
def is_domain_ip(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address == domain
    except socket.gaierror:
        return False
        
url_abnormility_ip = is_domain_ip(urlname)

TotAbnormality = url_abnormility_text or url_abnormility_ip

if TotAbnormality:
    Tot_ab_value = 1
else:
    Tot_ab_value = 0
        
#Check number of subdomains in the URL

def count_subdomains(url):
    extracted = tldextract.extract(url)
    subdomain = extracted.subdomain
    subdomain_parts = subdomain.split('.')
    
    # Exclude empty subdomain and www (if present)
    subdomain_parts = [part for part in subdomain_parts if part and part != 'www']
    
    return len(subdomain_parts)

subdomain_count = count_subdomains(urlname)

#Prefix and Suffix availability

def extract_prefix_suffix(domain):
    extracted = tldextract.extract(domain)
    if extracted.subdomain and extracted.suffix:
        return 1
    else:
        return 0

prefix_suffix_availabilityt = extract_prefix_suffix(urlname)

#Shortning services

def is_url_shortened(url):
    shortening_domains = [
        "bit.ly",
        "goo.gl",
        "tinyurl.com",
        "ow.ly",
        "t.co", 
        "is.gd",
        "buff.ly",
        "adf.ly",
        "shorte.st",
        "rebrand.ly",
        "youtu.be", 
        "qr.net",
        "adfoc.us",
        "cutt.ly",
        "v.gd"
        
        # Add more known shortening service domains as needed
    ]

    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()
    
    return domain in shortening_domains
    
is_shortened1 = is_url_shortened(urlname)

if is_shortened1:
    is_shortened1val = 1
else:
    is_shortened1val = 0



   
#Check the Whois registered or not
 
def is_registered(url):
    domain = url.split("//")[-1].split("/")[0]
    try:
        w = whois.whois(domain)
    except Exception:
        return False
    else:
        return bool(w.domain_name)
        
# def get_domain_name(url):
    # parsed_url = urlparse(url)
    # domain_name = parsed_url.netloc
    # return domain_name
        
#get_the_domain = get_domain_name(urlname)
is_reg_say = is_registered(urlname)
if is_reg_say:
    is_reg_say_y = 1
else:
    is_reg_say_y = 0
#Check the domain registration length

def get_domain_length(url):
    try:
        domain = url.split("//")[-1].split("/")[0]
        w = whois.whois(domain)
        if w.domain_name:
            return len(w.domain_name)
    except (whois.parser.PywhoisError, IndexError):
        pass
    
    return None

domain_length = get_domain_length(urlname)

if domain_length:
    domain_length_l = domain_length
else:
    domain_length_l = 0

#check domain age
def get_domain_age(url):
    try:
        domain = url.split("//")[-1].split("/")[0]
        w = whois.whois(domain)
        if w:
        
            creation_date = w.creation_date
            if isinstance(creation_date, list):
                creation_date = creation_date[0]
        
            if isinstance(creation_date, datetime.datetime):
                now = datetime.datetime.now()
                domain_age = now - creation_date
                return domain_age.days
    except (whois.parser.PywhoisError, IndexError):
        pass
    
    return None
   
domain_age = get_domain_age(urlname)
if domain_age:
    domain_age_y = domain_age
else:
    domain_age_y = -1
    
#No of Redirections

import requests

def count_redirects(urlname):
    try:
        response = requests.head(urlname, allow_redirects=True)
        redirects = len(response.history)
        return redirects
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0  # Return -1 to indicate an error



redirects = count_redirects(urlname)
if redirects >= 0:
    redirects_c = redirects
else:
    redirects_c = 0
    
#No of External Redirections

import requests
from urllib.parse import urlparse

def count_external_redirects(url):
    try:
        original_domain = urlparse(url).netloc
        redirects = 0

        while True:
            response = requests.head(url, allow_redirects=True)
            next_url = response.url

            # Break the loop if there are no more redirects
            if url == next_url:
                break

            next_domain = urlparse(next_url).netloc

            if original_domain != next_domain:
                redirects += 1

            url = next_url

        return redirects

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0  # Return -1 to indicate an error



redirects_xc = count_external_redirects(urlname)
if redirects >= 0:
    url_countxc = redirects_xc
else:
    url_countxc = 0
    

    

#No of words in the URL

#No of REPEATED letters in the URL

import re

def count_similar_sequences(url, pattern):
    # Use regular expression to find all occurrences of the pattern in the URL
    matches = re.findall(pattern, url)

    # Return the count of matches
    return len(matches)


pattern_to_count = r'(.)\1+'

# Count the occurrences of the pattern in the URL
count_of_char = count_similar_sequences(urlname, pattern_to_count)

#No of characters in the Shortest 

def find_shortest_word(url):
    # Split the URL by non-alphanumeric characters to extract words
    words = re.split(r'[^a-zA-Z0-9]+', url)

    # Remove empty strings from the list
    words = [word for word in words if word]

    if not words:
        return None, 0

    # Find the shortest word and its length
    shortest_word = min(words, key=len)
    shortest_word_length = len(shortest_word)

    return shortest_word, shortest_word_length



shortest_word, shortest_word_length = find_shortest_word(urlname)

#Shortest word length in the Host name
from urllib.parse import urlparse

def find_shortest_word_in_host(url):
    # Parse the URL to extract the host name
    parsed_url = urlparse(url)
    host = parsed_url.netloc

    # Split the host name by dots to extract words
    words = host.split('.')

    # Remove empty strings from the list
    words = [word for word in words if word]

    if not words:
        return None, 0

    # Find the shortest word and its length
    shortest_word = min(words, key=len)
    shortest_word_length = len(shortest_word)

    return shortest_word, shortest_word_length


shortest_word_host, shortest_word_length_host = find_shortest_word_in_host(urlname)

#Shortest word in the Path

from urllib.parse import urlparse

def shortest_word_length_in_url_path(url):
    # Parse the URL to extract the path
    parsed_url = urlparse(url)
    path = parsed_url.path

    # Split the path by slashes to extract words
    words = path.split('/')

    # Remove empty strings from the list
    words = [word for word in words if word]

    if not words:
        return 0  # No words found in the path

    # Find the shortest word length
    shortest_word_length = min(len(word) for word in words)

    return shortest_word_length



shortest_length_path = shortest_word_length_in_url_path(urlname)

#Longest word in the URL
import re

def longest_word_length_in_url(url):
    # Use regular expression to find all words in the URL
    words = re.findall(r'\b\w+\b', url)

    if not words:
        return 0  # No words found in the URL

    # Find the longest word length
    longest_word_length = max(len(word) for word in words)

    return longest_word_length



longest_length_IN_URL = longest_word_length_in_url(urlname)

#Longet word in the hostname

from urllib.parse import urlparse

def longest_word_length_in_hostname(url):
    # Parse the URL to extract the hostname
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    # Split the hostname by dots to extract words
    words = hostname.split('.')

    if not words:
        return 0  # No words found in the hostname

    # Find the longest word length
    longest_word_length = max(len(word) for word in words)

    return longest_word_length



longest_length_in_host = longest_word_length_in_hostname(urlname)


#Longest word in the Path

from urllib.parse import urlparse

def longest_word_length_in_url_path(url):
    # Parse the URL to extract the path
    parsed_url = urlparse(url)
    path = parsed_url.path

    # Split the path by slashes to extract words
    words = path.split('/')

    # Remove empty strings from the list
    words = [word for word in words if word]

    if not words:
        return 0  # No words found in the path

    # Find the longest word length
    longest_word_length = max(len(word) for word in words)

    return longest_word_length



longest_length_in_path = longest_word_length_in_url_path(urlname)

#No of hyperlinks in the url
import requests
from bs4 import BeautifulSoup

def count_hyperlinks_in_url(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the web page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all anchor tags (hyperlinks) in the HTML
            links = soup.find_all('a')

            # Count the number of hyperlinks
            num_links = len(links)

            return num_links
        else:
            return 0  # Request failed

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0  # Error occurred



num_hyperlinks = count_hyperlinks_in_url(urlname)

#Ratio internal hyperlinks

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def internal_hyperlink_ratio(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the web page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all anchor tags (hyperlinks) in the HTML
            links = soup.find_all('a')

            # Count the number of hyperlinks
            total_links = len(links)
            internal_links = 0

            # Extract the domain of the URL
            parsed_url = urlparse(url)
            base_domain = parsed_url.netloc

            # Count the number of internal hyperlinks
            for link in links:
                href = link.get('href')
                if href:
                    parsed_href = urlparse(href)
                    if parsed_href.netloc == base_domain:
                        internal_links += 1

            # Calculate the internal hyperlink ratio
            if total_links > 0:
                ratio = internal_links / total_links
                return ratio
            else:
                return 0  # No hyperlinks found

        else:
            return 0  # Request failed

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0  # Error occurred


ratio_internal_hyper = internal_hyperlink_ratio(urlname)

#Ratio external hyperlinks

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def external_hyperlink_ratio(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the web page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all anchor tags (hyperlinks) in the HTML
            links = soup.find_all('a')

            # Count the number of hyperlinks
            total_links = len(links)
            external_links = 0

            # Extract the domain of the URL
            parsed_url = urlparse(url)
            base_domain = parsed_url.netloc

            # Count the number of external hyperlinks
            for link in links:
                href = link.get('href')
                if href:
                    parsed_href = urlparse(href)
                    if parsed_href.netloc != base_domain:
                        external_links += 1

            # Calculate the external hyperlink ratio
            if total_links > 0:
                ratio = external_links / total_links
                return ratio
            else:
                return 0  # No hyperlinks found

        else:
            return 0  # Request failed

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0  # Error occurred



ratio_external_hyperlinks = external_hyperlink_ratio(urlname)

#Count of null hyperlinks

import requests
from bs4 import BeautifulSoup

def null_hyperlink_ratio(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the web page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all anchor tags (hyperlinks) in the HTML
            links = soup.find_all('a')

            # Count the number of hyperlinks
            total_links = len(links)
            null_links = 0

            # Count the number of null hyperlinks
            for link in links:
                href = link.get('href')
                if not href or href.strip() == '':
                    null_links += 1

            # Calculate the null hyperlink ratio
            if total_links > 0:
                ratio = null_links / total_links
                return ratio
            else:
                return 0  # No hyperlinks found

        else:
            return 0  # Request failed

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0  # Error occurred



ratio_null_hyperlinks = null_hyperlink_ratio(urlname)



#No of external css

import requests
from bs4 import BeautifulSoup

def count_external_css(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the web page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all <link> elements with rel="stylesheet" attribute
            css_links = soup.find_all('link', rel='stylesheet')

            # Count the number of external CSS links
            external_css_count = 0

            for css_link in css_links:
                href = css_link.get('href')
                if href and href.startswith('http'):
                    external_css_count += 1

            return external_css_count

        else:
            return 0  # Request failed

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0  # Error occurred


external_css_count = count_external_css(urlname)

#Ratio of internal redirections

import requests

def internal_redirection_ratio(url):
    try:
        # Send an HTTP GET request to the URL, allowing redirects
        response = requests.get(url, allow_redirects=True)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract all redirect URLs, including the original URL
            redirect_history = response.history + [response]

            # Count the number of internal redirects
            internal_redirects = 0
            base_url = response.url

            for redirect in redirect_history:
                if base_url in redirect.url:
                    internal_redirects += 1

            # Calculate the internal redirection ratio
            total_redirects = len(redirect_history)

            if total_redirects > 0:
                ratio = internal_redirects / total_redirects
                return ratio
            else:
                return 0  # No redirects or error

        else:
            return 0  # Request failed

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0  # Error occurred


ratio_internal_redirection = internal_redirection_ratio(urlname)


#External redirection ratio

import requests

def external_redirection_ratio(url):
    try:
        # Send an HTTP GET request to the URL, allowing redirects
        response = requests.get(url, allow_redirects=True)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract all redirect URLs, including the original URL
            redirect_history = response.history + [response]

            # Count the number of external redirects
            external_redirects = 0
            base_url = response.url

            for redirect in redirect_history:
                if base_url not in redirect.url:
                    external_redirects += 1

            # Calculate the external redirection ratio
            total_redirects = len(redirect_history)

            if total_redirects > 0:
                ratio = external_redirects / total_redirects
                return ratio
            else:
                return 0  # No redirects or error

        else:
            return 0  # Request failed

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0  # Error occurred


ratio_external_redirection = external_redirection_ratio(urlname)


#internal errors ratio

import requests

def internal_error_ratio(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return 0  # No internal errors

        # Check if the status code is in the 5xx range (internal server error)
        elif 500 <= response.status_code < 600:
            return 1  # Internal error occurred

        else:
            return 0  # Other status code (e.g., 404, 403, etc.)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0  # Error occurred during the request



internal_error_ratio_v = internal_error_ratio(urlname)

#external erroers ratio

import requests

def external_error_ratio(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return 0  # No external errors

        # Check if the status code is in the 4xx or 5xx range (client or server error)
        elif 400 <= response.status_code < 600:
            return 1  # External error occurred

        else:
            return 0  # Other status code

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0  # Error occurred during the request



error_ratio_external = external_error_ratio(urlname)

#login form availability

import requests
from bs4 import BeautifulSoup

def has_login_form(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the web page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Look for common login form elements (e.g., input fields for username and password)
            login_form = soup.find('form')

            if login_form:
                return True  # Login form found
            else:
                return False  # Login form not found

        else:
            return False  # Request failed

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False  # Error occurred during the request



has_login = has_login_form(urlname)

if has_login:
    has_login = 1
else:
    has_login = 0
    
    
#external favicon availability

import requests
from bs4 import BeautifulSoup

def has_external_favicon(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the web page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Look for the favicon link in the HTML
            favicon_link = soup.find('link', rel='icon')

            if favicon_link and 'http' in favicon_link.get('href', ''):
                return True  # External favicon found
            else:
                return False  # External favicon not found

        else:
            return False  # Request failed

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False  # Error occurred during the request



has_favicon = has_external_favicon(urlname)

if has_favicon:
    has_favicon = 1
else:
    has_favicon = 0

#links in tags

import requests
from bs4 import BeautifulSoup

def count_links_in_tags(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the web page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all anchor tags (<a>) in the HTML
            anchor_tags = soup.find_all('a')

            # Count the number of anchor tags
            num_links = len(anchor_tags)

            return num_links

        else:
            return 0  # Request failed

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0  # Error occurred during the request



num_links = count_links_in_tags(urlname)


#submit email availability

import requests
from bs4 import BeautifulSoup

def has_email_submission_form(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the web page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Look for common form elements (e.g., input fields for email)
            email_form = soup.find('form')

            if email_form:
                email_inputs = email_form.find_all('input', {'type': 'email'})
                if email_inputs:
                    return True  # Email submission form found
            return False  # Email submission form not found

        else:
            return False  # Request failed

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False  # Error occurred during the request



has_email_form = has_email_submission_form(urlname)

if has_email_form:
    has_email_form = 1
else:
    has_email_form = 0

#iframe availability

import requests
from bs4 import BeautifulSoup

def has_iframes(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the web page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all iframe tags (<iframe>) in the HTML
            iframe_elements = soup.find_all('iframe')

            if iframe_elements:
                return True  # Iframes found
            else:
                return False  # Iframes not found

        else:
            return False  # Request failed

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False  # Error occurred during the request



has_iframes_result = has_iframes(urlname)

if has_iframes_result:
    has_iframes_result = 1
else:
    has_iframes_result = 0


#pop-up-window availability

import requests
from bs4 import BeautifulSoup

def has_popup_windows(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the web page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Search for JavaScript code that opens pop-up windows
            # Note: This is a simplified example and may not cover all cases
            javascript_code = soup.find_all('script')

            for code in javascript_code:
                if "window.open" in code.text:
                    return True  # Pop-up windows found

            return False  # Pop-up windows not found

        else:
            return False  # Request failed

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False  # Error occurred during the request



has_popups = has_popup_windows(urlname)

if has_popups:
    has_popups = 1
else:
    has_popups = 0

#domain with copywrite

import requests
from bs4 import BeautifulSoup

def has_copyright_content(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the web page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Check if the copyright symbol (©) or the word "copyright" is in the page content
            page_content = soup.get_text().lower()  # Get the lowercase text content

            if "©" in page_content or "copyright" in page_content:
                return True  # Copyright content found

            return False  # Copyright content not found

        else:
            return False  # Request failed

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False  # Error occurred during the request



has_copyright = has_copyright_content(urlname)

if has_copyright:
    has_copyright = 1
else:
    has_copyright = 0

#path extensions

from urllib.parse import urlparse
import os

def has_path_extension(url, extensions):
    # Parse the URL using urlparse
    parsed_url = urlparse(url)

    # Get the path component of the URL
    path = parsed_url.path

    # Split the path to get the extension
    _, file_extension = os.path.splitext(path)

    # Check if the extracted extension is in the list of allowed extensions
    return file_extension.lower() in extensions

# Example URL and allowed extensions

allowed_extensions = {".pdf", ".html", ".php", ".txt", ".docx", ".doc", ".csv", ".xlsx", ".ppt", ".pptx", ".jpg", ".png", ".gif", ".bmp", ".js", ".mp3", ".wav", ".rar", ".gzip", ".zip", ".tar.gz", ".ttf", ".exe", ".app", ".otf"}

# Check if the URL has a valid path extension
path_ext = has_path_extension(urlname, allowed_extensions)

if path_ext:
    path_ext = 1
else:
    path_ext = 0





































    


x = [[length,
    counthostname,
    ip_availability,
    dot_count,
    hyphens_count,
    at_count,
    qm_count,
    and_count,
    or_count,
    eq_count,
    unders_count,
    tilde_count,
    percent_count,
    slash_count,
    star_count,
    colon_count,
    comma_count,
    semicolon_count,
    doller_count,
    spaces_count,
    url_www_count,
    url_com_count,
    url_dslash_prob,
    url_http_pr,
    url_https_pr,
    digits_ratio_url,
    digits_ratio_host,
    punycodeurl,
    port_av,
    tld_checker,
    tld_checker_sub,
    Tot_ab_value,
    subdomain_count,
    prefix_suffix_availabilityt,
    is_shortened1val,
    #path_ext,
    #redirects_c,
    #redirects_xc,
    #count_of_char,
    #shortest_word_length,
    #shortest_word_length_host,
    #shortest_length_path,
    longest_length_IN_URL,
    longest_length_in_host,
    #longest_length_in_path,
    #num_hyperlinks,
    #ratio_internal_hyper,
    #ratio_external_hyperlinks,
    #ratio_null_hyperlinks,
    #external_css_count,
    #ratio_internal_redirection,
    #internal_error_ratio_v,
    #error_ratio_external,
    #has_login,
    #has_favicon,
    #num_links,
    #has_email_form,
    #has_iframes_result,
    #has_popups,
    #has_copyright,
    is_reg_say_y,
    domain_length_l,
    domain_age_y]]



button2 = st.button('Attack ⚡')
if button2:
    result = model.predict(x)
    
    if result[[0]] == 0:
        textres = "Legitimate"
    else:
        textres = "Phishing"
        
    st.code(textres)
    #st.code(redirects_c)
    #st.code(redirects_xc)
    #st.code(extension)
    #st.code(count_of_char)
    #st.code(shortest_word_length)
    #st.code(shortest_word_length_host)
    #st.code(shortest_length_path)
    #st.code(longest_length_IN_URL)
    #st.code(longest_length_in_host)
    #st.code(longest_length_in_path)
    #st.code(num_hyperlinks)
    #st.code(ratio_internal_hyper)
    #st.code(ratio_external_hyperlinks)
    #st.code(ratio_null_hyperlinks)
    #st.code(external_css_count)
    #st.code(ratio_internal_redirection)
    #st.code(internal_error_ratio_v)
    #st.code(error_ratio_external)
    #st.code(has_login)
    #st.code(has_favicon)
    #st.code(num_links)
    #st.code(has_email_form)
    #st.code(has_iframes_result)
    #st.code(has_popups)
    #st.code(has_copyright)
    #st.code(path_ext)
    #st.code(is_reg_say_y)
    #st.code(domain_length_l)
    #st.code(domain_age_y)
    
    # st.code(length)
    # st.code(counthostname)
    # st.code(ip_availability)
    # st.code(dot_count)
    # st.code(hyphens_count)
    # st.code(at_count)
    # st.code(qm_count)
    # st.code(and_count)
    # st.code(or_count)
    # st.code(eq_count)
    # st.code(unders_count)
    # st.code(tilde_count)
    # st.code(percent_count)
    # st.code(slash_count)
    # st.code(star_count)
    # st.code(colon_count)
    # st.code(comma_count)
    # st.code(semicolon_count)
    # st.code(doller_count)
    # st.code(spaces_count)
    # st.code(url_www_count)
    # st.code(url_com_count)
    # st.code(url_dslash_prob)
    # st.code(url_http_pr)
    # st.code(url_https_pr)
    # st.code(digits_ratio_host)
    # st.code(digits_ratio_url)
    # st.code(punycodeurl)
    # st.code(port_av)
    # st.code(tld_checker)
    # st.code(tld_checker_sub)
    # st.code(Tot_ab_value)
    # st.code(subdomain_count)
    # st.code(prefix_suffix_availabilityt)
    # st.code(is_shortened1val)
    # st.code(longest_word_len)
    # st.code(longest_word_host_len)
    