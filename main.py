import time
import os
import json

from apis.hs_apis import HS_API


def main():
    api_token = os.getenv("HS_API_TOKEN")
    api = HS_API(api_token)
    device_id = os.getenv("DEVICE_ID")
    #apk_path = ''
    adb_command = 'am instrument -w -r    -e package com.simplemobiletools.contacts.activities -e debug false com.simplemobiletools.contacts.debug.test/android.support.test.runner.AndroidJUnitRunner'


    api.lock_device(device_id) #api to lock the device
    #api.install_apk(device_id, apk_path) #install app on spevific device
    apk_id = api.get_apk_info()
    api.install_apk(device_id, apk_id)
    session_id = api.start_session(device_id) #api to start performance session
    api.start_test(device_id, adb_command) #api to invoke test
    api.stop_session(session_id) #api to stop perfromnace session
    api.unlock_device(device_id) #api to release the device


if __name__ == '__main__':
    main()