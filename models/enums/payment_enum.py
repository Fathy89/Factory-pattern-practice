from enum import Enum 

class payment_method(Enum) :
    CREDIT_CARD:str = "credit_card"
    PAYPAL:str = "paypal"
    STRIPE:str = "stripe"
    APPLE:str="apple"