import logging
import sys
from logging.handlers import TimedRotatingFileHandler

import sentry_sdk
from sentry_sdk.integrations.logging import EventHandler


class NaaSLogger:
    logger = None
    default_level = logging.DEBUG  # Handlers should have greater or equal level
    name = "NaaS"
    log_format = "%(asctime)s (%(levelname)-8s) (%(module)s.%(funcName)s.%(lineno)d) %(message)s"
    log_file = None

    stream_handler = {
        "name": f"{name}.streamHandler",
        "level": logging.DEBUG,
        "stream": sys.stdout,
    }
    file_handler = {
        "name": f"{name}.fileHandler",
        "level": logging.DEBUG,
        "duration": "W6",  # Rollover on Sunday(6) of every week(W)
    }

    def __init__(self, name=name, log_format=log_format, log_file=log_file):
        self.name = name
        self.log_format = log_format
        self.log_file = log_file

    def get_format(self):
        return logging.Formatter(fmt=self.log_format)

    def get_sentry_handler(self):
        handler = EventHandler(level=logging.ERROR)
        handler.set_name(f"{self.name}.sentryHandler")
        return handler

    def get_console_handler(self):
        console_handler = logging.StreamHandler(self.stream_handler.get("stream"))
        console_handler.set_name(self.stream_handler.get("name"))
        console_handler.setLevel(self.stream_handler.get("level"))
        console_handler.setFormatter(self.get_format())
        return console_handler

    def get_file_handler(self):
        file_handler = TimedRotatingFileHandler(self.log_file, when=self.file_handler.get("duration"))
        file_handler.set_name(self.file_handler.get("name"))
        file_handler.setLevel(self.file_handler.get("level"))
        file_handler.setFormatter(self.get_format())
        return file_handler

    def get_logger(self):
        if self.logger is None:
            self.logger = logging.getLogger(self.name)
            self.logger.setLevel(self.default_level)
            self.logger.propagate = False

            self.logger.addHandler(self.get_console_handler())
            if self.log_file is not None:
                self.logger.addHandler(self.get_file_handler())

            if sentry_sdk.Hub.current.client is not None:
                self.logger.addHandler(self.get_sentry_handler())

        return self.logger


logger = NaaSLogger().get_logger()
