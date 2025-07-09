This repo contains a sample solution for testing https://rickandmortyapi.com/ website using [Playwright](https://playwright.dev/)  and its [Python](https://github.com/microsoft/playwright-python) implementation.

More information about Playwright can be found [here](https://playwright.dev).

# How to find elements on a web page

The easiest way to locate elements on a web page is to run your test in a debugging mode and use Pick Locator option in Playwright Inspector - see a screenshot.
```
% PWDEBUG=1 pytest -s -k test_case_name
```

![img.png](Inspector.png)

Another way is to use Inspect option in your browser.


# How to Execute Playwright tests
To run all tests in a headless mode without showing a browser, open a terminal and type:
```
pytest
```

To run all tests in a headed mode:
```
pytest --headed
```

To run all test cases in a specific file:
```
pytest Tests/test_verify_page_elements.py 
```

To execute a specific test case:
```angular2html
pytest -s -k test_verify_navigation_to_docs_page
```

To generate reports, install `pip install pytest-html` and use `--html` option while running scripts: 
```
pytest --html=Results/verify.html Tests/test_verify_page_elements.py
```