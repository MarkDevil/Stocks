# coding=utf-8
import ConfigParser
import os


class ReadWriteConfFile:
    def __init__(self):
        pass

    currentDir = os.path.dirname(__file__)
    filepath = currentDir + os.path.sep + "setting.ini"
    #print filepath

    @staticmethod
    def getConfigParser():
        cf = ConfigParser.ConfigParser()
        cf.read(ReadWriteConfFile.filepath)
        return cf

    @staticmethod
    def writeConfigParser(cf):
        f = open(ReadWriteConfFile.filepath, "w")
        cf.write(f)
        f.close()

    @staticmethod
    def getSectionValue(section, key):
        cf = ReadWriteConfFile.getConfigParser()
        return cf.get(section, key)


    @staticmethod
    def addSection(section):
        cf = ReadWriteConfFile.getConfigParser()
        allsections = cf.sections()
        if section in allsections:
            return
        else:
            cf.add_section(section)
            ReadWriteConfFile.writeConfigParser(cf)

    @staticmethod
    def setSectionValue(section, key, value):
        cf = ReadWriteConfFile.getConfigParser()
        cf.set(section, key, value)
        ReadWriteConfFile.writeConfigParser(cf)


if __name__ == '__main__':
    # ReadWriteConfFile.addSection('messages')
    # ReadWriteConfFile.setSectionValue('messages', 'name', 'sophia')
    x = ReadWriteConfFile.getSectionValue('maillist', 'user')
    print x