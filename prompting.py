def build_prompt(inp, history):
    prompt = ''

    for q, a in history[-5:]:
        prompt += 'Friend: ' + q + '\n'
        prompt += 'Empathetic chatbot: ' + a + '\n'

    prompt += 'Friend: ' + inp + '\n'
    prompt += 'Empathetic chatbot:'
    return prompt
