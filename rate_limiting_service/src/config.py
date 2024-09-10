#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class Config:
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
    RATE_LIMIT = int(os.getenv('RATE_LIMIT', 100))  # Requests per time window
    TIME_WINDOW = int(os.getenv('TIME_WINDOW', 60))  # Time window in seconds
