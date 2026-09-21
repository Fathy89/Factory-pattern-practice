from fastapi import FastAPI
from routers.payment_routers import router
app= FastAPI()
app.include_router(router)

@app.get("/") 
def home()  :
    return {"message" :"Welcome To my payment Website!"}

