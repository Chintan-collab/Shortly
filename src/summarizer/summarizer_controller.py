from src.common.request_object_class import requestFileInformation
from src.components import validator as vd
from src.components import chunk_master as cm
from src.components.model_predictor import predictor
from src.logger import logging

response_object = requestFileInformation('https://www.scribbr.com/statistics/simple-linear-regression/')

def summarizer(response_object):
    print("Enter Validation!")
    if vd.validation_body(response_object):
        chunk_list = cm.chunk_creator(response_object.text)
        result = predictor(chunk_list, 50, 30)
        summary = ' '.join([summary["summary_text"] for summary in result])
        requestFileInformation.summarized_text = summary
        logging.info("Resultant Summary -> %s",summary)
    else:
        pass

summarizer(response_object)