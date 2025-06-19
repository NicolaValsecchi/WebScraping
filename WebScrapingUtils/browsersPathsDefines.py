"""
This configuration file defines absolute paths for browser executables, drivers, and user data directories.
Please update the paths below according to your system environment. Use raw strings (r"...") and ensure all paths are valid.

Note: These variables are required for browser automation using tools like Selenium.
"""

# Chrome configuration
CHROME_EXE_PATH = r"C:\Path\To\Chrome\Application\chrome.exe"            # e.g., r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CHROME_DRIVER_PATH = r"C:\Path\To\chromedriver.exe"                      # e.g., r"C:\Drivers\chromedriver-win64\chromedriver.exe"
CHROME_USER_DATA_DIR = r"--user-data-dir=C:\Path\To\Chrome\User Data"    # e.g., r"--user-data-dir=C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data"

# Edge configuration
EDGE_EXE_PATH = r"C:\Path\To\Edge\Application\msedge.exe"                # e.g., r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
EDGE_DRIVER_PATH = r"C:\Path\To\msedgedriver.exe"                        # e.g., r"C:\Drivers\edgedriver_win64\msedgedriver.exe"
EDGE_USER_DATA_DIR = r"--user-data-dir=C:\Path\To\Edge\User Data"        # e.g., r"--user-data-dir=C:\Users\YourUsername\AppData\Local\Microsoft\Edge\User Data"

"""
To download new version of webdriver:
- Microsoft Edge:
    insert the target version of Microsoft Edge (Edge>menu>Settings>About Microsoft Edge>Version)
    https://msedgewebdriverstorage.z22.web.core.windows.net/?prefix=136.0.3240.50/
    or chose it from the list
    https://msedgewebdriverstorage.z22.web.core.windows.net
- Chrome:
    insert the target version of Chrome (Chrome>menu>Settings>About Chrome>Version)
    https://storage.googleapis.com/chrome-for-testing-public/136.0.7103.49/win64/chromedriver-win64.zip
"""
