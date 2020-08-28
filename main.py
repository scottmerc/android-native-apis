import time
import os
import json

from apis.hs_apis import HS_API



def main():
    api_token = os.getenv("HS_API_TOKEN")
    api = HS_API(api_token)

    device_id = os.geten("DEVICE_ID")

    #devices = api.get_devices()
    api.lock_device(device_id)
    serial = api.get_bridge(device_id)
    command = "adb connect {}".format(serial)
    os.system(command)
    time.sleep(3)
    # os.system("adb disconnect")
    # api.unlock_device("CQ3001SM53")



if __name__ == '__main__':
    main()