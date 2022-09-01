import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

EMAILFIELD_NTNU = '//input[@name="email"]'
SUBMITBUTTON_NTNU = '//input[@name="Submit"]'
MSFTPLACENTNU = "Web Authentication Redirect"

# Make selenium run headless.
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome('chromedriver', options=options)
driver.get('http://www.msftconnecttest.com/redirect')
pagetitle = driver.title


def main():
    WebDriverWait(driver, 20000).until(ec.visibility_of_element_located((By.TAG_NAME, 'body')))
    time.sleep(3)
    print("Attempting to login.")
    if MSFTPLACENTNU in pagetitle:
        email = "autolog@logon.com"
        email_field = driver.find_element(By.XPATH, EMAILFIELD_NTNU)
        email_field.send_keys(email)
        submit_button = driver.find_element(By.XPATH, SUBMITBUTTON_NTNU)
        submit_button.click()
    else:
        print("Page is not supported. Only works on the NTNU network..")
        input()
    driver.close()


if __name__ == '__main__':
    main()
