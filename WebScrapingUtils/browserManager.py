from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.edge.service import Service as ServiceEdge
from selenium.common.exceptions import WebDriverException, NoSuchWindowException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
from enum import Enum

from WebScrapingUtils.browsersPathsDefines import *


class BrowserConfig:

    def __init__(self, exe_path, driver_path, user_data_dir, options):
        self.number_of_attempts = 20
        self.exe_path = exe_path
        self.driver_path = driver_path
        self.user_data_dir = user_data_dir
        self.options = options

    def __repr__(self):
        return f"BrowserConfig(exe_path={self.exe_path}, driver_path={self.driver_path}, user_data_dir={self.user_data_dir})"


class Browser(Enum):
    CHROME = "Chrome"
    EDGE = "Edge"


browsers = {
    Browser.CHROME: BrowserConfig(
        exe_path=CHROME_EXE_PATH,
        driver_path=CHROME_DRIVER_PATH,
        user_data_dir=CHROME_USER_DATA_DIR,
        options=webdriver.ChromeOptions()
    ),
    Browser.EDGE: BrowserConfig(
        exe_path=EDGE_EXE_PATH,
        driver_path=EDGE_DRIVER_PATH,
        user_data_dir=EDGE_USER_DATA_DIR,
        options=webdriver.EdgeOptions()
    )
}


class BrowserManager:
    def __init__(self, browser_name, use_userData=False, leaveOpen=True, incognito=False, number_of_attempts=None, headless=False):
        """
        browser_name: 'chrome' or 'edge'
        use_userData: use existing browser profile
        leaveOpen: detach browser on exit
        incognito: open in private mode
        headless: run without GUI
        number_of_attempt
        """

        if isinstance(browser_name, str):
            browser_name = Browser[browser_name.upper()]
        if browser_name not in browsers:
            raise ValueError(f"Unsupported browser: {browser_name}")

        browser = browsers[browser_name]

        browser_options = browser.options
        browser_options.binary_location = browser.exe_path  # browser exe path

        if headless:
            browser_options.add_argument("--headless=new" if hasattr(browser_options, 'add_argument') else "--headless")
            browser_options.add_argument("--disable-gpu")

        if leaveOpen:
            browser_options.add_experimental_option("detach", True)  # to leave the browser open

        if use_userData:
            browser_options.add_argument(browser.user_data_dir)  # use your browser profile

        if incognito: #and (browser_name == bo.Browser.CHROME):
            browser_options.add_argument("--incognito")

        # Open the browser
        match browser_name:
            case Browser.CHROME:
                serv = ServiceChrome(browser.driver_path)
                self._webdriver = webdriver.Chrome(service=serv, options=browser_options)
            case Browser.EDGE:
                serv = ServiceEdge(browser.driver_path)
                self._webdriver = webdriver.Edge(service=serv, options=browser_options)
            case _:
                raise ValueError('No browser selected or unsupported browser.')

        self._number_of_attempts = number_of_attempts
        if number_of_attempts is None:
            self._number_of_attempts = browser.number_of_attempts

    def get_webdriver(self):
        return self._webdriver

    def pressByLINK_TEXT(self, text):
        for attempt in range(self._number_of_attempts):
            try:
                button = self._webdriver.find_element(By.LINK_TEXT, text)
                button.click()
                return
            except (NoSuchElementException, Exception):
                print(f"Element {text} not found. Next try in 1sec.")
                time.sleep(1)
        raise Exception(f"Element {text} not found after {self._number_of_attempts} attempts.")

    def fillTextBox_byID(self, id, text):
        for attempt in range(self._number_of_attempts):
            try:
                textbox = self._webdriver.find_element(By.ID, id)
                textbox.clear()
                textbox.send_keys(text)
                return
            except (NoSuchElementException, Exception):
                print(f"Element {id} not found. Next try in 1sec.")
                time.sleep(1)
        raise Exception(f"Element {id} not found after {self._number_of_attempts} attempts.")

    def pressByID(self, text):
        for attempt in range(self._number_of_attempts):
            try:
                button = self._webdriver.find_element(By.ID, text)
                button.click()
                return
            except (NoSuchElementException, Exception):
                print(f"Element {text} not found. Next try in 1sec.")
                time.sleep(1)
        raise Exception(f"Element {text} not found after {self._number_of_attempts} attempts.")

    def pressByXPATH(self, text, option=0):
        match option:
            case 0:  # text
                XPATH_text = text
            case 1:  # //div[contains(@class, 'tab-text') and text()=text]
                XPATH_text = f"//div[contains(@class, 'tab-text') and text()='{text}']"
            case 2:  # //p[contains(text(),text)]
                XPATH_text = f"//p[contains(text(),'{text}')]"
            case 3:  # //input[@alt=text]
                XPATH_text = f"//input[@alt='{text}']"
            case 4:  # //a[span[text()=text]]
                XPATH_text = f"//a[span[text()='{text}']]"
            case 5:  # //button[text()==text]
                XPATH_text = f"//button[text()='{text}']"
            case 6:  # //button[span[text()=text]]
                XPATH_text = f"//button[span[text()='{text}']]"
            case 7:  # //li[.//span[text()='text']]
                XPATH_text = f"//li[.//span[text()='{text}']]"
            case _:
                print(f"Error: option {option} is not valid.")
                return

        for attempt in range(self._number_of_attempts):
            try:
                button = self._webdriver.find_element(By.XPATH, XPATH_text)
                button.click()
                return
            except (NoSuchElementException, Exception):
                print(f"Element {text} not found. Next try in 1sec.")
                time.sleep(1)
        raise Exception(f"Element {text} not found after {self._number_of_attempts} attempts.")

    def switchPage(self, page):
        for attempt in range(self._number_of_attempts):
            try:
                if isinstance(page, int):
                    if page < self.getOpenPagesNumber():
                        self._webdriver.switch_to.window(self._webdriver.window_handles[page])
                        return
                    else:
                        print(f"Page number {page} not valid. Next try in 1sec")
                        time.sleep(1)
                elif isinstance(page, str):
                    window_handles = self._webdriver.window_handles
                    if page in window_handles:
                        self._webdriver.switch_to.window(page)
                        return
                    else:
                        print(f"Page {page} not found. Next try in 1sec")
                        time.sleep(1)
                else:
                    print("Invalid input type. Must be int or str.")
                    return
            except (NoSuchWindowException, WebDriverException):
                print(f"Error switching to page {page}. Next try in 1sec")
                time.sleep(1)
        raise Exception(f"Page {page} not found after {self._number_of_attempts} attempts.")

    def getOpenPagesNumber(self):
        return len(self._webdriver.window_handles)

    def closeDuplicatePages(self):
        url_list = set()

        for page in self._webdriver.window_handles:
            try:
                self._webdriver.switch_to.window(page)
                url = self._webdriver.current_url
                if url in url_list:
                    self._webdriver.close()
                else:
                    url_list.add(url)
            except (NoSuchWindowException, WebDriverException):
                continue

        self.switchPage(self._webdriver.window_handles[-1])

    def openNewPage(self, url):
        self._webdriver.execute_script("window.open('about:blank');")
        self._webdriver.switch_to.window(self._webdriver.window_handles[self.getOpenPagesNumber() - 1])
        self._webdriver.get(url)


class ChromeBrowserManager(BrowserManager):
    def __init__(self, use_userData=False, leaveOpen=True, incognito=False, number_of_attempts=None, headless=False):
        super().__init__('chrome', use_userData, leaveOpen, incognito, number_of_attempts, headless)


class EdgeBrowserManager(BrowserManager):
    def __init__(self, use_userData=False, leaveOpen=True, incognito=False, number_of_attempts=None, headless=False):
        super().__init__('edge', use_userData, leaveOpen, incognito, number_of_attempts, headless)

