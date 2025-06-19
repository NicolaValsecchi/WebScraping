from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import time
import os
from WebScrapingUtils import browserManager as bm

class PressRoutine:
    """
    Automates login procedures for Financial Times and Il Sole 24 Ore using Selenium.
    Credentials can be passed explicitly to the constructor or loaded from environment variables.

    NOTE: If credentials are not passed as parameters, this class expects the following environment variables to be set:
        FINANCIAL_TIME_USER, FINANCIAL_TIME_PASSWORD,
        IL_SOLE_24_ORE_USER, IL_SOLE_24_ORE_PASSWORD

    Environment variables can be defined in a `.env` file, which will be automatically loaded (if present)
    from the project root when `load_dotenv()` is called.
    See the `.env.example` file in this repository for formatting guidance.
    """

    def __init__(self, user_id_FT=None, user_pwd_FT=None, user_id_24=None, user_pwd_24=None, number_of_attempts=None):

        self._home_url_FT = 'https://www.ft.com/'
        self._user_id_FT = user_id_FT
        if user_id_FT is None:
            self._user_id_FT = str(os.getenv("FINANCIAL_TIME_USER"))
        self._user_pwd_FT = user_pwd_FT
        if user_pwd_FT is None:
            self._user_pwd_FT = str(os.getenv("FINANCIAL_TIME_PASSWORD"))

        self._home_url_24 = 'https://www.ilsole24ore.com/'
        self._user_id_24 = user_id_24
        if user_id_24 is None:
            self._user_id_24 = str(os.getenv("IL_SOLE_24_ORE_USER"))
        self._user_pwd_24 = user_pwd_24
        if user_pwd_24 is None:
            self._user_pwd_24 = str(os.getenv("IL_SOLE_24_ORE_PASSWORD"))

        self._webdriver = bm.EdgeBrowserManager(number_of_attempts=number_of_attempts)

    def financialtimesRoutine(self):
        """
        Opens FT homepage, accepts cookies, and performs login using provided credentials.
        """

        self._webdriver.openNewPage(self._home_url_FT)
        #n_pages = self._webdriver.getOpenPagesNumber()

        iframe = self._webdriver.get_webdriver().find_element(By.XPATH, '//*[@id="sp_message_iframe_1299719"]')
        # NOTE: The iframe ID (sp_message_iframe_1299719) may change over time.
        # If this selector fails, inspect the updated iframe ID and modify the XPath accordingly.

        self._webdriver.get_webdriver().switch_to.frame(iframe)
        self._webdriver.pressByXPATH("Accept Cookies", 5)

        self._webdriver.get_webdriver().switch_to.default_content()

        self._webdriver.pressByID("o-header-top-link-signin")

        self._webdriver.fillTextBox_byID("enter-email", self._user_id_FT)
        self._webdriver.pressByID("enter-email-next")
        self._webdriver.fillTextBox_byID("enter-password", self._user_pwd_FT)
        self._webdriver.pressByID("sign-in-button")

        #self._webdriver.closeDuplicatePages()

    def ilsole24oreRoutine(self):
        """
        Opens Il Sole 24 Ore homepage, accepts cookies, and performs login using provided credentials.
        """
        self._webdriver.openNewPage(self._home_url_24)
        #n_pages = self._webdriver.getOpenPagesNumber()

        self._webdriver.pressByID("onetrust-accept-btn-handler")

        login_attempts = 5
        for attempt in range(login_attempts):  # more attempts due to latency
            try:
                self._webdriver.pressByXPATH("Accedi", 6)
                self._webdriver.fillTextBox_byID("login-username", self._user_id_24)
                self._webdriver.fillTextBox_byID("login-password", self._user_pwd_24)
                self._webdriver.pressByXPATH("Accedi", 5)
                return
            except (NoSuchElementException, Exception):
                print(f"Login failed. Next try in 1sec.")
                time.sleep(1)

        raise Exception(f"Login failed after {login_attempts} attempts.")

    def run(self):
        """
        Executes both login routines (FT and Il Sole 24 Ore).
        """
        self.financialtimesRoutine()
        self.ilsole24oreRoutine()


if __name__ == '__main__':
    # Loads environment variables from a .env file (if present in the project root)
    load_dotenv()

    # Instantiate and run the full press routine
    pr = PressRoutine(number_of_attempts=5)
    pr.run()
