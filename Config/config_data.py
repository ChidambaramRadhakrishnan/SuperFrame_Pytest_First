import configparser

config = configparser.RawConfigParser()
config.read(".\Config\config.ini")

class data:

    @staticmethod
    def getdata():
        datas = config.get('common info', 'fruit')
        print(datas)
        return datas
