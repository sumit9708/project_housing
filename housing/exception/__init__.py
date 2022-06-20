import os
import sys

class HousingException(Exception):
    
    def __init__(self,error_message:Exception,error_detail:sys):
        
        super().__init__(error_message) ## super() is nothing but parent class initializer

        self.error_message = HousingException.get_detailed_error_message(error_message=error_message,error_detail=error_detail)

    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        

        """
        error message = Exception Object
        error_details = Object of sys module
        """

        _,_ ,exec_tb = error_detail.exc_info()
            
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"Error occured in script : [{file_name}] at line number : [{line_number}] error message is:[{error_message}]"



        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self)->str:
        return HousingException.__name__.str()



