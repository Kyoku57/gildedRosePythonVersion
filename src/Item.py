# -*- coding: utf-8 -*- 

class Item:
    """Item Class
    Rule : not modify this class
    """
    def __init__(self, name, sellin, quality):
        self.__name=name
        self.__sellin=sellin
        self.__quality=quality

    def setSellIn(self, sellin):
        self.__sellin=sellin

    def setQuality(self, quality):
        self.__quality=quality
    
    def getName(self):
        return self.__name

    def getSellIn(self):
        return self.__sellin

    def getQuality(self):
        return self.__quality
