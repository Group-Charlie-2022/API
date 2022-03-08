import covid_question_scraper
import fact_sheet_scraper

covid_question_scraper.run()
fact_sheet_scraper.run()

filenames = ['health_topics_chunked.jsonl', 'covid_answers.jsonl']

with open('combined_answers.jsonl', 'w') as outfile:
    count_of_written_files = 0
    for fname in filenames:
        with open(fname) as infile:
            if count_of_written_files!=0:
                outfile.write('\n')
            outfile.write(infile.read())
            count_of_written_files+=1