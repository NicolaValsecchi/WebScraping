# Setup and Execution

This document provides instructions for configuring the automation tool and running the example `main.py` script.

---

## Requirements

- Python 3.10 or higher
- Google Chrome and Microsoft Edge installed
- `Selenium`
- `python-dotenv`

---

## Setup

Before running the program:

1. Edit `WebScrapingUtils/browsersPathsDefines.py` to set the correct paths for your browser and driver executables.
2. Define the required environment variables for credentials:
```
FINANCIAL_TIME_USER
FINANCIAL_TIME_PASSWORD
IL_SOLE_24_ORE_USER
IL_SOLE_24_ORE_PASSWORD
```

You can define them using a `.env` file (see `PressRoutine/.env.example`), or set them manually in your terminal.

---

## Execution

### Run from Command Prompt (Windows):

```
set FINANCIAL_TIME_USER=your_ft_username
set FINANCIAL_TIME_PASSWORD=your_ft_password
set IL_SOLE_24_ORE_USER=your_sole24_username
set IL_SOLE_24_ORE_PASSWORD=your_sole24_password

python main.py
```

---
