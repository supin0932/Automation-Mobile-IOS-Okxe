

def get_desired_cap1():
    desired_cap = {
    "platformName": "iOS",
    "appium:platformVersion": "15.5",
    "appium:deviceName": "iPhone 12 Pro",
    "appium:automationName": "XCUITest",
    "appium:udid": "E3459DF1-0FC0-4158-B6AD-B9E586174C80"
    }
    return desired_cap


def get_desired_cap():
    desired_cap = {
        # Set your access credentials
        "browserstack.user": "lminhnht_Z0PVgW",
        "browserstack.key": "YBp4r6LvTMj95us59PuD",

        # Set URL of the application under test
        "app": "bs://c817d1d902b0d5e39b26b2dadc962dbc7d3d5018",

        # Specify device and os_version for testing
        "platformName": "android",
        "deviceName": "Google Pixel 3",
        "platformVersion": "9.0",

        # Set other BrowserStack capabilities
        "project": "First Python project",
        "build": "browserstack-build-1",
        "name": "first_test"
    }
    return desired_cap
