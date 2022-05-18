import logging


def new_line(log_method_function):
    def add_new_line(message):
        log_method_function(message=message + ' <br>')

    return add_new_line


class Logger:
    logger = logging.getLogger("Logger")
    logging.basicConfig(level=logging.INFO, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d-%m-%y %H:%M:%S')

    @staticmethod
    @new_line
    def info(message):
        Logger.logger.info(msg=message)

    @staticmethod
    @new_line
    def step(message):
        Logger.logger.info(msg=message)

    @staticmethod
    @new_line
    def debug(message):
        Logger.logger.debug(msg=message)

    @staticmethod
    @new_line
    def warning(message):
        Logger.logger.warning(msg=message)

    @staticmethod
    @new_line
    def error(message):
        Logger.logger.error(msg=message)

    @staticmethod
    @new_line
    def fatal(message):
        Logger.logger.fatal(msg=message)
