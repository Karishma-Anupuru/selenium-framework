import pytest
from selenium import webdriver
from pageObjects.Createaccount import Create_account
from pageObjects.Createaccount import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_create:
    baseURL =ReadConfig.getApplicationURL()
    firstname=ReadConfig.getfirstname()
    lastname=ReadConfig.getlastname()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    confirmpassword=ReadConfig.getconfirmpassword()

    logger = LogGen.loggen()


    def test_homePage_title(self,setup):

        self.logger.info("***********Test_001_create*********")
        self.logger.info("******verifying homepage title***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Home Page":
            assert True
            self.driver.close()
            self.logger.info("******homepage title test is passed*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" +"test_homePage_title.png")
            self.driver.close()
            self.logger.info("*******homepage title test failed***********")
            assert False



    def test_CreateAccount(self,setup):

        self.logger.info("******verifying createaccount ***********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=Create_account(self.driver)
        self.lp.clickcreateanaccount()
        self.lp.setFirstname(self.firstname)
        self.lp.setLastname(self.lastname)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.setConfirmpassword(self.confirmpassword)
        self.lp.clickcreateAccountbutton()
        actual_title = self.driver.title
        if actual_title == "Create New Customer Account":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_createAccount.png")
            self.driver.close()
            assert False


    def test_login(self,setup):

        self.logger.info("******verifying login***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.clickSignin()
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickSigninbutton()
        actual_title =self.driver.title
        if actual_title == "Customer Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "test_login.png")
            self.driver.close()
            assert False




