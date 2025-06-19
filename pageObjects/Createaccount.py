import string
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
class Create_account:
    link_account_linktext="Create an Account"
    textbox_firstname_id="firstname"
    textbox_lastname_id="lastname"
    textbox_username_id="email_address"
    textbox_password_id="password"
    textbox_confirm_pass_id="password-confirmation"
    button_createaccount_xpath="//button[@title='Create an Account']"


    #link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def clickcreateanaccount(self):
        self.driver.find_element(By.LINK_TEXT, self.link_account_linktext).click()

    def setFirstname(self,firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).clear()
        random_text = "Sai" + ''.join(random.choices(string.ascii_letters, k=5))
        print("Generated random text:", random_text)
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(random_text)

    def setLastname(self,lastname):
        self.driver.find_element(By.ID, self.textbox_lastname_id).clear()
        random_text = "Kumar" + ''.join(random.choices(string.ascii_letters, k=5))
        print("Generated random text:", random_text)
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(random_text)

    def setUsername(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        random_text = "testuser" + ''.join(random.choices(string.ascii_letters + string.digits, k=6)) + "@example.com"
        print("Generated random text:", random_text)
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(random_text)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        password_text = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k=10))
        print("Generated random text:", password_text)
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password_text)

    def setConfirmpassword(self,password_text):
        self.driver.find_element(By.ID, self.textbox_confirm_pass_id).clear()
        self.driver.find_element(By.ID,self.textbox_confirm_pass_id).send_keys(password_text)

    def clickcreateAccountbutton(self):
        self.driver.find_element(By.XPATH,self.button_createaccount_xpath).click()


class LoginPage:
    link_signin_linktext="Sign In"
    textbox_username_id="email"
    textbox_password_id="pass"
    button_signin_xpath="(//button[@id='send2'])[1]"

    def __init__(self,driver):
        self.driver=driver

    def clickSignin(self):
        self.driver.find_element(By.LINK_TEXT,self.link_signin_linktext).click()

    def setUsername(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        random_text = "testuser" + ''.join(random.choices(string.ascii_letters + string.digits, k=6)) + "@example.com"
        print("Generated random text:", random_text)
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(random_text)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        password_text = ''.join(
            random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k=10))
        print("Generated random text:", password_text)
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password_text)

    def clickSigninbutton(self):
        self.driver.find_element(By.XPATH,self.button_signin_xpath).click()




