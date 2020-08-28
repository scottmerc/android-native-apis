import time
import os
import json

from apis.hs_apis import HS_API


def main():
    api_token = os.getenv("HS_API_TOKEN")
    api = HS_API(api_token)

    #devices = api.get_devices()
    os.system("adb disconnect")
    api.unlock_device("31543137414b3098")



if __name__ == '__main__':
    main()