import logging.config
import logging.handlers
from sys import platform as _platform


def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance()


@singleton
class Logger():
    def __init__(self):
        if _platform != "darwin":
            config_file_path = "./hansya-daas.tar.gz/com/hansya/log/logging.conf"
        else:
            config_file_path = "/Users/arunprasathshankar/Desktop/hansya-daas/" \
                               "com/hansya/log/logging.conf"
        logging.config.fileConfig(config_file_path)
        self.logger = logging.getLogger('hansya-daas.log')
        # create console handler with a higher log level
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # set a format which is simpler for console use
        # See: https://docs.python.org/2/library/logging.html#logging.Formatter for more info
        formatter = logging.Formatter('%(name)s: %(levelname)s: %(asctime)2s: %(funcName)s: %(message)s',
                                      '%Y-%m-%d %H:%M:%S')
        # tell the handler to use this format
        console.setFormatter(formatter)
        # add the handler to the root logger
        self.logger.addHandler(console)
