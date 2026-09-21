from db.database import Data
from factory.payement_factory import *
from models.payment_models import payment_model


class PaymentService:

    def __init__(self, payment_method: payment_model, name: str):

        self.db = Data

        self.payment = PaymentFactory.create(
            payment_method.payment_type.value
        )

        self.amount = payment_method.amount

        self.client = next(
            (i for i in self.db if i["name"] == name),
            None
        )
        if self.client is None:
            raise ValueError("Client not found")
    def deposite(self)  : 
        
        if self.amount <= 0:
            return {"Message": "Invalid amount of money"}

        self.client["balance"] += self.amount

        return self.payment.pay(self.amount)
        

    def withdraw(self):

        if self.amount <= 0:
            return {"Message": "Invalid amount of money"}

        if self.client["balance"] < self.amount:
            return {"Message": "Insufficient balance"}

        self.client["balance"] -= self.amount

        return self.payment.pay(self.amount)    
    
    # def create_account(self,name,amount) : 
    #     pass
    
    
    # def delete_account(self,name)  :
    #     pass