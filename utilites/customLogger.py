import logging

class LogGen:
    @staticmethod
    def loggen():
        file = logging.FileHandler(".\\Logs\\logfile.log")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s :%(message)s')
        file.setFormatter(formatter)
        logger=logging.getLogger()
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger




