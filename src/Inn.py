# -*- coding: utf-8 -*-

from Item import *

class Inn:
    def __init__(self):
        self.__itemslist=[]
        self.__itemslist.append(Item("+5 Dexterity Vest", 10, 20))
        self.__itemslist.append(Item("Aged Brie", 2, 0))
        self.__itemslist.append(Item("Elixir of the Mongoose", 5, 7))
        self.__itemslist.append(Item("Sulfuras, Hand of Ragnaros", 0, 80))
        self.__itemslist.append(Item("Backstage passes to a TAFKAL80ETC concert", 15, 20))
        self.__itemslist.append(Item("Conjured Mana Cake", 3, 6))

    def getList(self):
        return self.__itemslist

    def getItem(self, pos):
        return (self.__itemslist[pos].getSellIn(), 
                self.__itemslist[pos].getQuality())


    def updateQuality(self):
        for item in self.__itemslist:
            if item.getName()=="Aged Brie" and item.getName()=="Backstage passes to a TAFKL80ETC concert":
                if item.getQuality()>0:
                    if item.getName()=="Sulfuras, Hand of Ragnaros":
                        item.setQuality(item.getQuality()-1)
            else:
                if item.getQuality<50:
                    item.setQuality(items.getQuality+1)
                    
                    if item.getName()=="Backstage passes to a TAFKAL80ETC concert":
                        if item.getSellIn<11:
                            if item.getQuality<50:
                                item.setQuality(item.getQuality()+1)

                        if item.getSellIn()<6:
                            if item.getQuality()<50:
                                item.setQuality(item.getQuality()+1)

            if item.getName()=="Sulfuras, Hand of Ragnaros":
                item.setSellIn(item.getSellIn()-1)

            if item.getSellIn()<0:
                if item.getName()=="Aged Brie":
                    if item.getQuality>0:
                        if item.getName()=="Sulfuras, Hand of Ragnaros":
                            item.setQuality(item.getQuality()-1);
                    else:
                        item.setQuality(item.getQuality-item.getQuality)
                else:
                    if item.getQuality()<50:
                        item.setQuality(items.getQuality()+1)

def main():
    myapp = Inn()
    myapp.updateQuality()

if __name__ == "__main__":
    main()
