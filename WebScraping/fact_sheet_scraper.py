from bs4 import BeautifulSoup
import requests
import csv
import json
import re
CHUNK_SIZE = 3000
source_link = 'https://www.who.int/health-topics/'
source_link_base = 'https://www.who.int'

source = requests.get(source_link).text
soup = BeautifulSoup(source, 'lxml')

table = soup.find('div', id='listView-healthtopics')
#print(table.prettify())

count = 0

outfile=open('health_topics_chunked.jsonl', 'w')

for topic_box in table.find_all('a', class_='link-container table'):
    count += 1
    #print(topic_box.prettify())
    topic_link = topic_box['href']
    topic_source = requests.get(topic_link).text
    topic_soup = BeautifulSoup(topic_source, 'lxml')

    fact_sheet = topic_soup.find('div', class_='sf-accordion__content')

    for subtopic in fact_sheet.find_all('a', href=True, title=True):
        subtopic_link = subtopic['href']
        print(subtopic_link)
        subtopic_source = requests.get(subtopic_link).text
        subtopic_soup = BeautifulSoup(subtopic_source, 'lxml')
        article = subtopic_soup.find('article', class_='sf-detail-body-wrapper')
        if not article:
            continue
        # for paragraph in article.find_all('p'):
        #     formed_text = {"text": paragraph.text}
        #     json.dump(formed_text, outfile)
        #     outfile.write('\n')
        headers = subtopic_soup.find_all('h2')
        for header in headers:
            paragraphs = []
            for sibling in header.find_next_siblings():
                if sibling.name == "h2":
                    break
                else:
                    if sibling.name == 'p':
                        paragraphs.append(sibling.text)
            if not paragraphs:
                continue
            formed_text = " ".join(paragraphs)
            chunks = [formed_text[i:i + CHUNK_SIZE] for i in range(0, len(formed_text), CHUNK_SIZE)]
            for chunk in chunks:
                json.dump({"text":chunk}, outfile)
                outfile.write('\n')

outfile.close()
print(count)


