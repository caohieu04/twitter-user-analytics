import logging, sys, os
logger = None

def get_logger():
    global logger
    if logger is None:
        try:
            os.makedirs("./tmp")
        except:
            pass
        handler = logging.FileHandler(
            filename="./tmp/log",
            mode="w"
        )
        handler.setLevel(logging.INFO)
        handler.setFormatter(
            logging.Formatter(
                '[%(asctime)s] [%(process)d] [%(levelname)s] [%(module)s] %(message)s', 
                '%Y-%m-%d %H:%M:%S %z'))
        logger = logging.Logger('log')
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
    return logger
