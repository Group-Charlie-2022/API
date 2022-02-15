from conversational import Conversational

def answer_question(q, history):
    return Conversational.process(q, history)
    #return f"You asked: \"{q}\"\nI do not know how to respond :("
