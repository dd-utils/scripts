#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import configparser
import requests
import random
import datetime

CONFIG_NAME = "setting.conf"
SECTION_NAME = "conf"
URL_NAME = "weixin_url"
NORMAL_DESC_NAME = "normal_desc"
UP_DESC_NAME = "up_desc"
UP_WEEKDAY_NAME = "up_weekday"

conf = configparser.ConfigParser()
conf.read(os.path.join(os.getcwd(), CONFIG_NAME), encoding='utf-8')
desc = conf.get(SECTION_NAME, NORMAL_DESC_NAME)
if datetime.datetime.now().weekday() == conf.getint(SECTION_NAME, UP_WEEKDAY_NAME):
    desc = conf.get(SECTION_NAME, UP_DESC_NAME)

headers = {"Content-Type": "application/json"}
data = {
    "msgtype": "text",
    "text": {
        "content": desc,
        # "mentioned_list":["@all"],
    }
}

url = conf.get(SECTION_NAME, URL_NAME)

try:
    r = requests.post(
        url=url,
        headers=headers,
        json=data)
except Exception as err:
    print ("Err: ", err)