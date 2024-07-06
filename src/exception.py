import sys

def error_message_detail(error: Exception, sys_module: sys) -> str:
    """
    This function generates an error message with details.
    
    Args:
        error: The error message to be included in the generated message.
        sys_module: The sys.exc_info() object containing error details.
    
    Returns:
        str: The formatted error message.
    """
    _,_,exc_tb = sys_module.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f'Error in {file_name} at line {exc_tb.tb_lineno}: {str(error)}'
    return error_message

class CustomException(Exception):
    """
    Custom exception class to handle specific errors.

    This class provides a custom exception with detailed error messages.
    """

    def __init__(self, error: Exception, sys_module: sys = sys):
        super().__init__(error)
        self.error_message = error_message_detail(error, sys_module)
        self.original_error_message = error

        self.traceback = sys_module.exc_info()[2]

    def __str__(self) -> str:
        return self.error_message
