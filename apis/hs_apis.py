import requests
import json
import traceback
import logging
import datetime
import pytest
import time
import calendar
import logging
from datetime import timedelta


class HS_API():

    #INTIALIZATION OF APIs WITH HS API TOKEN
    def __init__(self, api_token, device_address=None):
        self.api_token = api_token
        self.url_root = 'https://api-dev.headspin.io/v0/'
        self.headers = {}
        self.headers["Authorization"] = "Bearer {}".format(api_token)
        self.device_address= device_address


    def get_devices(self):
        request_url = self.url_root + 'adb/devices'
        response = requests.get(request_url, headers=self.headers)
        json_data = json.loads(response.text)
        if response.status_code == 200:
            return json_data
        else:
            logging.error("Could not get devices")

    def lock_device(self, device_id):
        request_url = self.url_root + 'adb/{}/lock'.format(device_id)
        response = requests.post(request_url, headers=self.headers)
        if response.status_code == 200:
            return 1
        else:
            logging.error("Device {device_id} could not be locked")
            return 0

    def unlock_device(self, device_id):
        request_url = self.url_root + 'adb/{}/unlock'.format(device_id)
        response = requests.post(request_url, headers=self.headers)
        if response.status_code == 200:
            return 1
        else:
            logging.error("Device {device_id} could not be unlocked")
            return 0

    def get_bridge(self, device_id):
        request_url = self.url_root + 'adb/{}/bridge'.format(device_id)
        with open('/Users/scottmercer/.android/adbkey.pub', 'rb') as f:
            data = f.read()
        response = requests.get(request_url, data=data, headers=self.headers)
        json_data = json.loads(response.text)
        if response.status_code == 200:
            return json_data["serial"]
        else:
            logging.error("Device {device_id} did not return adb bridge")
            return 0

            