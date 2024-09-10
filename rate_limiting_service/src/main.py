#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify

from rate_limiting_service.src.rate_limiter import RateLimiter

app = Flask(__name__)
rate_limiter = RateLimiter()


@app.route('/api/resource', methods=['GET'])
def api_resource():
    user_id = request.headers.get('User-ID')
    if not user_id:
        return jsonify({"error": "User-ID header is required"}), 400

    if rate_limiter.is_allowed(user_id):
        return jsonify({"message": "Request allowed"}), 200
    else:
        return jsonify({"error": "Rate limit exceeded"}), 429


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
