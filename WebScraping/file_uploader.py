import openai
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="../secret/.env")

openai.api_key = os.getenv("OPENAI_KEY")
print(openai.File.create(file=open("combined_answers.jsonl"), purpose='answers'))


print(openai.File.list())