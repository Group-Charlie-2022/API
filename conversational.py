from interface import Routine
import openai
import os

openai.api_key = os.getenv("OPENAI_KEY")

class Conversational(Routine):
    
    @staticmethod
    def process(inp, history):

        prompt = ''

        for q, a in history[-5:]:
            prompt += 'Friend: ' + q + '\n'
            prompt += 'Empathetic chatbot: ' + a + '\n'

        prompt += 'Friend: ' + inp + '\n'
        prompt += 'Empathetic chatbot:'

        response = openai.Completion.create(
                engine="text-davinci-001",
                prompt=prompt,
                temperature=0.5,
                max_tokens=60,
                top_p=1.0,
                frequency_penalty=0.5,
                presence_penalty=0.0,
                stop=["Friend"]
            )

        return response["choices"][0]["text"]

