#!/usr/bin/env python3

"""Script that explores the logging options"""

import os
import logging
from logging import handlers

"""LOG CONFIGURATION"""
#TODO: usar funcão
#TODO: usar lib (loguru)
#links the logging level to a system variable
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
#creating my own logger instance
log = logging.Logger("Jenny", log_level)
#stabilishing the handler
#ch = logging.StreamHandler() #sends the log message to the console
fh = handlers.RotatingFileHandler(
    "meulog_logs.log",
    maxBytes=2**20, #the ideal is something around 2**20 or 1Mib
    backupCount=10, #teacher suggested 10 but is to be evaluated
)
#setting the level as the debug level
#ch.setLevel(log_level) #console handler
fh.setLevel(log_level) #file handler
#formatting the log message
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d "
    "f:%(filename)s: %(message)s"
)
#adds the formatting configuration to the console handler
#ch.setFormatter(fmt)
#adds the formatting configuration to the file handler
fh.setFormatter(fmt)
#tells that my log has a console handler
#log.addHandler(ch)
#tells that my log has a file handler
log.addHandler(fh)

"""
#logging message examples
log.debug("Message to the developer")
log.info("General message to users")
log.warning("A warning that do not causes errors")
log.error("Error that affects one execution only")
log.critical("Error that affects the entire excecution p. ex: missing database")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("An error has occured: %s", str(e))
