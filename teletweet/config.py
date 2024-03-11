#!/usr/local/bin/python3
# coding: utf-8

# TeleTweet - config.py
# 10/22/20 16:20
#

__author__ = "Benny <benny.think@gmail.com>"

import os

BOT_TOKEN = os.getenv("TOKEN", "5782497998:AAFdx2dX3yeiyDIcoJwPa_ghY2h_dozEh_E")
APP_ID = int(os.getenv("APP_ID", "17983098"))
APP_HASH = os.getenv("APP_HASH", "ee28199396e0925f1f44d945ac174f64")

CONSUMER_KEY = os.getenv("CONSUMER_KEY", "vI7bd1TjXv5jfzvKzOKAb90yo")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET", "r1pkkhWP8IRBewkbZO9nXcDoNfwIUm8773qZ42QNBUxtyvBNnS")

tweet_format = "https://twitter.com/{screen_name}/status/{id}"
