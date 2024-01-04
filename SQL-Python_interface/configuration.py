import logging


config = {
  'user': '',
  'password': '',
  'host': '',
  'database': '',
  'raise_on_warnings': True
}

DB_NAME = ''

def logger_function(file_name:str) -> logging.Logger:
    """
    Function for estabilish a logger with all it's informations
    Param file_name: name of the txt file where all the information will be exported
    Return: Logger with the file_name.txt
    """
    try:
        if (not isinstance(file_name, str)):
            raise TypeError("Variable is not of str type.")
        
        # Set up logger
        logger = logging.getLogger(file_name)
        logger.setLevel(logging.INFO)
        #formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # Log to console
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Also log to a file
        file_handler = logging.FileHandler(file_name)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return  logger
        
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise