from Inn import *
import pdb

def testInnNormalItem():
    """Normal Item
    Each iteration : 
        - SellIn-1
        - Quality-1
        - if SellIn<0 Quality-2
        - Quality>0
    Exemple, item[2] 
    """
    myinn = Inn()
    for i in range(1,50):
        # Prepare before and after updateQuality
        before_item = myinn.getItem(2)
        myinn.updateQuality()
        after_item = myinn.getItem(2)

        # Test if SellIn decrease
        print "iteration="+str(i),
        print "before="+str(before_item),
        print "after="+str(after_item)
        assert(after_item[0]==before_item[0]-1)
        
        # Test if Quality decrease
        if after_item[0]<0:
            if before_item[1]>=2:    
                assert(after_item[1]==before_item[1]-2)
        else:
            if before_item[1]>=1:
                assert(after_item[1]==before_item[1]-1)

        # Test if Quantity is always > 0        
        assert(after_item[1]>=0 and after_item[1]<=50)


def testConjuredItem():
    """Conjured Item
    Like Normal but Quality decrease twice as fast
    Exemple, item[2]
    """
    myinn = Inn()
    for i in range(1,50):
        # Prepare before and after updateQuality
        before_item = myinn.getItem(5)
        myinn.updateQuality()
        after_item = myinn.getItem(5)

        # Test if SellIn decrease
        print "iteration="+str(i),
        print "before="+str(before_item),
        print "after="+str(after_item)
        assert(after_item[0]==before_item[0]-1)
        
        # Test if Quality decrease
        if after_item[0]<0:
            if before_item[1]>=4:
                assert(after_item[1]==before_item[1]-4)
        else:
            if before_item[1]>=2:
                assert(after_item[1]==before_item[1]-2)

        # Test if Quantity is always > 0        
        assert(after_item[1]>=0 and after_item[1]<=50)


def testInnAgeBrieItem():
    """AgeBrie Item
    Each iteration : 
        - SellIn-1
        - Quality+1
        - 0<Quality<50
    Exemple, item[1] 
    """
    myinn = Inn()
    for i in range(1,50):
        # Prepare before and after updateQuality
        before_item = myinn.getItem(1)
        myinn.updateQuality()
        after_item = myinn.getItem(1)

        # Test if SellIn decrease
        print "iteration="+str(i),
        print "before="+str(before_item),
        print "after="+str(after_item)
        assert(after_item[0]==before_item[0]-1)
        
        # Test if Quality increase
        if before_item[1]<50:
            assert(after_item[1]==before_item[1]+1)
        
        # Test if Quantity is always > 0 and <50
        assert(after_item[1]>=0 and after_item[1]<=50)


def testInnSulfurasItem():
    """Sulfuras Item
    Each iteration : 
        - SellIn = 0
        - Quality not move
    Exemple, item[3] 
    """
    myinn = Inn()
    for i in range(1,50):
        # Prepare before and after updateQuality
        before_item = myinn.getItem(3)
        myinn.updateQuality()
        after_item = myinn.getItem(3)

        # Test if SellIn = 0 
        print "iteration="+str(i),
        print "before="+str(before_item),
        print "after="+str(after_item)
        assert(after_item[0]==0)
        
        # Test if Quality not move
        assert(after_item[1]==before_item[1])


def testInnBackStageItem():
    """Backstage Item
    Each iteration : 
        - SellIn-1
        - Quality+1 if > 10, if < 10 +2, if < 5 +3, if < 0 =0
        - 0<Quality<50
    Exemple, item[4] 
    """
    myinn = Inn()
    for i in range(1,50):
        # Prepare before and after updateQuality
        before_item = myinn.getItem(4)
        myinn.updateQuality()
        after_item = myinn.getItem(4)

        # Test if SellIn decrease
        print "iteration="+str(i),
        print "before="+str(before_item),
        print "after="+str(after_item)
        assert(after_item[0]==before_item[0]-1)
        
        # Test if Quality increase
        addquality=0
        if after_item[0]<0:
            assert(after_item[1]==0)
        if after_item[0]>=0:
            addquality=3
        if after_item[0]>5:
            addquality=2
        if after_item[0]>10:
            addquality=1
        if before_item[1]<47:
            assert(after_item[1]==before_item[1]+addquality)
        
        # Test if Quantity is always > 0 and <50
        assert(after_item[1]>=0 and after_item[1]<=50)
