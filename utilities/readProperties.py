import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url =config.get('common info','baseURL')
        return url

    @staticmethod
    def getfirstname():
        firstname=config.get('common info', 'firstname')
        return firstname

    @staticmethod
    def getlastname():
        lastname=config.get('common info', 'lastname')
        return lastname

    @staticmethod
    def getusername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getconfirmpassword():
        confirmpassword = config.get('common info', 'confirmpassword')
        return confirmpassword


