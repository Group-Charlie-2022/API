from bs4 import BeautifulSoup
import requests
import csv
import json

source_link = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub'
source_link_base = 'https://www.who.int'

source = requests.get(source_link).text
soup = BeautifulSoup(source, 'lxml')

table = soup.find('div', id='PageContent_C002_Col01')

count = 0

outfile=open('answers.jsonl', 'w')

for topic_box in table.find_all('a', class_='sf-list-vertical__item'):
    count += 1
    topic_link_suffix = topic_box['href']
    topic_link = source_link_base + topic_link_suffix
    topic_source = requests.get(topic_link).text
    topic_soup = BeautifulSoup(topic_source, 'lxml')

    for accordion in topic_soup.find_all('div', class_='sf-accordion__panel'):
        question = accordion.find("span", itemprop="name").text
        answer = accordion.find("div", itemprop="text").text
        text = "Question: " + question.strip() + " Answer: "+ answer.strip()
        formed_text = {"text": text}
        json.dump(formed_text, outfile)
        outfile.write('\n')

outfile.close()
print(count)


