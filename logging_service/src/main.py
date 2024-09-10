#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.log_manager import setup_logging


def main():
    """Main function to start the service."""
    logger = setup_logging()
    logger.info("Logging Service Started")

    # Simulate logging activity
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")


if __name__ == "__main__":
    main()
