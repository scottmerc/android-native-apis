## Invoke Espresso Test Via Headspin APIs

This short script can be incorporated into your dev ops pipeline to run native espresso test against Headspin devices or run locally. It essentially perfroms the following:

1. Locks the target device `https://{your-api-token}@api-dev.headspin.io/v0/adb/{device_id}/lock`
2. Has the ability to install your apk on the device `https://{your-api-token}@api-dev.headspin.io/v0/adb/{device-id}/install`
3. Start Capture `https://{your-api-token}@api-dev.headspin.io/v0/sessions`
4. Run Adb shell command to invoke test suite `https://{your-api-token}@api-dev.headspin.io/v0/adb/{device-id}/shell`
5. Stop Capture `https://{your-api-token}@api-dev.headspin.io/v0/sessions/{session-id}`
6. Unlock Device `https://{your-api-token}@api-dev.headspin.io/v0/adb/{device_id}/unlock`

### Run Test

```
HS_API_TOKEN={your-api-token} DEVICE_ID=71fef222 python main.py
```

### Install Dependencies

```
pip install requirements.py
```

