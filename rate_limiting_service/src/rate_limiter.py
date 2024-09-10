#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import redis
from .config import Config


class RateLimiter:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)

    def is_allowed(self, user_id):
        key = f"rate_limit:{user_id}"
        current_count = self.redis_client.get(key)
        if current_count and int(current_count) >= Config.RATE_LIMIT:
            return False
        pipe = self.redis_client.pipeline()
        pipe.incr(key)
        pipe.expire(key, Config.TIME_WINDOW)
        pipe.execute()
        return True
