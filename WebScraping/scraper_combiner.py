import covid_question_scraper
import fact_sheet_scraper

covid_question_scraper.run()
fact_sheet_scraper.run()

filenames = ['health_topics_chunked.jsonl', 'covid_answers.jsonl']

with open('combined_answers.jsonl', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())