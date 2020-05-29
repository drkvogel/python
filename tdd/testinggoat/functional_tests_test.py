from selenium import webdriver
import time

browser = webdriver.Firefox()
# browser = webdriver.Chrome()
time.sleep(3)
  # without sleep(): selenium.common.exceptions.WebDriverException: Message: Process unexpectedly closed with status 0

# if django server not running:
# selenium.common.exceptions.WebDriverException: Message: 
# Reached error page: about:neterror?e=connectionFailure&u=http%3A//localhost%3A8000/&c=UTF-8&f=regular&d=Firefox%20can%27t%20establish%20a%20connection%20to%20the%20server%20at%20localhost%3A8000.

browser.get('http://localhost:8000')
  # even when django server running, throws error on Firefox (but not on Chrome):
  # selenium.common.exceptions.WebDriverException: Message: 
  # Reached error page: about:neterror?e=connectionFailure&u=http%3A//localhost%3A8000/&c=UTF-8&f=regular&d=Firefox%20can%27t%20establish%20a%20connection%20to%20the%20server%20at%20localhost%3A8000.

browser.get('http://127.0.0.1:8000') # works on Firefox *and* Chrome
# remember, these are really old versions of django, python and selenium, etc, as recommended by the goat...

assert 'Django' in browser.title

# browser.close()
browser.quit()
