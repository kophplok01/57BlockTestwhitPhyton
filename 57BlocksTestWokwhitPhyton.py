import unittest
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time




class WorkTest(unittest.TestCase):

  
    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path =r"C:\WEBCHROMEDRIVER\chromedriver.exe")
  
    # Test case method. It should always start with test_
    def test_worktest_57blocks_checkingButtons(self):
          
        # get driver
        driver = self.driver
        # get github.com using selenium
        driver.get("https://github.com/login")
  
        # assertion to confirm if title has Github keyword in it
        self.assertIn("GitHub", driver.title)
        
        # I use xpath to locate each element of the page because for me, it seems the most efficient to work with
        termsXpath="//a[normalize-space()='Terms']"

        PrivacyXpath="//a[normalize-space()='Privacy']"

        SecurityXpath="//a[normalize-space()='Security']"

        ContactXpath="//a[normalize-space()='Contact GitHub']"

        CreateAccountXpath="//a[normalize-space()='Create an account']"

        ForgotPasswordXpath="//a[normalize-space()='Forgot password?']"

       # function that aims to test the functionality of buttons that have no direct relationship with the login process
        def checkButtonsByXpath(IdentifierByXpath):
            driver.find_element_by_xpath(IdentifierByXpath).click()  
            time.sleep(3)
            if  driver.current_url != "https://github.com/login":
                driver.back()

        checkButtonsByXpath(termsXpath)
        checkButtonsByXpath(PrivacyXpath)
        checkButtonsByXpath(SecurityXpath)
        checkButtonsByXpath(ContactXpath)
        checkButtonsByXpath(CreateAccountXpath)
        checkButtonsByXpath(ForgotPasswordXpath)
     
        assert "No results found." not in driver.page_source



    def test_worktest_57blocks_SignIn(self):
        
        driver = self.driver
        driver.get("https://github.com/login")
       
       

        def login_tescase1 ():
            driver.find_element_by_xpath("//input[@name='commit']").click()
            time.sleep(3)

        def login_tescase2 ():
            driver.get("https://github.com/login")
            user = driver.find_element_by_xpath("//input[@id='login_field']")
            user.send_keys("anaximander")
            driver.find_element_by_xpath("//input[@name='commit']").click()
            time.sleep(3)

        def login_tescase3 ():
            driver.get("https://github.com/login")
            user = driver.find_element_by_xpath("//input[@id='login_field']")
            password = driver.find_element_by_xpath("//input[@id='password']")
            user.clear()
            password.send_keys("aa23413ad")
            driver.find_element_by_xpath("//input[@name='commit']").click()
            time.sleep(3)

        def login_tescase4 ():
            user = driver.find_element_by_xpath("//input[@id='login_field']")
            password = driver.find_element_by_xpath("//input[@id='password']")
            user.clear
            password.clear
            user.send_keys("anaximanderpkk@gmail.com")
            password.send_keys("57blocksworktest")
            driver.find_element_by_xpath("//input[@name='commit']").click()
            time.sleep(10)

        login_tescase1()
        login_tescase2()
        login_tescase3()
        login_tescase4()
       
      
       
  
    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()
  
# execute the script
if __name__ == "__main__":
    unittest.main()

