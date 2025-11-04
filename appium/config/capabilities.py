from appium.options.android import UiAutomator2Options

def get_appium_options():
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.automation_name = 'uiautomator2'
    options.udid = 'emulator-5554' 
    options.device_name = 'sdk_gphone64_x86_64'
    options.app_package = 'com.simplemobiletools.notes.pro'
    options.app_activity = 'com.simplemobiletools.notes.pro.activities.MainActivity'
    options.no_reset = True
    return options
