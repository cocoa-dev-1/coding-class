from abc import *

class Customer(ABC):
    def __init__(self, name, grade, point):
        self.name = name
        self.grade = grade
        self.point = point
        self.payment = 0.0

    @abstractmethod
    def pay(self, payment):
        pass

    @abstractmethod
    def benefit(self):
        pass

    def get_point(self):
        return self.point
    
    def upgrade(self):
        if self.payment >= 10000.0:
            self.grade = 'vip'
        elif self.payment >= 5000.0:
            self.grade = 'gold'
        else:
            self.grade = 'silver'
    
    def __str__(self):
        return f"{self.name} : {self.grade} (used: {self.payment}/ points: {self.point})"
    
class VipCustomer(Customer):
    saving = 0.1

    def __init__(self, name):
        self.sale = 0.8
        self.vipsale = True
        super().__init__(name, 'vip', 0)
    
    def pay(self, payment):
        vip_payment = (payment*self.sale)
        self.payment += vip_payment
        self.point += (payment*self.saving)
        self.benefit()
        return vip_payment
        
    def benefit(self):
        if self.payment > 15000.0 and self.vipsale:
            self.point += (self.payment*0.15)
            self.vipsale = False
        if self.payment > 20000.0:
            self.sale = 0.7

class GoldCustomer(Customer):
    saving = 0.05

    def __init__(self, name):
        self.sale = 0.9
        self.goldsale = True
        super().__init__(name, 'gold', 0)
    
    def pay(self, payment):
        gold_payment = (payment*self.sale)
        self.payment += gold_payment
        self.point += (payment*self.saving)
        self.benefit()
        return gold_payment
        
    def benefit(self):
        if self.payment > 7000.0 and self.goldsale:
            self.point += (self.payment*0.10)
            self.goldsale = False

class SilverCustomer(Customer):
    saving = 0.01

    def __init__(self, name):
        self.sale = 0.1
        self.silversale = True
        super().__init__(name, 'silver', 0)
    
    def pay(self, payment):
        silver_payment = (payment*self.sale)
        self.payment += silver_payment
        self.point += (payment*self.saving)
        self.benefit()
        return silver_payment
        
    def benefit(self):
        if self.payment > 2500.0 and self.silversale:
            self.point += 100.0
            self.silversale = False
