import logging
import os

LOG_PATH = os.path.join(os.getcwd(), 'log')
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

class MyLogger:
    def __init__(self, name, level=logging.DEBUG):
        # Set the logger's name and level.
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger_level = level
        # Set the format of the log entries.
        self.formatter = logging.Formatter('[%(asctime)s]: %(message)s')
        
        # Add handlers for the console and file.
        self.__add_file_handler()
    
    # Add a handler to write to the file.
    def __add_file_handler(self):
        file_handler = logging.FileHandler(os.path.join(LOG_PATH, 'log.txt'), encoding='utf-8')
        file_handler.setLevel(self.logger_level)
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)
    
    # Return the logger.
    def get_logger(self):
        return self.logger
    
    # Log a message.
    def log(self, msg):
        self.logger.info(msg)