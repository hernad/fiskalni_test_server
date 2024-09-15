import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    name = "hernad"
    return {"hello": name}


class Invoice(BaseModel):
    id: int
    name: str

@app.post("/invoice")
async def invoice(invoice_data: Invoice):
    id = invoice_data.id
    name = invoice_data.name
    return {
        "msg": "SVE_JE_OK",
        "id": id,
        "name": name,
    }
 

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, access_log=False, workers=2)