from abc import ABC ,abstractmethod



class payment_factory(ABC) : 
    
    def __init__(self) : 
        pass
    @abstractmethod
    def pay (self, amount) :  
        pass
    
    
class PayPal(payment_factory) : 
    def __init__(self):
        super().__init__()
        
    def pay(self, amount):
        return f"This paid {amount} using Paypal"
    

    
class CreditCard(payment_factory) : 
    def __init__(self):
        super().__init__()
        
    def pay(self, amount):
        return f"This paid {amount} using CridetCard"
    

class StripePayment(payment_factory):
    def __init__(self):
        super().__init__()
        
    def pay(self, amount):
        return f"This paid {amount} using StripePayment"
    

class PaymentFactory:

    _payments = {
        "paypal": PayPal,
        "credit_card": CreditCard,
        "stripe": StripePayment,
    }

    @staticmethod
    def create(payment_type):
        payment_class = PaymentFactory._payments.get(payment_type)

        if payment_class is None:
            raise ValueError(f"Unsupported payment type: {payment_type}")

        return payment_class()