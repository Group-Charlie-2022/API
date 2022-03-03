from conversational import Conversational
from svm_comp import classify
from medical import Medical

def answer_question(q, history):
    if classify(q) == 0:
        return Medical.process(q, history)
    else:
        return Conversational.process(q, history)
    #return f"You asked: \"{q}\"\nI do not know how to respond :("
