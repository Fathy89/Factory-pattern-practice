from pydantic import BaseModel
from  models.enums.payment_enum import payment_method

class payment_model (BaseModel) : 
    
    payment_type: payment_method
    amount : float 
    