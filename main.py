import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from typing import List
#from fastapi.security import OAuth2PasswordBearer
import json

API_KEY = "0123456789abcdef0123456789abcdef"


PIN = "1234"
GSC_CODE = "9999"   # sve naštimano
#GSC_CODE = "1300"  # bezbjednosni element nije prisutan
#GSC_CODE = "1500"  # PIN se mora unijeti

app = FastAPI()

@app.get("/")
def root():
    name = "hernad"
    return {"hello": name}


def check_api_key(req: Request):

    token = req.headers["Authorization"].replace("Bearer ", "").strip()

    if token != API_KEY:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED, detail = "Unauthorized API-KEY %s" % (token)
        )
        return False

    return True

# dostupan
#curl --location 'http://127.0.0.1:3566/api/attention' \
#--header 'Authorization: Bearer 0123456789abcdef0123456789abcdef'

@app.get("/api/attention")
async def get_attention(req: Request):

    if check_api_key(req):
        return True
    else:
        return None

# settings get
# curl --location 'http://127.0.0.1:3566/api/settings' \
# --header 'Authorization: Bearer 0123456789abcdef0123456789abcdef'

#{
#  "allowedPaymentTypes": [
#    0,
#    1,
#    2,
#    3,
#    4,
#    5,
#    6
#  ],
#  "apiKey": "****",
#  "applicationLanguage": "sr-Cyrl-RS", <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#  "authorizeLocalClients": false,
#  "authorizeRemoteClients": false,
#  "availableDisplayDevices": [],
#  "availableEftPosDevices": [
#    "Internal"
#  ],
#  "availableEftPosProtocols": [
#    "ASoftPos"
#  ],
#  "availablePrinterTypes": [
#    "EscPos"
#  ],
#  "availablePrinters": [
#    "Internal"
#  ],
#  "availableScaleDevices": [],
#  "availableScaleProtocols": [
#    "Aclas PS6X D0",
#    "Apollo",
#    "Birotehna OB1/OP1",
#    "Dialog 06",
#    "Dollar",
#    "Ecr-Posnet",
#    "Tisa"
#  ],
#  "customTabName": null,
#  "customTabUrl": null,
#  "displayDeviceName": null,
#  "displayDeviceRs232BaudRate": null,
#  "displayDeviceRs232DataBits": null,
#  "displayDeviceRs232HardwareFlowControl": null,
#  "displayDeviceRs232Parity": null,
#  "displayDeviceRs232StopBits": null,
#  "displayEnabled": false,
#  "displayHandler": null,
#  "displayProtocol": null,
#  "displayTextCodePage": null,
#  "displayTextCols": null,
#  "displayTextRows": null,
#  "eFakturaApiKey": null,
#  "eFakturaCompanyAddress": null,
#  "eFakturaCompanyBankAccount": null,
#  "eFakturaCompanyCity": null,
#  "eFakturaCompanyEMail": null,
#  "eFakturaCompanyName": null,
#  "eFakturaCompanyPhone": null,
#  "eFakturaCompanyRegistrationId": null,
#  "eFakturaCompanyTaxId": null,
#  "eFakturaTest": true,
#  "eftPosCredentials": null,
#  "eftPosDeviceName": "Test",
#  "eftPosDeviceRs232BaudRate": null,
#  "eftPosDeviceRs232DataBits": null,
#  "eftPosDeviceRs232HardwareFlowControl": null,
#  "eftPosDeviceRs232Parity": null,
#  "eftPosDeviceRs232StopBits": null,
#  "eftPosProtocol": "Test",
#  "issueCopyOnRefund": false,
#  "language": "sr-Cyrl-RS", <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#  "languages": [
#    "sr-RS",  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#    "sr-Cyrl-RS", <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#    "en-US" <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#  ],
#  "lpfr": {
#    "apiKey": "****",
#    "authorizeLocalClients": false,
#    "authorizeRemoteClients": false,
#    "availableSmartCardReaders": [
#      "PSAM"
#    ],
#    "canHaveMultipleSmartCardReaders": false,
#    "externalStorageFolder": null,
#    "languages": [
#      "sr-RS",
#      "sr-Cyrl-RS",
#      "en-US"
#    ],
#    "password": "*****",
#    "smartCardReaderName": null,
#    "username": "admin"
#  },
#  "lpfrUrl": "http://127.0.0.1:3565/api/v3",
#  "paperHeight": null,
#  "paperMargin": null,
#  "paperWidth": null,
#  "posName": null,
#  "printerDpi": null,
#  "printerName": null,
#  "printerType": "EscPos",
#  "qrCodeSize": null,
#  "receiptCustomCommandBegin": null,
#  "receiptCustomCommandEnd": null,
#  "receiptCutPaper": "CutPaper",
#  "receiptDiscountText": null,
#  "receiptFeedLinesBegin": 0,
#  "receiptFeedLinesEnd": 3,
#  "receiptFontSizeLarge": 24,
#  "receiptFontSizeNormal": 19,
#  "receiptFooterImage": null,
#  "receiptFooterTextLines": null,
#  "receiptHeaderImage": null,
#  "receiptHeaderTextLines": null,
#  "receiptLayout": "Slip",
#  "receiptLetterSpacingCondensed": -0.05,
#  "receiptLetterSpacingNormal": 0,
#  "receiptOpenCashDrawer": "None",
#  "receiptSplitMaxHeight": null,
#  "receiptWidth": 386,
#  "receiptsDelay": 5,
#  "runUi": true,
#  "scaleDeviceName": null,
#  "scaleDeviceRs232BaudRate": 9600,
#  "scaleDeviceRs232DataBits": 8,
#  "scaleDeviceRs232HardwareFlowControl": 0,
#  "scaleDeviceRs232Parity": 0,
#  "scaleDeviceRs232StopBits": 1,
#  "scaleProtocol": null,
#  "syncReceipts": true,
#  "vpfrCertificateAddress": null,
#  "vpfrCertificateBusinessName": null,
#  "vpfrCertificateCity": null,
#  "vpfrCertificateCountry": null,
#  "vpfrCertificateSerialNumber": null,
#  "vpfrCertificateShopName": null,
#  "vpfrClientCertificateBase64": null,
#  "vpfrEnabled": false,
#  "vpfrPac": null
#}

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


# curl post settings
#curl --location 'http://127.0.0.1:3566/api/settings' \
#--header 'Authorization: Bearer 0123456789abcdef0123456789abcdef' \
#--header 'Content-Type: application/json' \
#--data '{
#    "authorizeLocalClients": false,
#    "authorizeRemoteClients": true,
#    "apiKey": "c0521663642496c82f79a55725302eba",
#    "webserverAddress": "http://0.0.0.0:3566/"
#}'


#Pre korišćenja ESIR rešenja u produkciji preporučuje se provera i dodatno pojačaju sigurnosna podešavanja preko sledećih parametara:
#
#authorizeLocalClients (boolean) - vrednost true ako je potrebno da lokalni klijenti (aplikacije koje se izvršavaju na istom uređaju kao i ESIR) šalju API KEY uz svaki zahtev odnosno false u suprotnom. Preporuka je da se ovaj parametar podesi na true.
#authorizeRemoteClients (boolean) - vrednost true ako je potrebno da udaljeni klijenti (aplikacije koje se izvršavaju na drugim računarima/uređajima i pristupaju ESIR API-u preko mreže/interneta) šalju API KEY uz svaki zahtev odnosno false u suprotnom. Nikako nije preporučljivo ovaj parametar staviti na false osim ukoliko ste sigurni da ste na drugi način obezbedili kontrolu pristupa Teron ESIR API-ju.
#apiKey (string) - nova vrednost API KEY-a. Preporučuje se da promenite API KEY kako bi ste vi bili jedini koji ga znate.
#webserverAddress (string) - IP adresa i port na kojoj se nalazi API. Ukoliko je dovoljan samo pristup lokalnim klijentima (aplikacijama na samom uređaju) preporuka je da se IP adresa promeni na 127.0.0.1 umesto 0.0.0.0 što će dodatno onemogućiti pristup API-u spolja. Dodatno ovaj poziv se može iskoristiti da se promeni i port na kojem se nalazi API ukoliko je to potrebno. Nakon promene ovog parametra neophodno je restartovati Teron ESIR kako bi se novi parametri primenili.

# WORKFLOW
#1. Proveriti da li su ESIR i PFR dostupni pozivom /api/attention (opisan u "Provera dostupnosti"). Ukoliko je odgovor negativan treba prikazati odgovarajuću poruku korisniku i posle par sekundi pokušati ponovo. Nastaviti ovu proveru bez ograničenja dok ESIR ne postane dostupan.
# while

#2. Samo ako se koristi LPFR: proveriti da li je bezbednosni element prisutan pozivom /api/status (opisan u "Provera statusa") i proverom da li se u spisku statusa u polju gsc nalazi kod 1300. Ukoliko se ovaj kod nalazi onda treba prikazati adekvatnu poruku korisniku da bezbednosni element nije prisutan i nastaviti ovu proveru sve dok se ne izgubi kod 1300.

#3. Samo ako se koristi LPFR: proveriti dali je neophodan unos PIN-a pozivom /api/status i proverom da li se u spisku statusa u polju gsc nalazi kod 1500. 
# Ukoliko se ovaj kod nalazi onda treba prikazati adekvatnan ekran korisniku za unos PIN-a i slanjem istog na /api/pin poziv za proveru (opsian u "Unos PIN-a bezbednosnog elementa"). Nakon uspešno unetog PIN-a se može nastaviti dalje sa radom.

#4. Obaviti standardni unos svih elemenata računa i poslati na fiskalizaciju i štampu pozivom /api/invoices(opisan u "Fiskalizacija računa"). Ukoliko je vraćena greška da bezbednosni element nije prisutan (npr. korisnik je izvukao karticu u međuvremenu) onda se vratiti na korak 2. Ukoliko je vraćena greška da je neophodan unos PIN-a (npr. korisnik je izvukao i vratio istu ili drugu karticu) onda se vratiti na korak 3. U suprotnom ovaj API će vratiti grešku ukoliko postoji problem u sadržaju računa (koji treba prikazati korisniku adekvatno na ekranu) ili odgovor da je fiskalizacija i štampa uspešno obavljena u kom slučaju se može pristupiti unosom novog računa od koraka 2. U slučaju da je vraćena greška ona može biti geška pre fiskalizacije ili greška nakon fiskalizacije ali pre štampanja računa. U slučaju da je fiskalizacija obavljena ali je greška nastala prilikom štampe računa odgovor će pored informacija o grešci sadržati i polje invoiceResponse u kom slučaju je potrebno ispraviti grešku sa štampačem (npr. ukoliko nema papira) a potom ponoviti isti poziv ali uključiti i invoiceResponse polje što je signal Teron ESIR API-u da ne radi ponovo fiskalizaciju već samo da pokuša štampu ponovo.



#curl --location 'http://127.0.0.1:3566/api/pin' \
#--header 'Authorization: Bearer 0123456789abcdef0123456789abcdef' \
#--header 'Content-Type: text/plain' \ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ne JSON
#--data '1234'

#POST
#Unos PIN-a bezbednosnog elementa
#http://127.0.0.1:3566/api/pin
#Namena ovog poziva je da otključa bezbednosni element za potrebe fiskalizacije unosom PIN koda. 
# PIN kod se prosleđuje u zahtevu dok odgovor sadrži status kod operacije a pored status koda 
# ukoliko je operacija uspešna odgovor sadrži HTTP 200 OK status dok u svim ostalim slučajevima 
# vraća status HTTP 4xx ili HTTP 5xx. Mogući numerički status kodovi u odgovoru su:
#
#0100 - PIN je ispravno unet
#1300 - Bezbednosni element nije prisutan
#2400 - LPFR nije spreman
#2800 - Pogrešan format PIN-a (očekivano 4 cifre)
#2806 - Pogrešan format PIN-a (očekivano 4 cifre)
#Napomena: zbog uniformnosti sa LPFR API-jima koje je propisao PURS, 
# ovo je jedini API poziv koji na ulazu prihvata čist tekst (Content-type: text/plain).

#response
#"0100"

@app.post("/api/pin", response_class=PlainTextResponse)
async def post_pin(req: Request):
   
   if not check_api_key(req):
       return False
    
   body = (await req.body()).decode('utf-8')
   response = "2400"
   if body == PIN:
       response = "0100"
   elif len(body) != 4:
       response = "2800"

   return response


class TaxRate(BaseModel):
    label: str
    rate: int

class TaxCategory(BaseModel):
    categoryType: int
    name: str
    orderId: int
    taxRates: list[TaxRate] = []
     

class TaxRates(BaseModel):
   groupId: str
   taxCategories: list[TaxCategory] = []
   validFrom: str
    
class Status(BaseModel):
   allTaxRates:  list[TaxRates] = [] 
   currentTaxRates: list[TaxRates] = []
   deviceSerialNumber: str
   gsc: list[str] = []
   hardwareVersion: str
   lastInvoiceNumber: str
   make: str 
   model: str
   mssc:  list[str] = []
   protocolVersion: str
   sdcDateTime: str
   softwareVersion: str
   supportedLanguages: list[str] = []


# 
#curl --location 'http://127.0.0.1:3566/api/status' \
#--header 'Authorization: Bearer 0123456789abcdef0123456789abcdef'

#Ovaj poziv vraća status sistema za fiskalizaciju (LPFR ili VPFR u zavisnosti od podešavanja). 
# Glavna polja u odgovoru od interesa za integraciju sa ESIR-om su:

#sdcDateTime (timestamp) - trenutno vreme na PFR-u
#gsc: (list of string) - niz status LPFR-a. Za spisak svih statusa konsultovati PURS dokumentaciju za LPFR, glavni statusi su opisani i prethodnoj sekciji u okviru opisa niza koraka prilikom fiskalizacije računa. Ovo polje ne postoji u slučaju korišćenja VPFR-a
#uid (string) - UID bezbednosnog elementa (LPFR, ukoliko je ubačen) odnosno sertifikata (VPFR)

@app.get("/api/status")
async def get_status(req: Request):

    if not check_api_key(req):
        return False
    
    taxRate0 = TaxRate( rate = 0, label = "G")
    taxRateA = TaxRate( rate = 0, label = "A")
    taxRateE = TaxRate( rate = 10, label = "E")
    taxRateD = TaxRate( rate = 20, label = "D")

    taxCategory1 = TaxCategory(categoryType=0, name="Bez PDV", orderId=4, taxRates=[taxRate0])
    taxCategory2 = TaxCategory(categoryType=0, name="Nije u PDV", orderId=1, taxRates=[taxRateA])
    taxCategory3 = TaxCategory(categoryType=6, name="P-PDV", orderId=3, taxRates=[taxRateE])
    taxCategory4 = TaxCategory(categoryType=6, name="D-PDV", orderId=3, taxRates=[taxRateD])

    allTaxRates = [
        TaxRates(
            groupId="1",
            taxCategories=[
                taxCategory1
            ],
            validFrom="2021-11-01T02:00:00.000+01:00"
        ),
        TaxRates(
            groupId="6",
            taxCategories=[
                taxCategory2,
                taxCategory3,
                taxCategory4
            ],
            validFrom=""
        )
    ]

    currentTaxRates = [
        TaxRates(
            groupId="6",
            taxCategories=[
                taxCategory2,
                taxCategory3,
                taxCategory4
            ],
            validFrom = "2021-11-01T02:00:00.000+01:00"
        )
    ]
    
    response = Status(
        allTaxRates=allTaxRates,
        currentTaxRates=currentTaxRates,
        deviceSerialNumber = "01-0001-WPYB002248000772",
        gsc = [
         GSC_CODE,
         "0210"
        ],
        hardwareVersion = "1.0",
        lastInvoiceNumber = "RX4F7Y5L-RX4F7Y5L-132",
        make ="OFS",
        model = "OFS P5 EFU LPFR",
        mssc = [],
        protocolVersion = "2.0",
        sdcDateTime = "2024-03-11T23:03:24.390+01:00",
        softwareVersion = "2.0",
        supportedLanguages = [
         "bs-BA",
         "bs-Cyrl",
         "en-US"
        ]
    )

    return response
    

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



@app.post("/api/invoices")
async def invoice(req: Request, invoice_data: InvoiceData):

    # https://github.com/fastapi/fastapi/discussions/9601

    type = invoice_data.invoiceRequest.invoiceType

    items_length = len(invoice_data.invoiceRequest.items)
    payments_length = len(invoice_data.invoiceRequest.payment)
    cashier = invoice_data.invoiceRequest.cashier

    
    if check_api_key(req):

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
    else:
        return None
 

#curl --location 'http://127.0.0.1:3566/api/invoices/search' \
#--header 'Authorization: Bearer 0123456789abcdef0123456789abcdef' \
#--header 'Content-Type: application/json' \
#--data '{
#    "fromDate": "2024-03-01",
#    "toDate": "2024-03-31",
#    "amountFrom": 10.00,
#    "amountTo": 10000.00,
#    "invoiceTypes": ["Normal","Advance"],
#    "transactionTypes": ["Sale","Refund"],
#    "paymentTypes": ["Cash","WireTransfer"]
#}' 


#RX4F7Y5L-RX4F7Y5L-1,Normal,Sale,2024-03-06T17:33:12.582+01:00,10.0000
#RX4F7Y5L-RX4F7Y5L-131,Normal,Sale,2024-03-11T20:29:05.329+01:00,10.0000
#RX4F7Y5L-RX4F7Y5L-132,Normal,Sale,2024-03-11T20:29:25.422+01:00,15.0000
#RX4F7Y5L-RX4F7Y5L-133,Normal,Sale,2024-03-11T23:05:53.608+01:00,100.0000
#RX4F7Y5L-RX4F7Y5L-134,Normal,Sale,2024-03-11T23:13:55.829+01:00,100.0000
#RX4F7Y5L-RX4F7Y5L-135,Normal,Sale,2024-03-11T23:16:03.098+01:00,300.0000
#RX4F7Y5L-RX4F7Y5L-137,Normal,Refund,2024-03-11T23:19:54.853+01:00,100.0000
#RX4F7Y5L-RX4F7Y5L-138,Normal,Sale,2024-03-12T07:47:09.548+01:00,100.0000
#RX4F7Y5L-RX4F7Y5L-139,Normal,Sale,2024-03-12T07:47:38.530+01:00,100.0000
#RX4F7Y5L-RX4F7Y5L-140,Normal,Sale,2024-03-12T07:48:47.626+01:00,300.0000
#RX4F7Y5L-RX4F7Y5L-142,Normal,Refund,2024-03-12T07:50:19.735+01:00,100.0000
#RX4F7Y5L-RX4F7Y5L-143,Advance,Sale,2024-03-12T07:51:53.207+01:00,100.0000
#RX4F7Y5L-RX4F7Y5L-144,Advance,Sale,2024-03-12T07:53:26.177+01:00,400.0000
#RX4F7Y5L-RX4F7Y5L-145,Advance,Refund,2024-03-12T07:55:07.582+01:00,500.0000
#RX4F7Y5L-RX4F7Y5L-146,Normal,Sale,2024-03-12T07:55:09.365+01:00,1000.0000
#RX4F7Y5L-RX4F7Y5L-147,Advance,Sale,2024-03-12T07:56:07.043+01:00,100.0000
#RX4F7Y5L-RX4F7Y5L-148,Advance,Sale,2024-03-12T07:57:16.884+01:00,400.0000
#RX4F7Y5L-RX4F7Y5L-149,Advance,Refund,2024-03-12T07:59:21.414+01:00,500.0000
#RX4F7Y5L-RX4F7Y5L-150,Normal,Sale,2024-03-12T08:03:39.781+01:00,1000.0000
#RX4F7Y5L-RX4F7Y5L-151,Advance,Sale,2024-03-12T08:05:12.753+01:00,100.0000


# kopija računa

#curl --location 'http://127.0.0.1:3566/api/invoices' \
#--header 'Authorization: Bearer 0123456789abcdef0123456789abcdef' \
#--header 'RequestId: 12345' \
#--header 'Content-Type: application/json' \
#--data '{
#    "invoiceRequest": {
#        "invoiceType": "Copy",                 <<<<<<<<<<<<<<<<<<<<<<<<<<<
#        "transactionType": "Sale",           <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#        "referentDocumentNumber": "RX4F7Y5L-RX4F7Y5L-140", <<<<<<<<<<<<<<<
#        "referentDocumentDT": "2024-03-12T07:48:47.626+01:00", <<<<<<<<<<<<
#        "payment": [
#            {
#                "amount": 100.00,
#                "paymentType": "Cash"
#            },
#            {
#                "amount": 200.00,
#                "paymentType": "Card"
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
#            },
#            {
#                "name": "Artikl 2",
#                "labels": [
#                    "F"
#                ],
#                "totalAmount": 200.00,
#                "unitPrice": 200.00,
#                "quantity": 1.000
#            }
#        ],
#        "cashier": "Radnik 1"
#    }
#}'

# response kopija računa
#{
#  "address": "Prvog Krajiškog Korpusa 18",
#  "businessName": "SIRIUS2010 doo Banja Luka",
#  "district": "Banja Luka",
#  "encryptedInternalData": "DyCdfR/iSM9miXAK3h0YU89roRF4wRjYl1mYfz....",
#  "invoiceCounter": "6/141КП",
#  "invoiceCounterExtension": "КП",
#  "invoiceImageHtml": null,
#  "invoiceImagePdfBase64": null,
#  "invoiceImagePngBase64": null,
#  "invoiceNumber": "RX4F7Y5L-RX4F7Y5L-141",
#  "journal": "======= ОВО НИЈЕ ФИСКАЛНИ РАЧУН ======\r\n             4402692070009            \r\n       SIRIUS2010 doo Banja Luka      \r\n       SIRIUS2010 doo Banja Luka      \r\n      Prvog Krajiškog Korpusa 18      \r\n              Banja Luka              \r\nРеф. број:       RX4F7Y5L-RX4F7Y5L-140\r\nРеф. вријеме:     12.03.2024. 07:48:47\r\nКасир:                        Radnik 1\r\nЕСИР број:                      13/2.0\r\n----------- КОПИЈА ПРОДАЈА -----------\r\nАртикли                               \r\n======================================\r\nНазив  Цена        Кол.         Укупно\r\nArtikl 1 (F)                          \r\n      50,00       2,000         100,00\r\nArtikl 2 (F)                          \r\n     200,00       1,000         200,00\r\n--------------------------------------\r\nУкупан износ:                   300,00\r\nГотовина:                       100,00\r\nПлатна картица:                 200,00\r\n======================================\r\n======= ОВО НИЈЕ ФИСКАЛНИ РАЧУН ======\r\n======================================\r\nОзнака    Назив    Стопа         Порез\r\nF          ECAL      11%         29,73\r\n--------------------------------------\r\nУкупан износ пореза:             29,73\r\n======================================\r\nПФР вријеме:      12.03.2024. 07:49:43\r\nПФР бр.рач:      RX4F7Y5L-RX4F7Y5L-141\r\nБројач рачуна:                 6/141КП\r\n======================================\r\n======= ОВО НИЈЕ ФИСКАЛНИ РАЧУН ======\r\n",
#  "locationName": "SIRIUS2010 doo Banja Luka",
#  "messages": "Успешно",
#  "mrc": "01-0001-WPYB002248000772",
#  "requestedBy": "RX4F7Y5L",
#  "sdcDateTime": "2024-03-12T07:49:43.171+01:00",
#  "signature": "Zfeew71z6wpGGTXK2w....",
#  "signedBy": "RX4F7Y5L",
#  "taxGroupRevision": 2,
#  "taxItems": [
#    {
#      "amount": 29.7297,
#      "categoryName": "ECAL",
#      "categoryType": 0,
#      "label": "F",
#      "rate": 11
#    }
#  ],
#  "tin": "4402692070009",
#  "totalAmount": 300,
#  "totalCounter": 141,
#  "transactionTypeCounter": 6,
#  "verificationQRCode": "R0lGODlhhAG....",
#  "verificationUrl": "https://sandbox.suf.poreskaupravars.org/v/?vl=A1JYNEY3WTV...="
#}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, access_log=False, workers=1)
