import sys
import logging

def get_error_message(error,error_message_detail:sys):
    _,_,exc_traceback = error_message_detail.exc_info()
    error_file_name = exc_traceback.tb_frame.f_code.co_filename
    custom_error = "Error occured in python script -> [{0}], at line -> [{1}], error message -> [{2}].".format(
                    error_file_name,
                    exc_traceback.tb_lineno,
                    str(error)
                )

    return custom_error
    
class CustomExceptionClass(Exception):
    def __init__(self,error_message,error_message_detail:sys):
        super().__init__(error_message)
        self.error_message = get_error_message(error_message,error_message_detail = error_message_detail)

    def __str__(self):
        return self.error_message

