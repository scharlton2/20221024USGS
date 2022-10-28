
import logging

logging.basicConfig(
    format='%(levelname)s %(name)s %(asctime)s %(filename)s %(lineno)d %(message)s', # set the format for log entries
    datefmt="%x-%X",
    filename='../TEMP/formatted.log',
    level=logging.INFO,
    filemode="w"
)

logging.info("this is information")
logging.warning("this is a warning")
logging.info("this is information")
logging.critical("this is critical")
logging.error("this should be a 5-line file")
