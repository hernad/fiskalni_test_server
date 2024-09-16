import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status, Request
from pydantic import BaseModel
from typing import List
#from fastapi.security import OAuth2PasswordBearer
import json

API_KEY = "0123456789abcdef0123456789abcdef"

app = FastAPI()

@app.get("/")
def root():
    name = "hernad"
    return {"hello": name}



#curl --location 'http://127.0.0.1:3566/api/invoices' \
#--header 'Authorization: Bearer 0123456789abcdef0123456789abcdef' \
#--header 'RequestId: 12345' \
#--header 'Content-Type: application/json' \
#--data '{
#    "invoiceRequest": {
#        "invoiceType": "Normal",
#        "transactionType": "Sale",
#        "payment": [
#            {
#                "amount": 100.00,
#                "paymentType": "Cash"
#            }
#        ],
#        "items": [
#            {
#                "name": "Artikl 1",
#                "labels": [
#                    "F"
#                ],
#                "totalAmount": 100.00,
#                "unitPrice": 50.00,
#                "quantity": 2.000
#            }
#        ],
#        "cashier": "Radnik 1"
#    }
#}'


class PaymentLine(BaseModel):
    amount: float
    paymentType: str


class ItemLine(BaseModel):
    totalAmount: float
    unitPrice: float
    quantity: float


class InvoiceRequest(BaseModel):     
    invoiceType: str
    transactionType: str
    payment: list[PaymentLine] = []
    items: list[ItemLine] = []
    cashier: str

class InvoiceData(BaseModel):
    invoiceRequest: InvoiceRequest


# {
#  "address": "Prvog Krajiškog Korpusa 18",
#  "businessName": "SIRIUS2010 doo Banja Luka",
#  "district": "Banja Luka",
#  "encryptedInternalData": "Vvwq4nVn/wIQ...",
#  "invoiceCounter": "100/138ПП",
#  "invoiceCounterExtension": "ПП",
#  "invoiceImageHtml": null,
#  "invoiceImagePdfBase64": null,
#  "invoiceImagePngBase64": null,
#  "invoiceNumber": "RX4F7Y5L-RX4F7Y5L-138",
#  "journal": "=========== ФИСКАЛНИ РАЧУН ===========\r\n             4402692070009            \r\n       SIRIUS2010 doo Banja Luka      \r\n       SIRIUS2010 doo Banja Luka      \r\n      Prvog Krajiškog Korpusa 18      \r\n              Banja Luka              \r\nКасир:                        Radnik 1\r\nЕСИР број:                      13/2.0\r\n----------- ПРОМЕТ ПРОДАЈА -----------\r\nАртикли                               \r\n======================================\r\nНазив  Цена        Кол.         Укупно\r\nArtikl 1 (F)                          \r\n      50,00       2,000         100,00\r\n--------------------------------------\r\nУкупан износ:                   100,00\r\nГотовина:                       100,00\r\n======================================\r\nОзнака    Назив    Стопа         Порез\r\nF          ECAL      11%          9,91\r\n--------------------------------------\r\nУкупан износ пореза:              9,91\r\n======================================\r\nПФР вријеме:      12.03.2024. 07:47:09\r\nПФР бр.рач:      RX4F7Y5L-RX4F7Y5L-138\r\nБројач рачуна:               100/138ПП\r\n======================================\r\n======== КРАЈ ФИСКАЛНОГ РАЧУНА =======\r\n",
#  "locationName": "SIRIUS2010 doo Banja Luka",
#  "messages": "Успешно",
#  "mrc": "01-0001-WPYB002248000772",
#  "requestedBy": "RX4F7Y5L",
#  "sdcDateTime": "2024-03-12T07:47:09.548+01:00",
#  "signature": "Mw+IB0vgnaMjYrwA7m7zhtRseRIZ...",
#  "signedBy": "RX4F7Y5L",
#  "taxGroupRevision": 2,
#  "taxItems": [
#    {
#      "amount": 9.9099,
#      "categoryName": "ECAL",
#      "categoryType": 0,
#      "label": "F",
#      "rate": 11
#    }
#  ],
#  "tin": "4402692070009",
#  "totalAmount": 100,
#  "totalCounter": 138,
#  "transactionTypeCounter": 100,
#  "verificationQRCode": "R0lGODlhhAGEAf...",
#  "verificationUrl": "https://sandbox.suf.poreskaupravars.org/v/?vl=A1JYNEY3WTVMUlg0....="
#}

class TaxItems(BaseModel):
    amount: float
    categoryName: str
    categoryType: int = 0
    label: str = "F"
    rate: int = 11
    
class InvoiceResponse(BaseModel):
    address: str
    businessName: str
    district: str
    encryptedInternalData: str
    invoiceCounter: str
    invoiceCounterExtension: str
    invoiceImageHtml: str | None = None
    invoiceImagePdfBase64: str | None = None
    invoiceImagePngBase64: str | None = None
    invoiceNumber: str
    journal: str
    locationName: str
    messages: str
    mrc: str
    requestedBy: str
    sdcDateTime: str
    signature: str
    signedBy: str
    taxGroupRevision: int
    taxItems: list[TaxItems] = []    
    tin: str
    totalAmount: float
    totalCounter: int
    transactionTypeCounter: int
    verificationQRCode: str 
    verificationUrl: str 

# https://stackoverflow.com/questions/67307159/what-is-the-actual-use-of-oauth2passwordbearer
# {"access_token": access_token, "token_type":"bearer"}

#def api_token():
#    return
#    '{ "access_token":"%s", "token_type":"bearer"}' % (API_KEY)

@app.post("/api/invoices")
async def invoice(req: Request, invoice_data: InvoiceData):

    # https://github.com/fastapi/fastapi/discussions/9601

    type = invoice_data.invoiceRequest.invoiceType

    items_length = len(invoice_data.invoiceRequest.items)
    payments_length = len(invoice_data.invoiceRequest.payment)
    cashier = invoice_data.invoiceRequest.cashier

    token = req.headers["Authorization"].replace("Bearer ", "").strip()

    if token != API_KEY:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED, detail = "Unauthorized API-KEY %s" % (token)
        )
    else:

        response = InvoiceResponse(
            address = "Ulica 7. Muslimanske brigade 77",
            businessName = "Sigma-com doo Zenica",
            district = "ZEDO",
            encryptedInternalData = "Vvwq4nVn/wIQFAKE",
            invoiceCounter = "100/138ZE",
            invoiceCounterExtension = "ZE",
            invoiceImageHtml = None,
            invoiceImagePdfBase64 = None,
            invoiceImagePngBase64 = None,
            invoiceNumber = "RX4F7Y5L-RX4F7Y5L-138",
            journal = "=========== FAKE RAČUN ===========\r\n             4402692070009            \r\n       SIRIUS2010 doo Banja Luka      \r\n       Sigma-com doo Zenica      \r\n      7. Muslimanske Brigade 77      \r\n              Zenica              \r\nKasir:                        Radnik 1\r\nESIR BROJ:                      13/2.0\r\n----------- PROMET PRODAJA -----------\r\nАrtikli                               \r\n======================================\r\nNaziv  Cijena        Kol.         Ukupno\r\nArtikl 1 (F)                          \r\n      50,00       2,000         100,00\r\n--------------------------------------\r\nUkupan iznos:                   100,00\r\nGotovina:                       100,00\r\n======================================\r\nOznaka    Naziv    Stopa    Porez\r\nF          ECAL      11%          9,91\r\n--------------------------------------\r\nUkupan iznos poreza:              9,91\r\n======================================\r\nПФР вријеме:      12.03.2024. 07:47:09\r\nOFS br. rač:      RX4F7Y5L-RX4F7Y5L-138\r\nBrojač računa:               100/138ZE\r\n======================================\r\n======== KRAJ FISKALNOG RAČUNA =======\r\n",
            locationName = "Sigma-com doo Zenica poslovnica Sarajevo",
            messages = "Uspješno",
            mrc = "01-0001-WPYB002248000772",
            requestedBy = "RX4F7Y5L",
            sdcDateTime = "2024-03-12T07:47:09.548+01:00",
            signature = "Mw+IB0vgnaMjYrwA7m7zhtRseRIZFAKE",
            signedBy = "RX4F7Y5L",
            taxGroupRevision = 2,
            taxItems = [ TaxItems(amount=9.9099, categoryName="ECAL", categoryType = 0, label = "F", rate = 11) ],
            tin = "4402692070009",
            totalAmount = 100.00,
            totalCounter = 138,
            transactionTypeCounter = 100,
            verificationQRCode = "R0lGODlhhAGEAfFAKE",
            verificationUrl = "https://sandbox.suf.poreskaupravars.org/v/?vl=A1JYNEY3WTVMUlg0FAKE="
        )

        return response
 

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, access_log=False, workers=1)
