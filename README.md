# WebScraping


This project is a general-purpose tool to streamline automated web browsing with Selenium.
It abstracts away common browser management tasks and interaction patterns, allowing faster development of web automation routines.

As an example, the project includes routines that automate login to **Financial Times** and **Il Sole 24 Ore**.


## Project Structure
```
WebScraping/
│
├── main.py                       # Entry point for test execution
│
├── PressRoutine/
│   ├── pressRoutine.py           # Login routines for FT and Il Sole 24 Ore
│   └── .env.example              # Example file for environment variable configuration
│
└── WebScrapingUtils/
    ├── browserManager.py         # Wrapper for Selenium WebDriver and browser control
    └── browsersPathsDefines.py   # User-defined paths for browser executables and drivers
```


---
