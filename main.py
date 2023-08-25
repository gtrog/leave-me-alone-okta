import os.path
from typing import Optional

import rumps
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

OKTA_SESSION_DURATION = 60 * 60
OKTA_REFRESH_URI = "https://renttherunway.okta.com/app/UserHome"
CHROME_DRIVER: Optional[Chrome] = None
FIRST_LOAD = True


def make_okta_happy(*_):
    global FIRST_LOAD

    if FIRST_LOAD:
        FIRST_LOAD = False
        return

    try:
        CHROME_DRIVER.get(OKTA_REFRESH_URI)
    except:
        CHROME_DRIVER.quit()
        rumps.quit_application()


class LmaoApp(object):
    def __init__(self):
        self.app = rumps.App(name="Leave Me Alone Okta", title="😭", menu=["Quit"], quit_button=None)
        self.timer = rumps.Timer(make_okta_happy, OKTA_SESSION_DURATION / 2)
        self.timer.start()

    def run(self):
        self.app.run()


def setup_chrome():
    global CHROME_DRIVER
    executable = ChromeDriverManager().install()
    service = ChromeService(executable)
    options = ChromeOptions()

    home_dir = os.path.expanduser("~")
    user_data_dir = f"{home_dir}/Library/Application Support/Google/Chrome/"
    options.add_argument(f"user-data-dir={user_data_dir}")

    CHROME_DRIVER = Chrome(service=service, options=options)
    CHROME_DRIVER.get(OKTA_REFRESH_URI)


@rumps.clicked("Quit")
def quit(*_):
    global CHROME_DRIVER
    if CHROME_DRIVER:
        CHROME_DRIVER.quit()
    rumps.quit_application()


if __name__ == "__main__":
    setup_chrome()
    app = LmaoApp()
    app.run()
