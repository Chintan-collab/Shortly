from src.exception import CustomExceptionClass
from src.logger import logging
from src.utils import get_data_from_url


def validation_body(response_object):
    print(response_object.type)
    """try:
        if response_object.type=='URL':
            print(response_object.type)
            text_data = get_data_from_url(response_object.url)
            print(text_data)
            if len(text_data) < 500:
                response_object.error = 'Less than 500 characters'
                return False
            else:
                logging.info(text_data)
                response_object.text = text_data
                return True
            

        elif response_object.type=='DOC':
            pass
        else:
            pass

    except:
        pass"""
    if response_object.type=='URL':
        print(response_object.type)
        text_data = get_data_from_url(response_object.url)
        print(text_data)
        if len(text_data) < 500:
            response_object.error = 'Less than 500 characters'
            return False
        else:
            logging.info(text_data)
            response_object.text = text_data
            return True