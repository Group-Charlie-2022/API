from interface import Route
import openai

openai.api_key = open("secret/openai_key").read().strip()

class Conversational(Route):
    
    def process(self, inp, history):
        response = openai.Completion.create(
                engine="text-davinci-001",
                prompt='Friend: ' + input +'\n'\
                        'Empathetic chatbot: ',
                temperature=0.5,
                max_tokens=60,
                top_p=1.0,
                frequency_penalty=0.5,
                presence_penalty=0.0,
                stop=["Friend"]
            )

        return response

