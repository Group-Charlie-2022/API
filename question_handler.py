from conversational import Conversational
from svm_comp import classify
from medical import Medical
from empathizer import empathize

def answer_question(q, history):
    if classify(q) == 0:
        answer = Medical.process(q, history)
        return answer
        # return empathize(answer)
    else:
        return Conversational.process(q, history)