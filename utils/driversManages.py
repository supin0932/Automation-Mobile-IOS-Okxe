

def get_desired_cap1():
    desired_cap = {
        "platformName": "iOS",
        "appium:platformVersion": "15.3.1",
        "appium:deviceName": "ADMIN's iPhone",
        "appium:automationName": "XCUITest",
        "appium:udid": "5f295dc0a46757b7a212d6eacb3a2cc72a7655eb"
        }
    return desired_cap


def get_desired_cap():
    desired_cap = {
        # Set your access credentials
        "browserstack.user": "nhtl_YNC5cp",
        "browserstack.key": "ohyhW8iebF6Zsgr3dbiW",

        # Set URL of the application under test
        "app" : "bs://e3b4ba2306b465096da87ae0a09181dadc0e0a15",

        # Specify device and os_version for testing
        "platformName": "ios",
        "deviceName": "iPhone 12 Pro Max",
        "platformVersion": "14",

        # Set other BrowserStack capabilities
        "project": "First Python project",
        "build": "browserstack-build-1",
        "name": "first_test"
    }
    return desired_cap
