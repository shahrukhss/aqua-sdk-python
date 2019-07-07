import logging


class Logger():
    __instance = None

    def __init__(self, file_name="default_logger.log"):
        if Logger.__instance == None:

            logger = logging.getLogger(__name__)
            logger.setLevel(logging.INFO)
            # create file handler which logs even debug messages
            fh = logging.FileHandler(file_name)
            fh.setLevel(logging.DEBUG)

            # # create formatter and add it to the handlers
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            # formatter = logging.Formatter('%(asctime)-15s %(clientip)s %(user)-8s %(message)s')
            fh.setFormatter(formatter)

            # # add the handlers to the logger
            logger.addHandler(fh)
            logger = logger
            Logger.__instance = logger

    @staticmethod
    def getLoggerObj():
        if Logger.__instance == None:
            Logger()
        return Logger.__instance
