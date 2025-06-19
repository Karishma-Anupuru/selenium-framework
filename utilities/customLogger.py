import logging
import os


class LogGen:
    @staticmethod
    def loggen():

        if not os.path.exists(".\\Logs"):
            os.makedirs(".\\Logs")

        logger = logging.getLogger("AutomationLogger")
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            file_handler = logging.FileHandler(".\\Logs\\Automation.log")
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger
        # logging.basicConfig(filename=".\\Logs\\Automation1.log",
        #                     format= '%(asctime)s: %(levelname)s: %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p')
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        # return logger

