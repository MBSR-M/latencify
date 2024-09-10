#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, request, jsonify
import logging

from cache_management_service.src.cache_manager import CacheManager

app = Flask(__name__)
cache_manager = CacheManager()

# Set up logging
logger = logging.getLogger('cache_management_service')
logger.setLevel(logging.DEBUG)


@app.route('/cache/set', methods=['POST'])
def set_cache():
    data = request.json
    key = data.get('key')
    value = data.get('value')

    if not key or value is None:
        logger.error("Key and value are required")
        return jsonify({"error": "Key and value are required"}), 400

    cache_manager.set(key, value)
    logger.info(f"Cached value for key: {key}")
    return jsonify({"message": "Value cached successfully"}), 200


@app.route('/cache/get', methods=['GET'])
def get_cache():
    key = request.args.get('key')

    if not key:
        logger.error("Key is required")
        return jsonify({"error": "Key is required"}), 400

    value = cache_manager.get(key)
    if value is None:
        logger.warning(f"Key not found: {key}")
        return jsonify({"error": "Key not found"}), 404

    logger.info(f"Retrieved value for key: {key}")
    return jsonify({"key": key, "value": value}), 200


@app.route('/cache/delete', methods=['DELETE'])
def delete_cache():
    key = request.args.get('key')

    if not key:
        logger.error("Key is required")
        return jsonify({"error": "Key is required"}), 400

    cache_manager.delete(key)
    logger.info(f"Deleted key: {key}")
    return jsonify({"message": "Key deleted successfully"}), 200


@app.route('/cache/flush', methods=['POST'])
def flush_cache():
    cache_manager.flush_all()
    logger.info("Cache cleared successfully")
    return jsonify({"message": "Cache cleared successfully"}), 200


@app.route('/cache/info', methods=['GET'])
def cache_info():
    info = cache_manager.cache_info()
    logger.info("Retrieved cache info")
    return jsonify(info), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
