class ParkingLot:  # Declare class.
    street = ""
    city =""
    plates = []
    lots=[]

    # This is our constructor. It initializes variables when the object is created.
    def __init__(self, street, city, plates, lots):
        self.street = street
        self.city = city
        self.plates = []
        self.lots = []

# to append new assignemtn of lots
    def assignLotUse(self):
        self.plates = self.plates.append(self.plates)
        self.lots = self.lots.append(self.lots)

    # Declare a function to display details about parking lot.
    def showLotReport(self,street, city ):
        print("**************************************");
        print("Parking lot report:");
        print("**************************************");
        print(self.street+", "+self.city)
        for x in len(self.plates):
            print (self.plates[x]+" is parked in lot # "+self.lots[x])


#input
georgiaPark = ParkingLot("100 Georgia Street", "Vancouver")
georgiaPark.assignLotUse("X2X 102", 5)
georgiaPark.assignLotUse("M2Z 2K2", 8)
georgiaPark.showLotReport()

sanjosePark = ParkingLot("1 Main Street", "San Jose")
sanjosePark.assignLotUse("30211005", 3)
sanjosePark.assignLotUse("47810B23", 6)
sanjosePark.showLotReport()
