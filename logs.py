#!/usr/bin/env python3

"""Script that explores the logging options"""

import os
import logging

"""LOG CONFIGURATION"""
#TODO: usar funcão
#TODO: usar lib (loguru)
#links the logging level to a system variable
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
#creating my own logger instance
log = logging.Logger("Jenny", log_level)
#stabilishing the handler
ch = logging.StreamHandler()
#setting the level as the debug level
ch.setLevel(log_level)
#formatting the log message
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d "
    "f:%(filename)s: %(message)s"
)
#adds the formatting configuration to the console handler
ch.setFormatter(fmt)
#tells that my log has a console handler
log.addHandler(ch)

"""
#logging message examples
log.debug("Message to the developer")
log.info("General message to users")
log.warning("A warning that do not causes errors")
log.error("Error that affects one execution only")
log.critical("Error that affects the entire excecution p. ex: missing database")
"""
print ("-----")

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("An error has occured: %s", str(e))
