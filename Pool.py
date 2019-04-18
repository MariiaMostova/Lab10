class Pool:
    price_per_person = 70

    def __init__(self, address="Baker Street, 5", volume=20, max_guests=2,
                 length=2, height=2, width=5):
        self.address = address
        self.volume = volume
        self.max_guests = max_guests
        self.length = length
        self.height = height
        self.width = width
        
    def __del__(self):
        pass
    
    def __str__(self):
        return ('Adress of pool '+ self.address + ', volume = {0} litres,'
                + 'maximum quaintity of quests = {1}, pool length = {2},'
                + 'pool height = {3}, pool width = {4}.').format(self.volume,
                self.max_guests,self.length, self.height, self.width)

    @staticmethod
    def get_price_per_person():
        return Pool.price_per_person

water = Pool()
print(water)
waterfall = Pool("Green Street, 7", 100, 20)
print(waterfall)
sea = Pool("Yellow Street, 15", 300, 30, 10, 3, 10)
print(sea)
