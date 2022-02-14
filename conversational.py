from interface import Routine
import openai
import os

openai.api_key = os.getenv("OPENAI_KEY")

class Conversational(Routine):
    
    @staticmethod
    def process(inp, history):
        response = openai.Completion.create(
                engine="text-davinci-001",
                prompt='Friend: ' + inp +'\n'\
                        'Empathetic chatbot: ',
                temperature=0.5,
                max_tokens=60,
                top_p=1.0,
                frequency_penalty=0.5,
                presence_penalty=0.0,
                stop=["Friend"]
            )

        return response

