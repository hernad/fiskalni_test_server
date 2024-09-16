import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status, Request
from pydantic import BaseModel
#from fastapi.security import OAuth2PasswordBearer
import json

API_KEY = "0123456789abcdef0123456789abcdef"

app = FastAPI()

@app.get("/")
def root():
    name = "hernad"
    return {"hello": name}

# CURL *curl;
#CURLcode res;
#curl = curl_easy_init();
#if(curl) {
#  curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "POST");
#  curl_easy_setopt(curl, CURLOPT_URL, "http://127.0.0.1:3566/api/invoices");
#  curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
#  curl_easy_setopt(curl, CURLOPT_DEFAULT_PROTOCOL, "https");
#  struct curl_slist *headers = NULL;
#  headers = curl_slist_append(headers, "Authorization: Bearer 0123456789abcdef0123456789abcdef");
#  headers = curl_slist_append(headers, "RequestId: 12345");
#  headers = curl_slist_append(headers, "Content-Type: application/json");
#  curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
#  const char *data = "{\n    \"invoiceRequest\": {\n        \"invoiceType\": \"Normal\",\n        \"transactionType\": \"Sale\",\n        \"payment\": [\n            {\n                \"amount\": 100.00,\n                \"paymentType\": \"Cash\"\n            }\n        ],\n        \"items\": [\n            {\n                \"name\": \"Artikl 1\",\n                \"labels\": [\n                    \"F\"\n                ],\n                \"totalAmount\": 100.00,\n                \"unitPrice\": 50.00,\n                \"quantity\": 2.000\n            }\n        ],\n        \"cashier\": \"Radnik 1\"\n    }\n}";
#  curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
#  res = curl_easy_perform(curl);
#}
#curl_easy_cleanup(curl);

class Invoice(BaseModel):
    invoiceRequest: int
    invoiceType: str

# https://stackoverflow.com/questions/67307159/what-is-the-actual-use-of-oauth2passwordbearer
# {"access_token": access_token, "token_type":"bearer"}

#def api_token():
#    return
#    '{ "access_token":"%s", "token_type":"bearer"}' % (API_KEY)

@app.post("/api/invoices")
async def invoice(req: Request, invoice_data: Invoice):

    # https://github.com/fastapi/fastapi/discussions/9601

    request = invoice_data.invoiceRequest
    type = invoice_data.invoiceType
    token = req.headers["Authorization"].replace("Bearer ", "").strip()

    if token != API_KEY:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized API-KEY %s" % (token)
        )
    else:
        return {
            "msg": "SVE_JE_OK",
            "token": token,
            "invoiceRequest": request,
            "invoiceType": type,
        }
 

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, access_log=False, workers=1)
