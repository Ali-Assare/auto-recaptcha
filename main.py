from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

import recaptcha

auth = '<your_api_key_here>'
link = "https://www.google.com/recaptcha/api2/demo"


def initialize_driver(link):
    options = Options()
    ua = UserAgent(use_cache_server=False, verify_ssl=False)
    userAgent = ua.chrome
    print(userAgent)
    options.add_argument(f'user-agent={userAgent}') # add fake user
    options.add_argument("--incognito") # browse incognito
    options.add_experimental_option("detach", True) # this allows the browser to stay awake after the closing driver.
    driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe') # initialize the driver
    driver.get(link) # open the link
    return driver
    

driver = initialize_driver(link)
recaptcha.handle_recaptcha(driver, auth)
