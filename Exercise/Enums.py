class Bulb(object):
    class BulbSize:
        SMALL='SMALL'
        MEDIUM='MEDIUM'
        LARGE='LARGE'
    
    def __init__(self):
        self.isOn = False
        self.size = Bulb.BulbSize.MEDIUM
    
    def getBulbSize(self):
        return self.size
    
    def setBulbSize(self, value):
        self.size = value
    
class BulbDemo(object):
    @classmethod
    def main(cls):
        b = Bulb()
        print("Bulb Size : "+b.getBulbSize())

if __name__ == '__main__':
    bulb = BulbDemo()
    bulb.main()