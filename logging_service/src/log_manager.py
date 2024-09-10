#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from src.log_handler import setup_file_handler, setup_console_handler


def setup_logging():
    """Set up logging configuration."""
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # or Config.LOG_LEVEL
    logger.addHandler(setup_file_handler())
    logger.addHandler(setup_console_handler())
    return logger
