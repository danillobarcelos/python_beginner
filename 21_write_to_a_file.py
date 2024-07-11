#from exercise 17
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/')
r_text = r.text
soup = BeautifulSoup(r_text, 'html.parser')

with open('21_write_to_a_file.txt', 'w', encoding='utf-8') as open_file:
    for story_heading in soup.find_all(class_="indicate-hover"): 
        if story_heading.a: 
            open_file.write(story_heading.a.text.replace("\n", " ").strip() + "\n")
        else: 
            open_file.write(story_heading.contents[0].strip() + "\n")

