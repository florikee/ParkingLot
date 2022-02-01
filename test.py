#factory design pattern
#rip - replace if with polymorphism -> oop
#builder pattern
#strategy design pattern

class Elevator:
    #list e silos
    __silos=[]

    def __init__(self,silos):
        self.__silos=silos
    
    def acceptsShipment(self, grain,silo):
        for siloItem in self.__silos:
            if siloItem = silo:
                siloItem.addGrain(grain)
                return True
        return False

    def addSilosToSpecificIndex(self, silo, index):
        self.__silos.append(Silo())
        for i in range(len(self.__silos)-1,index, -1):
            silo[i-1]=silo[i]
        
        self.__silos[i]=silo
        #
#1,2, silo ,3,4,5,
class Silo:
    #list of grain
    __grains=[]
    #__isEmpty=True
    __siloMaximumSize=None

    def __init__(self,grains=None):
        self.__grains=grains

    def addGrain(self,grain):
        if grain.getGrades() = self.checkGrainGrade() and if grain.getName() = self.checkGrainType():
            self.__grains.append(grain)
        return
        

    
    def addGrains(self,grainList):
        self.__grains.extend(grainList)
    
    def checkIfEmpty(self):
        if(len(self.__grains)=0)return True
        return False
    
    def checkSiloWeight(self):
        totalWeight=0
        for grain in self.__grains:
            totalWeight=totalWeight+grain.getWeight()
        
        return totalWeight
    
    def checkGrainType(self):
        return self.__grains[0].getName()
    
    def checkGrainGrade(self):
        return self.__grains[0].getGrades()
        
#nenkupton nje thes
class Grain:
    _name=''
    _grades=None
    _weight=-1

    def __init__(self,name,grade,weight):
        self._grades=grade
        self._name=name
        self._weight=weight

    def placeOnSilos(self,elevator,silo):
        grainToAdd = self
        grainList=[grainToAdd]
        if elevator.acceptsShipment(grainList, silo):
            print('U shtua me sukses')
        else 
            print('ka nje problem me shtimin e te dhenave') 
        #

    def moveGrain(self):
        #
    
    def addGrain(self,grain):
        self._grades=grain.getGrades()
        self._name=grain.getName()
        self._weight=grain.getWeight()
    
    def getWeight(self):
        return self._weight

    def getName(self):
        return self._name

    def getGrades(self):
        return self._grades


class Bushels:
    __id=None

    def __init__(self,id):
        self.__id=id


class Person:
    _name=''

    def __init__(self,name):
        self._name=name

class Buyer(Person):

    def __init__(self,name):
        super().__init__(name)

    def buyGrain(self):
        #do something

class Conductor(Person):

    def __init__(self,name):
        super().__init__(name)

    def driveRailroadCar(self):
        #do something

class Driver(Person):

    def __init__(self,name):
        super().__init__(name)

    def driveTruck(self):
        #do something

class Seller(Person):

    def __init__(self,name):
        super().__init__(name)

    def SellGrain(self):
        #do something

class RailroadCar:
    __serialNumber=None
    __Conductor=None
    __GrainBuyer=None

    def __init__(self,serialNumber, conductor, buyer):
        self.__serialNumber=serialNumber
        self.__Conductor=conductor
        self.__GrainBuyer=buyer


class Truck:
    __plateNumber=None
    __seller=None
    __driver=None

    def __init__(self,plateNumber=None,seller=None,driver=None):
        self.__plateNumber=plateNumber
        self.__seller=seller
        self.__driver=driver


class TransporterService:
    
    #kush ben tranportimin, permes cfare mjeti transportues
    def MoveGrain(self, transporterName, role, transporterVehicleType, details ):
        person=HumanResources.CreatePerson(role, details)
        vehicle=VehicleFactory.CreateVehicle(transporterVehicleType, details,person)

#factory pattern design pattern
class VehicleFactory:

    vehicleTypes={
        "Truck":Truck(),
        "RailroadCar":RailroadCar()
    }

    #RIP
    #Replace if with polymorphism
    @staticmethod
    def CreateVehicle(transporterVehicleType, details, transporter):
        vehicle=None
        vehicle=vehicleTypes[transporterVehicleType]
        return vehicle


class HumanResources:

    personTypes={
        "Buyer":Buyer(),
        "Seller":Seller(),
        "Driver":Driver(),
        "Conductor":Conductor(),
    }

    @staticmethod
    def CreatePerson(role,person) :
        personInRole=None

        personInRole=personTypes[role]

        return personInRole



class SellerLicensDriveService:
    def SellerName(self, sellerName, sellerAddress, sellerAge, details=[]):
        sellerName = SellerFactory.CreateSellerName(
            sellerName, sellerAddress, sellerAge, details)

class SellerFactory:
    @staticmethod
    def CreateSellerName(sellerName, sellerAddress, sellerAge, details):
        seller = None
        if sellerAge >= 18:
            sellerLicensDrive = Driver(
                sellerName, sellerAddress, sellerAge, details)
        elif sellerAge < 18:
            sellerLicensDrive = Driver(
                sellerName, sellerAddress, sellerAge, None)
        return seller


from 'abc' import {ABC, abstractmethod} 

class PaymentInterface(ABC):
    @abstractmethod
    def pay(total): 
        pass

class CreditCardPaymentService(PaymentInterface):

    __CCNumbers=None
    __CCOwner=None
    __CCcvv=None

    def __init__(self,CCNumbers,CCOwner, CCcvv):
        self.__CCcvv=CCcvv
        self.__CCOwner=CCOwner
        self.__CCNumbers=CCNumbers

    def pay(self,total):
        #calls bank api


class PaypalPaymentService(PaymentInterface):
    __email=None
    __password=Non

    def __init__(self,email,password):
        self.__email=email
        self.__password=password

    def pay(self,total):
        #calls paypal api


#strategy pattern
class Market:
    __grain=[]
    __paymentMethod=None

    def BuyFromMarket(self):
        sumTotal=0
        for grain in self.__grain:
            sumTotal=+grain.price
        
        self.__paymentMethod.pay(sumTotal)

    
    def initializePaymentProcedure(self, paytype, credentials=[12345,"arber kadriu",144]):
        
        if paytype == "Paypal":
            self.__paymentMethod=PaypalPaymentService(credentials[0],credentials[1])
        elif paytype == 'CreditCard':
            self.__paymentMethod=CreditCardPaymentService(credentials[0],credentials[1],credentials[2])

        self.BuyFromMarket()


    def addToCart(self, items=[]):
        self.__grain=item

    def getPaymentMethod(self):
        return self.__paymentMethod



#implementimi i Builder design pattern
#automatikisht te perdoret ky DP per te u mbush te dhenat e objekteve person dhe vehicle



class PersonBuilder():

    @staticmethod
    def produce_buyer(name):
        return Buyer(name)

    @staticmethod
    def set_money(buyer, money):
        buyer.set_money(money)
        return buyer

    @staticmethod
    def produce_driver(name):
        return Driver(name)

    @staticmethod
    def produce_seller(name):
        return Seller(name)

    @staticmethod
    def produce_conductor(name):
        return Conductor(name)

# %%
class VehicleBuilder:
    
    @staticmethod
    def produce_railroad_vehicle(serialNumber, conductor, GrainBuyer):
        return RailroadVehicle(serialNumber, conductor, GrainBuyer)

    @staticmethod
    def produce_truck_vehicle(plate_number, seller, driver):
        return TruckVehicle(plate_number, seller, driver)


    


