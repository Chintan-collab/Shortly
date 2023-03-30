from common.request_object_class import requestFileInformation
from components import validator as vd
from components import chunk_master as cm
response_object = requestFileInformation()

class summarizer(response_object):
    if vd.validation_body(response_object):
        chunk_list = cm.chunk_creator(response_object.text)
    else:
        pass