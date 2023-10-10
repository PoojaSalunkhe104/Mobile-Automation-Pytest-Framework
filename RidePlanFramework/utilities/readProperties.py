import configparser

config=configparser.RawConfigParser()
config.read("./Configuration/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationPath():
        appPath=config.get('common info','Path')
        return appPath

    @staticmethod
    def getApplicationIOSPath():
        IOSPath = config.get('common info', 'iOSAppPath')
        return IOSPath


