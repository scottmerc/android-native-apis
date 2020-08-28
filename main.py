import time
import os
import json

from apis.hs_apis import HS_API



def main():
    api_token = os.getenv("HS_API_TOKEN")
    api = HS_API(api_token)

    #devices = api.get_devices()
    api.lock_device("cd3aed29")
    serial = api.get_bridge("cd3aed29")
    print(serial)
    command = "adb connect {}".format(serial)
    os.system(command)
    time.sleep(3)
    # os.system("adb disconnect")
    # api.unlock_device("CQ3001SM53")



if __name__ == '__main__':
    main()