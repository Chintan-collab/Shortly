from src.exception import CustomExceptionClass
from src.logger import logging
from utils import get_data_from_url


def validation_body(response_object):
    try:
        if response_object.type=='URL':
            text_data = get_data_from_url(response_object.url)
            if len(text_data) < 500:
                response_object.error = 'Less than 500 characters'
                return False
            else:
                response_object.text = text_data
                return True
            

        elif response_object.type=='DOC':
            pass
        else:
            pass

    except:
        pass