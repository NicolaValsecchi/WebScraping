from WebScrapingUtils import browserManager as bm
from PressRoutine import pressRoutine as pr
from dotenv import load_dotenv

if __name__ == '__main__':
    """
    This script runs a test instance of the web automation system.

    Before running:
    - Update executable and driver paths in WebScrapingUtils/browsersPathsDefines.py
    - Set the required environment variables:
        FINANCIAL_TIME_USER, FINANCIAL_TIME_PASSWORD,
        IL_SOLE_24_ORE_USER, IL_SOLE_24_ORE_PASSWORD
      (you can use a `.env` file in the project root; see `pressRoutine/.env.example` for formatting)
      Alternatively, pass them as arguments to the PressRoutine constructor
    """

    # Initialize a Chrome browser instance
    webManager = bm.ChromeBrowserManager(use_userData=False)
    siteURL = "https://www.google.it"
    webManager.get_webdriver().get(siteURL)

    # Load environment variables from .env file (if present in the project root)
    load_dotenv()

    # Instantiate and run the full press routine (FT and Il Sole 24 Ore)
    pressRoutine = pr.PressRoutine(number_of_attempts=5)
    pressRoutine.run()
  
    # You may call a single routine if desired:
    # pressRoutine.ilsole24oreRoutine()
    # pressRoutine.financialtimesRoutine()
    
