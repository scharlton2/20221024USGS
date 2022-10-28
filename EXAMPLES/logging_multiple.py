import sys
import logging
import logging.handlers
from getpass import getpass
from apple import apple
from banana import banana

# logging.basicConfig(level=logging.DEBUG, format="huh??")

LOG_FILENAME = '../TEMP/multiple.log'

# set up formatting for all handlers (but could be different for each)
formatter = logging.Formatter(
    '%(levelname)-9s %(name)s %(asctime)s %(message)s',
    '%x %X',
)  # create formatter for all logs


# log to STDOUT for DEBUG and higher
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

# log to a file for all levels INFO and higher
file_handler = logging.FileHandler(LOG_FILENAME)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)


# log to email for CRITICAL
smtp_password = "Gr3@tStud3nt"

email_handler = logging.handlers.SMTPHandler(
    ('smtp2go.com', 2525),
    f'{__name__}@pythonclass.com',
    ['jstrickler@gmail.com'],
    'ThisApplication Log Entry',
    ('pythonclass', smtp_password),
)
email_handler.setLevel(logging.CRITICAL)

log = logging.getLogger()  # create root Logger object
# testlogger.propagate = False # don't use default logger

log.addHandler(stream_handler)
log.addHandler(file_handler)
# testlogger.addHandler(email_handler)

# list handlers=
print("HANDLERS:")
for handler in log.handlers:
    print(handler)
print()

log.setLevel(logging.DEBUG)  # optional

log.debug("alpha")
log.info("beta")
log.warning("gamma")
log.error("delta")
log.critical("epsilon")
log.warning('zeta')
log.warning('eta')
log.critical("theta")
log.debug("iota")
log.error("kappa")
log.warning("lambda")
log.warning("mu")
log.warning("nu")
log.critical("rho")
apple()
banana()