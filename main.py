import random
import string
import time

from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Return a single random word

outlook = "ACCOUNT"
password = "PASSWORD"

ed_options = webdriver.EdgeOptions()
ed_options.add_experimental_option("detach", True)
ed_driver = webdriver.Edge(options=ed_options)

ed_driver.get("https://login.microsoft.com")
time.sleep(2)
# ******** signin selenium to web browser required ********

ed_driver.get("https://www.bing.com/?FORM=Z9FD1")

for x in range(0, 32):
    word = "".join(random.choices(string.ascii_letters + " ", k=random.randint(0, 90)))
    search = ed_driver.find_element(By.ID, "sb_form_q")
    search.send_keys(Keys.CONTROL + "a")
    time.sleep(2)
    search.send_keys(word, Keys.ENTER)
    time.sleep(2)
    ed_driver.back()
