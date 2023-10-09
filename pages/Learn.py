from PIL import Image
import streamlit as st

st.set_page_config(page_title = "Learn Area", layout="wide")

image_contact_form1 = Image.open("images/Phishing-1.jpg")
image_contact_form2 = Image.open("images/Phishing-2.jpg")

with st.container():
    st.title("Learning Portal")
    st.write("##")
    
    st.subheader("What is a phishing attack?")
    st.write("""Phishing refers to an attempt to steal sensitive information, typically in the form of usernames, passwords,
    credit card numbers, bank account information or other important data in order to utilize or sell the stolen information. By 
    masquerading as a reputable source with an enticing request, 
    an attacker lures in the victim in order to trick them, similarly to how a fisherman uses bait to catch a fish.""")
    
    st.image("images/learn-1.png")
    
    st.subheader("Statistics of the Phishing Attacks")
    
    st.write("""According to the IC3 FBI Crime Report, the phishing scams lost the $52 million approximately. 
    It says phishing attacks are the most common attack type in 2022. There were 300,497 
    victims found this year, as shown in the following figure.""")
    
    st.image("images/learn-2.png")
    
    st.write("""The detection of Phishing sites had a rapid increase according to the data of Statista, as 
    shown in the following figure. The third quarter of 2021 to the third quarter of 2022 
    saw an increase starting from 1.097 million to 1.270 million. It was approximately 345% of the 
    increase in the Covid-19 pandemic situation.""")
    
    st.image("images/learn-3.png")
    
    st.write("""The years 2020 to 2022 were pandemic situations. Most people work in the Work from home 
    based. Then the phishing scams increased in these two years of time other than in the earlier
    years. The phishing attackers mostly attack Online based websites to gain financial income. 
    Therefore, these attackers mostly try to attack financial websites. According to the Anti-Phishing Working Group (AWPG) published on Statista data in Q3 of 2022, financial institutions were the 
    most targeted online industry by phishing attacks, as shown in the following figure.""")
    
    st.image("images/learn-4.png")
    
    st.subheader("Types of Phishing Attacks")
    
    st.write("""There are many kinds of phishing attacks, such as Email Phishing, Spear phishing, Smishing, 
    Angler phishing, etc. Email Phishing is the most common method in phishing methods. It 
    targets a set of people once and sends the email to all of them. These emails have mistaken rather 
    than legitimate emails. The source email address of these emails is fake email addresses. The 
    attackers create an email address that is most similar to the original service email address. 
    Mostly, attackers misspell the email address and other content in these emails. Then, the attacker 
    forces to direct to the embedded web link in the email by saying “urgent work”, “important”, and 
    “attention please” like words. The following figure shows the format of the email 
    phishing attack.""")
    
    st.image("images/learn-5.png")
    
    st.write("""Spear Phishing is another kind of email phishing type. This attack type targets a single target 
    rather than a set of targets. The body of these emails is extremely similar to regular phishing 
    attacks, as shown in the following figure. But the quality of the email body, when 
    compared to the normal phishing attack, has an extreme difference. Spear phishing emails have 
    more quality than regular phishing attacks.""")
    
    st.image("images/learn-6.png")
    
    st.write("""Smishing, also known as SMS over phishing, is another kind of phishing attack type. The 
    attacker uses SMS to send malicious details in these attacks. The attacker acts as an HR manager, 
    CEO, or any other legitimate party. The body of these messages mostly contains hiring a job for 
    more salary, winning a grand prize in a competition, winning a lottery, etc. These messages are 
    also embedded with a website link by the attacker to achieve the user data. The more common 
    Smishing attack evidence is shown in the following figure.""")
    
    st.image("images/learn-7.png")
    
    st.write("""Angler phishing is another kind of Phishing technique. It uses social media to do the phishing 
    attack. Most people use social media such as Facebook, Twitter, and Instagram to share their 
    lifestyles, thoughts, and experience with others. When people get an experience with a highprofile 
    organization such as Pizzahut, Domino’s, Burger King, Coca-Cola, Microsoft, Google, or 
    any other organization, if the experienced service of these organizations is getting worst, then 
    people use Social media to tell the experience with their anger. The phishing attackers are also on 
    the social media platforms. They tend to create fake accounts on social media platforms 
    impersonating the legitimate organization. They tend to maintain these accounts as similar to the 
    original organizational social media accounts. Then they reply to these angry posts that the 
    people post on their social media timelines. They respond by requesting personal details such as 
    name, address, phone number, bank details, etc. Also, they can give a web link to report the 
    incident from this social media platform to get the credentials of the social media account. The 
    following figure shows an example of this attack.""")
    
    st.image("images/learn-8.png")

    st.write("""Most of these high-profile organizations verify their profiles on social media, but the people in 
    an angry situation in these situations forget to see the replier verified or not. The phishing 
    attacker exploits the human using his anger in these attacks.""")
    
    st.subheader("URLs and their properties")
    
    st.write("""According to the above attack types, most phishing attacks use web URLs. These URLs do not 
    behave like legitimate web URLs. A web URL has several components. They are scheme, 
    subdomain, domain, top-level domain (TLD), port number, path, query string separator, query 
    string (parameter), and fragment. Consider the following example URL.
    
    https://www.example.co.uk/blog/article/search?docid=720&hl=en#dayone""")
    
    st.image("images/learn-9.png")
    
    st.write("""Scheme:- Scheme is the protocol used to transmit and exchange data on the Web site. For 
    example, HTTP, HTTPS, FTP, etc.""")
    
    st.write("""Subdomain:- Subdomain used to segregate the different sections of the website. The subdomain 
    specifies what type of resources are delivered to the client. Mostly used “WWW-World Wide Web”.""")
    
    st.write("""Domain:- The Domain specifies the name of the organization that the URL belongs to.""")
    
    st.write("""Top-Level Domain (TLD):- Top-Level domain is the website registered organization. For 
    example, “.com” represents commercial businesses, and “.net” represents Network organizations.""")
    
    st.write("""Path:- The specific location of the web page, file, or any resource the client wants to access on
    this website.""")
    
    st.write("""Query String Separator:- This separator separates the Query string from the rest of the part of 
    the web URL. It tells the given Query is performed to the browser.""")
    
    st.write("""Query String:- The Query String specifies the parameters that are requested from the website 
    database by the requester. It consists of a parameter and a value. They joined using the ‘&’ sign. 
    The parameter can be a number, string, encrypted value, or any other form of data on the 
    database.""")
    
    st.write("""Fragment: Fragment represents an id or name attribute of an HTML element. This is optional 
    for a web URL.""")
    
    st.subheader("Detecting Phishing URLs")
    
    st.write("""Legitimate or Phishing, every URL has these properties. The Phishing attacker changes the 
    attributes of these URLs and generates a URL similar to a legitimate URL. The Phishing URLs 
    can identify using the parameters of these attributes such as URL length, IP address, Having ‘@’ 
    symbols, Domain registration length, Checking whether Whois registered or not, Protocol that is 
    used by the URL, Page rank, Google indexed or not, URL abnormality, etc. These parameters are 
    based on four main categories. They are,""")
    
    st.write("""1. Address Bar Based Features
2. Abnormal Based Features
3. HTML and JavaScript based Features
4. Domain based Features
""")
    
    st.subheader("Address Bar Based Features")
    st.write("1. URL Length")
    st.write("""Phishing attackers use long URLs to hide the suspicious part of the URL. For example,
http://federmacedoadv.com.br/3f/aze/ab51e2e319e51502f416dbe46b773a5e/?cmd=_home&amp;dispatch=11004d58f5b74f8dc1e7c2e8dd4105e811004d58f5b74f8dc1e7c2e8dd4105e8@phishing.website.html""")

    st.write("""It was estimated that if the URL length is less than fifty-four (54) characters, then it will be a
    legitimate URL. Otherwise, if the URL is between characters of 54 and 75, then it can be 
    categorized as a Suspicious URL. Otherwise, the URL is a Phishing URL.""")
    
    st.write("2. Using an IP Address as a Domain Name")
    
    st.write("""Some URLs’ domain name comes with an IP address instead of a Domain name. Then, these URLs can be categorized as Phishing URLs. """)
    
    st.write("""For example, “http://78.143.96.35/wordpress/gam/index.php?bidderblocklogin=”""")
    
    st.write("3. URLs using “TinyURLs”")
    
    st.write("""TinyURLs are the shortening service of URLs. This technique is called “HTTP Redirect” The domain of these URLs are short, and it links to a Long URL. For example, the URL 
    “http://portal.hud.ac.uk/” can be shortened to “bit.ly/19DXSk4” [28]. These TinyURLs can be phishing URLs because the user doesn’t know the exact Long URL.""")
    
    st.write("4. URL’s having “@” symbol")
    
    st.write("""The “@” can ignore the other parts of the URL and direct the URL to the following paths of the 
    “@” symbol. Then the Phishing attacker can link Phishing URL to a legitimate URL, setting the 
    “@” symbol in the legitimate URL. Therefore, URLs having the “@” symbol can be Phishing 
    URLs.""")
    
    st.write("5. Redirecting using")
    
    st.write("""URLs with “//” in the URL's path will redirect to another location. Therefore, URLs with “//” in their path can be phishing.""")
    
    st.write("""For example, http://www.legitimate.com//http://www.phishing.com """)
    
    st.write("6. Multi-level subdomains")
    
    st.write("""Consider the following example.""")
    st.write("https://www.example.co.uk:443/blog/")
    st.write("""In this URL, the top-level domain is “co.uk”. If this Top-level domain goes with a multi-level of 
    subdomains, then this URL can be Phishing URL. When we omit the country-code top-level 
    domain, then count the remaining dots in the Top-level domain. If the number of dots is greater 
    than two can be categorized as Phishing URL.""")
    
    st.write("7. The Domain is separated with a ‘-‘ sign")
    st.write("""In legitimate URLs, the ‘-‘ sign uses very rarely in the Domain. The Phishers use ‘-‘ signs to add 
    them to their Phishing URLs Domain name. It separates the Legitimate URL part from the 
    Phishing attacker's content, which can be added as a prefix or a suffix.""")
    
    st.write("For example http://www.Confirme-paypal.com/")
    
    st.write("8. Favicon")
    
    st.write("""Favicon is a graphical icon that is associated with the Web site. Many websites use this as a 
    trademark of their websites. If the favicon is loaded from a domain other than that shown in the 
    address bar, then the URL will likely be considered a Phishing URL.""")
    
    st.image("images/learn-10.png")
    
    st.write("9. Domain Registration Length")
    st.write("""The legitimate domains registered in several years of time. The Phishing attackers register their domain to do their task. Therefore, short-time registered domains can be Phishing attacks.""")
    
    st.write("10. Having HTTPS in the URL")
    
    st.write("""The HTTPS certificate tells the URL is secured, but this is not enough because the HTTPS cerificate issuer must be trusted, such as, 
    “GeoTrust”, “GoDaddy”, “Network Solutions”, 
    “Thawte”,” Comodo”, etc. Also, the age of the certificate must be greater than the years of 
    time considered as a Legitimate website.""")
    
    st.write("11. Using Non-standard port")
    
    st.write("""Sometimes phishers requested access to the other ports instead of our requested service. For example, if we are requesting web service 
    (Port 80 or 443) from the server, but the server wants to access SSH (Port 22) in our computer may be a Phishing attempt. Therefore, make sure the 
    other ports are closed on your computer.""")
    
    st.subheader("Abnormal Based Features")
    
    st.write("1. Request URL")
    
    st.write("""The legitimate web pages, the web page, and other embedded objects load within the web 
    domain, but the Phishers are used to redirect the embedded objects to the other domains. It is 
    estimated that if the external redirection of content is less than 22%, then it is considered as a 
    legitimate webpage. Otherwise, if the external redirection of content is between 22% and 
    61%, then it is considered a suspicious webpage. Otherwise, it can consider a Phishing 
    Website.""")
    
    st.write("2. URL of Anchor")
    
    st.write("""The anchor element is represented in the “<a>” tag. Using the anchor tags, web pages are used to 
    add hyperlinks. If fewer of these hyperlinks have a different domain, then these websites can be 
    categorized as legitimate websites. It was estimated that URLs of anchor percentage less than 
    31% in the different domains are legitimate [28]; otherwise, URLs of anchor percentage between 
    31% And ≤ 67% in the different domains can be classified as suspicious. Otherwise, the 
    website is considered as a Phishing website.""")
    
    st.write("""3. Links in <Meta>, <Script> and <Link> tags""")
    
    st.write("""The <meta> tags are used to offer metadata about the HTML document, <Script> tags are used to 
    create a client-side script, and <Link> tags are used to retrieve other web resources. In legitimate 
    websites, these tags are lined to the same domain. It was estimated that the percentage of Links 
    in " < Meta > "," < Script > " and " < Link>" are less than 17% in the other domains that can be 
    considered legitimate websites. Otherwise, the percentage of Links in " < Meta > "," < 
    Script > " and " < Link>" are between 17% and 81% in the other domains and can be considered 
    suspicious web pages. Otherwise can be considered Phishing web pages.""")
    
    st.write("4. Abnormal URL")
    
    st.write("""Abnormal URLs can identify in the WHOIS database (https://who.is/). If we can fetch data from 
    WHOIS that is based on the domain of our URL, then the URL can consider legitimate;
    otherwise, it can be a phishing URL.""")
    
    st.write("5. Server Form Handler (SFH)")
    
    st.write("""The server form handler can contain an empty string, or “about: blank” can consider as Phishing 
    URL. The domain name of the SFH can be different from the domain name of the webpage. 
    Then these web URLs can be suspicious. Otherwise, URLs can categorize as legitimate 
    URLs.""")
    
    st.write("""6. Summitting Information to Email""")
    
    st.write("""Most websites require the personal information of their users. They request it using the forms. 
    Then phishers can redirect this summited information to his mail using various techniques. PHP
    uses the mail() function to do this task on the server side. When it comes to the client side, it can 
    use mailto: function to function. If a website uses mail() or mailto: function to submit user 
    information can be categorized as a Phishing website; otherwise, it can be a legitimate 
    website""")
    
    st.subheader("HTML and JavaScript based Features")
    
    st.write("""1. Website Forwarding""")
    st.write("""Website Forwarding is how many times the Website has been Redirected. It was found that a 
    legitimate website will redirect a maximum of one time. Otherwise, a Phishing website is 
    redirected at least four times.""")
    
    st.write("2. Status Bar Customization")
    
    st.write("""Phishers use JavaScript to change the Status Bar to users. In JavaScript, the " onMouseOver " 
    event shows a fake URL in the address bar by the Phishers. Therefore, the “onMouseOver” event 
    changes the status bar, and that can be categorized as a Phishing website [28]. Otherwise, it is a 
    Legitimate URL.""")
    
    st.write("3. Disabling Right Click")
    
    st.write("""The attackers use JavaScript to disable the Right Click on the website. Therefore, users cannot 
    view and save the source code of the Website. If the Right Click is disabled on the website, then 
    it is a Phishing Website. Otherwise, it is a Legitimate website.""")
    
    st.write("4. IFrame Redirection")
    
    st.write("""IFrame is an HTML tag that shows a different page on the current page. The Phishers use IFrame 
    to show a Phishing page in a Legitimate page without the borders of the Phishing website. 
    Therefore, a website that uses IFrame can be categorized as a Phishing website. Otherwise, 
    it can be classified as a Legitimate page.""")
    
    st.write("5. Using a Pop-up window to ask for personal details")
    
    st.write("""Legitimate websites have never asked for personal details using a Pop-up window. A Pop-up 
    window uses to give greetings, warnings, or other information. Phishing websites use this feature 
    to ask for personal data, such as usernames and passwords, from the users. Therefore, if a 
    website asks for any personal information using a Pop-Up window can be categorized as 
    Phishing; otherwise, it is classified as legitimate.""")

    st.subheader("Domain Based Features")
    st.write("1. Age of the Domain")
    
    st.write("""The domain age can verify using the “WHOIS” (https://who.is/) database, as shown in the 
    flowing figure""")
    
    st.image("images/learn-11.png")
    
    st.write("""It was found that if the domain's age is less than six months, it can be categorized as a Phishing 
    website; otherwise, it is a legitimate website.""")
    
    st.write("2. Website Traffic")
    
    st.write("""Website traffic can measure using the number of visits to a web page and how many web pages 
    are used by the people. The Alexa database ranks the web pages based on their popularity. Then 
    it is found that a website rank is less than 100000 can be categorized as legitimate; otherwise,
    it is a Phishing website.""")
    
    st.write("3. DNS Record")
    
    st.write("""DNS records also be found using the “WHOIS” database. The Phishing websites' DNS records 
    cannot be found in the “WHOIS” database. Therefore, if a domain of a URL cannot be found,
    DNS records using the “WHOIS” database can be categorized as Phishing URLs; otherwise, it is 
    a legitimate URL.""")
    
    st.write("4. Page Rank")
    st.write("""Page rank is a value that gives to a website by the internet. It indicates how is important this web 
    page to the internet. The value provides a range of 0 to 1. Most of the Phishing websites don’t
    have a page rank. It was found that a page rank value is less than 0.2 can be categorized as 
    Phishing; otherwise, it is a legitimate website.""")
    
    st.write("5. Google Index")
    st.write("""This feature examines whether the URL-based website is google indexed or not. The google 
    indexed websites are shown in Google when it searches in google. When the considered URL 
    domain is searched on Google, and it shows results on Google can be categorized as a Legitimate 
    website; otherwise, it is a Phishing Website.""")
    
    st.write("6. Number of Links Pointing to the Website")
    
    st.write("""When we search for a domain in a web browser, it points to other external links that belong to 
    the searched domain. It was found that if there are several external links, less than two and 
    greater than 0 can be considered as suspicious URLs. Otherwise, if the URL has 0 external links 
    can be categorized as Phishing URL. Otherwise, it is a Legitimate URL.""")
    
    st.write("7. Statistical-Reports-Based Feature")
    
    st.write("""Phishtank and StopBadware are leading Phishing URL detectors, and they provide statistical 
    reports based on phishing URLs. Using these detectors, it can find the Top phishing 
    domains; if our URL is in these Top phishing domains, then it can be considered as a Phishing 
    URL; otherwise, it is a Legitimate URL.""")
    
    st.write("""Using these parameters, a user can tell the legitimacy of a URL manually. But it is not an easy 
    task. Therefore, people tend to use many computing techniques to check the legality of an URL.""")
    
    st.subheader("List-Based Phishing detection systems")
    
    st.write("""The list-based phishing detection mechanism is one of these techniques. This technique uses 
    whitelists and blacklists to identify the threat. The phishing attacks identifying day by day, then 
    these identified phishing attacks are moved to the Blacklist. Then these blacklists are used by the 
    organizations to set an alert and block these websites when their employees log into these 
    websites. The companies maintain a blacklist database of IPs to prevent the employees logs into 
    them. The phishing attacks increased daily, and then this technique failed to identify the zero-day attacks. The effectiveness of this mechanism becomes 20%. 
    After that, whitelist-based systems were introduced by the organizations. It includes all the 
    legitimate websites, and the users have access to only these whitelist-based websites. Any of the 
    other IP addresses were blocked by default. Same as the blacklist-based databases, it creates 
    the whitelist-based database. But these databases also had a problem because websites are 
    created every day. If it introduced a new legitimate website, then users can’t access it. Then 
    whitelist-based systems also failed, like the Blacklist-based systems.""")
    
    st.subheader("Phishing detection using Visual similarity")
    
    st.write("""This technique uses HTML tags, CSS, and image logos to find the similarity of the webpage with 
    the actual webpage. It matches for a certain level of similarity with the actual web page and then 
    determines the similarity of the web page. The accuracy of this method was 80%. The 
    organizations maintain a whitelisted database of websites and check the similarity using this 
    whitelisted website database. This method also failed because the newly created websites can’t 
    be identified by this method, and Phishers tend to create websites exactly the same as legitimate 
    websites. Therefore, new phishing attacks also can’t be detected by organizations.""")
    
    st.write("""Then the people had to think of different options than they attempted. After these attempts, 
    people moved to Artificial intelligence to identify phishing attacks. Using Artificial intelligence 
    (AI), people identified zero-day attacks.""")
    
    st.subheader("Phishing attack detection using Artificial intelligence")
    
    st.write("""Artificial intelligence is the machines that simulate human intelligent processes [29]. Artificial 
    Intelligence has mainly has two main categories. They are Machine Learning (ML) and Deep 
    learning (DL). Deep learning is also a part of machine learning. The architecture is shown in the 
    following figure.""")
    
    st.image("images/learn-12.png")
    
    st.write("""The core of Artificial Intelligence is Machine Learning. Machine Learning is imitating human 
    intelligence to computer machines to do a certain amount of complex tasks. The difference
    between machine learning and the automated program is that machine learning can analyze and 
    think and, after that, do the task, but automated programs can't think and do the given task. 
    Machine learning can be categorized into three main categories they are Supervised Learning, 
    Unsupervised Learning, and Reinforcement learning. Supervised Machine learning is used to 
    handle Labeled data, and data has the supervision to handle them. Then the Unsupervised 
    data is used to handle Unlabeled data. In Reinforcement learning, the machines identify 
    their errors and learn through the mistakes. Deep learning techniques use many layers to 
    predict their outcomes. These layers are called neurons. Machine learning and Deep learning 
    both the techniques use algorithms to train the available data. After training the data, the trained 
    AI model is used to predict the decisions. The important thing is to choose the AI algorithm 
    based on the problem. AI algorithms can be classified as Classification algorithms, Regression 
    algorithms, and Clustering algorithms. Since the Phishing URL detection problem is a 
    Classification problem, classification algorithms are used to solve this problem, such as Decision 
    trees, Support vector machines, Random Forest, etc. The entire research is based on identifying 
    phishing attacks using various Artificial intelligence-based techniques.""")
    
    st.subheader("Phishing Prevension Techniques")
    
    st.image("images/learn-13.png")
    

    