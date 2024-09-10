#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import redis

from cache_management_service.src.config import Config


class CacheManager:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host=Config.REDIS_HOST,
                                              port=Config.REDIS_PORT, decode_responses=True)

    def set(self, key, value):
        """Set a value in the cache with an expiration time."""
        self.redis_client.setex(key, Config.CACHE_EXPIRATION, value)

    def get(self, key):
        """Get a value from the cache."""
        return self.redis_client.get(key)

    def delete(self, key):
        """Delete a value from the cache."""
        self.redis_client.delete(key)

    def flush_all(self):
        """Clear all cache entries."""
        self.redis_client.flushdb()

    def cache_info(self):
        """Retrieve cache statistics."""
        return {
            "cache_size": self.redis_client.dbsize(),
            "max_size": Config.CACHE_MAX_SIZE
        }
