# https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/')
r_text = r.text

# print(r.encoding)

soup = BeautifulSoup(r_text)


for story_heading in soup.find_all(class_="indicate-hover"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())



#class="indicate-hover css-11gjfuy"