import logging
import os

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.ERROR, )


def get_logging(file_name):
    dir_path = os.getcwd()
    logger = logging.getLogger(file_name)
    if not os.path.isdir(f"{dir_path}/logs"):
        os.mkdir(f"{dir_path}/logs")
    handler = logging.FileHandler(filename=f'{dir_path}/logs/{file_name}')
    logger.addHandler(handler)
    return logger
