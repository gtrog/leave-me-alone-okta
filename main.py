import os.path
import time
from typing import Optional

import rumps
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

OKTA_SESSION_DURATION = 60 * 60
OKTA_REFRESH_URI = "https://renttherunway.okta.com/app/UserHome"
CHROME_DRIVER: Optional[Chrome] = None
REMOTE_DEBUG_PORT = 9014
FIRST_LOAD = True


def make_okta_happy(*_):
    global FIRST_LOAD

    if FIRST_LOAD:
        FIRST_LOAD = False
        return

    for attempt in range(2):
        try:
            CHROME_DRIVER.get(OKTA_REFRESH_URI)
            return
        except Exception as e:
            CHROME_DRIVER.quit()
            if attempt == 0:
                print(e)
                print("Lost Chrome browser, attempting to reconnect")
                setup_chrome_driver(reconnect=True)
            else:
                print(e)
                print("Giving up trying to reconnect to Chrome browser")
                rumps.quit_application()


class LmaoApp(object):
    def __init__(self):
        self.app = rumps.App(name="Leave Me Alone Okta", title="😭", menu=["Quit"], quit_button=None)
        self.timer = rumps.Timer(make_okta_happy, OKTA_SESSION_DURATION / 2)
        self.timer.start()

    def run(self):
        self.app.run()


def get_chrome_service() -> ChromeService:
    executable = ChromeDriverManager().install()
    return ChromeService(executable)


def launch_chrome():
    service = get_chrome_service()
    options = ChromeOptions()

    home_dir = os.path.expanduser("~")
    user_data_dir = f"{home_dir}/Library/Application Support/Google/Chrome/"
    options.add_argument(f"user-data-dir={user_data_dir}")
    options.add_argument(f"remote-debugging-port={REMOTE_DEBUG_PORT}")
    options.add_experimental_option("detach", True)

    driver = Chrome(service=service, options=options)

    # wait for user to pick a profile
    while not driver.current_window_handle:
        time.sleep(1)

    driver.get(OKTA_REFRESH_URI)


def setup_chrome_driver(reconnect: bool = False):
    global CHROME_DRIVER
    service = get_chrome_service()

    if not reconnect:
        launch_chrome()

    options = ChromeOptions()
    options.debugger_address = f"127.0.0.1:{REMOTE_DEBUG_PORT}"

    CHROME_DRIVER = Chrome(service=service, options=options)


@rumps.clicked("Quit")
def quit(*_):
    global CHROME_DRIVER
    if CHROME_DRIVER:
        CHROME_DRIVER.quit()
    rumps.quit_application()


if __name__ == "__main__":
    setup_chrome_driver()
    app = LmaoApp()
    app.run()
