import configparser


config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url=config.get('info','baseURL')
        return url

    @staticmethod
    def getClientCode():
        clientcode = config.get('info', 'clientcode')
        return clientcode

    @staticmethod
    def getEnv():
        env = config.get('info', 'env')
        return env

    @staticmethod
    def getFn():
        fn = config.get('info', 'fn')
        return fn

    @staticmethod
    def getLn():
        ln = config.get('info', 'ln')
        return ln

    @staticmethod
    def getAmt():
        amt = config.get('info', 'amt')
        return amt

    @staticmethod
    def getCon():
        con = config.get('info', 'con')
        return con

    @staticmethod
    def getEmail():
        email = config.get('info', 'email')
        return email

    @staticmethod
    def getVisadebit():
        visadebit = config.get('info', 'visadebit')
        return visadebit

    @staticmethod
    def getVisacredit():
        visacredit = config.get('info', 'visacredit')
        return visacredit

    @staticmethod
    def getRupaydebit():
        rupaydebit = config.get('info', 'rupaydebit')
        return rupaydebit

    @staticmethod
    def getRupaycredit():
        rupaycredit = config.get('info', 'rupaycredit')
        return rupaycredit

    @staticmethod
    def getUpiId():
        upiid = config.get('info', 'upiid')
        return upiid

    @staticmethod
    def getpath():
        path = config.get('info', 'path')
        return path
