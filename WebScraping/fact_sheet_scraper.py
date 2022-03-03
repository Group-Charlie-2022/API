from bs4 import BeautifulSoup
import requests
import json

CHUNK_SIZE = 3000

def run():
    source_link = 'https://www.who.int/health-topics/'
    source_link_base = 'https://www.who.int'

    source = requests.get(source_link).text
    soup = BeautifulSoup(source, 'lxml')

    table = soup.find('div', id='listView-healthtopics')

    count_of_written_lines = 0

    outfile=open('health_topics_chunked.jsonl', 'w')

    for topic_box in table.find_all('a', class_='link-container table'):
        topic_link = topic_box['href']
        topic_source = requests.get(topic_link).text
        topic_soup = BeautifulSoup(topic_source, 'lxml')

        fact_sheet = topic_soup.find('div', class_='sf-accordion__content')

        for subtopic in fact_sheet.find_all('a', href=True, title=True):
            subtopic_link = subtopic['href']
            print("Investigating subtopic at " + subtopic_link)
            subtopic_source = requests.get(subtopic_link).text
            subtopic_soup = BeautifulSoup(subtopic_source, 'lxml')
            article = subtopic_soup.find('article', class_='sf-detail-body-wrapper')
            if not article:
                continue
            headers = subtopic_soup.find_all('h2')
            for header in headers:
                paragraphs = []
                #iterating over the paragraphs under a header
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
                    #if it is not the first line, write a newline before it
                    if count_of_written_lines != 0:
                        outfile.write('\n')
                    json.dump({"text":chunk}, outfile)
                    count_of_written_lines+=1


    outfile.close()
    print("Written "+ str(count_of_written_lines) + " lines to health_topic_chunked.jsonl")

