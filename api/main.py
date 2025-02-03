from schemas import ImeiRequest
from fastapi import FastAPI

from imei_request import imei_request


app = FastAPI()


@app.post('api/check-imei')
def check_imei(data: ImeiRequest):

    response = imei_request(data.imei, data.token)
    return response
