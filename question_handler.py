from conversational import Conversational
from svm_comp import classify
from medical import Medical
from empathizer import empathize
import logging
import sys

stdout_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler(filename='logs/log')
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=[stdout_handler, file_handler]
)
log = logging.getLogger()


def answer_question(q, history):
    log.info('answering question: ' + q)
    answer = ''
    category = classify(q)
    if category == 0:
        log.info('classified as medical')
        answer = Medical.process(q, history)
        answer = empathize(answer, quality_filter=0.1)
    elif category == 1:
        log.info('classified as conversational')
        answer = Conversational.process(q, history)
    else:
        answer = "I'm sorry, I don't think I can help with that. Please contact a medical professional if you need help."
    log.info('answering: ' + answer)
    return answer
