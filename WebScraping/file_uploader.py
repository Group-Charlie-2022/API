import openai

openai.api_key = "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"

#print(openai.File.create(file=open("combined_answers.jsonl"), purpose='answers'))

#openai.File.delete("file-mw9jCXDFWjhxmFKSddgAG5AC")





print(openai.File.list())