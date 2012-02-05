# -*- coding: utf-8 -*-

import os
from Item import *
import bottle

bottle.debug

class Inn:
    def __init__(self):
        """Constructor
        Rule : not modify this method
        """
        self.__itemslist=[]
        self.__itemslist.append(Item("+5 Dexterity Vest", 10, 20))
        self.__itemslist.append(Item("Aged Brie", 2, 0))
        self.__itemslist.append(Item("Elixir of the Mongoose", 5, 7))
        self.__itemslist.append(Item("Sulfuras, Hand of Ragnaros", 0, 80))
        self.__itemslist.append(Item("Backstage passes to a TAFKAL80ETC concert", 15, 20))
        self.__itemslist.append(Item("Conjured Mana Cake", 3, 6))


    def getList(self):
        """Return the items list"""
        return self.__itemslist

    def getItem(self, pos):
        """Return a tuple with sellin and quality properties for an item"""
        return (self.__itemslist[pos].getSellIn(), 
                self.__itemslist[pos].getQuality())

    def decreaseSellIn(self, item):
        """decrease SellIn property"""
        item.setSellIn(item.getSellIn()-1)

    def increaseQuality(self, item, iteration=1):
        """increase Quality property and check value between 0<x<50"""
        item.setQuality(item.getQuality()+iteration)
        if item.getQuality()<0:
            item.setQuality(0)
        if item.getQuality()>50:
            item.setQuality(50)

        

    def updateQuality(self):
        """update sellin and quality for a day"""
        for item in self.__itemslist:
            # Traitement au cas par cas (pas de règles générales)
            if item.getName()=="Aged Brie":
                self.decreaseSellIn(item)
                self.increaseQuality(item,1)
                continue
            elif item.getName()=="Backstage passes to a TAFKAL80ETC concert":
                self.decreaseSellIn(item)
                if item.getSellIn()<0:
                    item.setQuality(0)
                if item.getSellIn()>=0:
                    self.increaseQuality(item,3)
                if item.getSellIn()>5:
                    self.increaseQuality(item,-1)                
                if item.getSellIn()>10:
                    self.increaseQuality(item,-1)
                continue
            elif item.getName()=="Sulfuras, Hand of Ragnaros":
                item.setSellIn(0)
                continue
            else:
                self.decreaseSellIn(item)
                self.increaseQuality(item, (-2 if item.getName()=="Conjured Mana Cake" else -1)*(2 if item.getSellIn()<0 else 1))

def main():
    bottle.run(host="localhost",port=8080)    

@bottle.route('/myapp', method="get")
def webapp():
    myapp = Inn()

    try:
        numday=int(bottle.request.GET["incr"])
    except:
        numday=0
    finally:
        for i in range(0,numday): 
            myapp.updateQuality()
        template_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'interface.html')
        return bottle.template(template_file,
                               items=myapp.getList(),
                               numday=numday)


if __name__ == "__main__":
    main()
