Introduction
------------

This repository contains basic example of usage PageObject
pattern with Selenium and Python (PyTest + Selenium) 
in the process of testing the (https://only.digital) site



Files
-----

[conftest.py](conftest.py) contains all the required code (fixtures) to run tests

[constants.py](constants.py) contains all needed data for performing tests (contain locators
to define web elements on web pages.
)

[pages/app.py](pages/app.py) helper class that contains information about driver, url and also all pages 

[pages/base_page.py](pages/base_page.py) contains PageObject pattern implementation for Python (implementation main methods of webdriver)

[pages/main_page.py](pages/main_page.py) contains PageObject pattern implementation for performing tests related with all actions on the main page


[tests/tests_site_only.py](tests/tests_site_only.py) contains all Web UI tests for Only (https://only.digital)


How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
    ```


Note:
~/chrome in this example is the file of Selenium WebDriver downloaded and unarchived on step #2.
