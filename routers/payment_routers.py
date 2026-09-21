from fastapi import APIRouter 
from services.payment_service import PaymentService 
from models.payment_models import payment_model
router=APIRouter()


@router.post("/payments/deposite/{name}")
def deposite(name: str, payment_method: payment_model):
    service = PaymentService(payment_method, name)

    return service.deposite()

@router.post("/payments/withdraw/{name}")
def withdraw(name: str, payment_method: payment_model):

    service = PaymentService(payment_method, name)

    return service.withdraw()
