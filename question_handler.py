from conversational import Conversational
from svm_comp import classify
from medical import Medical
from empathizer import empathize

def answer_question(q, history):
    category = classify(q)
    if category == 0:
        answer = Medical.process(q, history)
        return empathize(answer, quality_filter=0.1)
    elif category == 1:
        return Conversational.process(q, history)
    else:
        return "UNSAFE"