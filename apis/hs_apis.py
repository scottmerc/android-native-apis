import requests
import json
import traceback
import logging
import datetime
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

    def start_test(self, device_id, adb_command):
        request_url = self.url_root + 'adb/{}/shell'.format(device_id)
        response = requests.post(request_url, headers=self.headers, data=adb_command)
        if response.status_code == 200:
            return "Success"
        else:
            return "Fail"

 #START A PERFORMANCE SESSION PROGRAMATICALLY
    def start_session(self, device_address):
        request_url = self.url_root + "sessions"
        payload = {}
        payload["session_type"] = "capture"
        payload["device_address"] = device_address
        payload["allow_replace"] = True
        payload["capture_video"] = True
        payload["capture_network"] = True
        payload = json.dumps(payload)
        print("Starting Capture....\n")
        response = requests.post(request_url, headers=self.headers, data = payload)
        # print(response.text.encode('utf8'))
        json_data = json.loads(response.text)
        if response.status_code == 200:
            return json_data["session_id"]
        else:
            print("Error starting capture....\n")
            pytest.raises(Exception)

    #STOP A PERFORMANCE SESSION PROGRAMATICALLY
    def stop_session(self, session_id):
        request_url = self.url_root + "sessions/{}".format(session_id)
        payload = "{\"active\": false}"
        response = requests.patch(request_url, headers=self.headers, data = payload)
        # print(response.text.encode('utf8'))
        json_data = json.loads(response.text)
        if response.status_code == 200:
            print("Stopped session capture.... {}\n".format(json_data["msg"]))
        else:
            print("Error stopping capture....\n")


    # def install_apk(self, device_address, path_to_apk):
    #     request_url = self.url_root + "adb/{}/install".format(device_address)
    #     with open(path_to_apk, 'rb') as f:
    #         data = f.read()
    #     response = requests.post(request_url, headers=self.headers, data=data)
    #     print response.text
    
    def install_apk(self, device_address, apk_id):
        request_url = self.url_root + "adb/{}/install".format(device_address)
        params = {'apk_id': apk_id}
        response = requests.post(request_url, headers=self.headers, params=params)
        print response.text


    def get_apk_info(self):
        request_url = self.url_root + "apps/apk/latest"
        response = requests.post(request_url, headers=self.headers)
        json_data = json.loads(response.text)
        if response.status_code == 200:
            return json_data["apk_id"]
            print(son_data["apk_id"])
        else:
            logging.error("Failed to upload apk")
