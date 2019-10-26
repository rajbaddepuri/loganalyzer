import logging

class Logger(object):

    __instnace = None
    @staticmethod
    def get_logger(loglevel=logging.INFO):
        if Logger.__instnace == None:
            Logger(loglevel) #doub
        return Logger.__instnace

    def __init__(self, loglevel=logging.INFO):
        if Logger.__instnace != None:
            raise Exception("This logger is a singleton Instance, user get_logger() static method instead")
        else:
            Logger.__instnace = self
        self.logger = logging.getLogger("loganalyzer.log") #objec created
        self.logger.setLevel(loglevel) #level set

        #create console handler
        _ch = logging.StreamHandler()
        _ch.setLevel(loglevel)

        #formatter
        _formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        _ch.setFormatter(_formatter)

        #set handler
        self.logger.addHandler(_ch)

    def info(self, message, *args, **kwargs):
        self.logger.info(message, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warn(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)