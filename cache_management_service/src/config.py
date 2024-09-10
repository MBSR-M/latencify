#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


class Config:
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
    CACHE_EXPIRATION = int(os.getenv('CACHE_EXPIRATION', 3600))
    CACHE_MAX_SIZE = int(os.getenv('CACHE_MAX_SIZE', 1000))
