import Adyen
import json


def adyen_sessions(host_url):
    
    ady = Adyen.Adyen()
    ady.payment.client.xapikey = "AQEnhmfuXNWTK0Qc+iSdm2cqqPeUTp8YXMpA6r4K0do+R+AIcN9JO7uMEMFdWw2+5HzctViMSCJMYAc=-5sHWLSXqKKvKQbMhmcmiS9t4sQedfk0pYgSn+GvJqR0=-UI8,wCV2fgft>.32"
    ady.payment.client.merchant_account = "Microsoft519_000001_TEST"
    ady.payment.client.platform = "test" # change to live for production
    ady.payment.client.hmac = "89347796AC5FDEC4866BEBACDA5D07DF074BCCD102D9A4BE1D5A7F8F6E77FC65"


    request = {}

    request['amount'] = {"value": "1000", "currency": "EUR"}
    # request['reference'] = f"Reference {uuid.uuid4()}"  # provide your unique payment reference
    # set redirect URL required for some payment methods
    request['returnUrl'] = f"{host_url}/redirect?shopperOrder=myRef"
    request['countryCode'] = "NL"

    result = ady.checkout.sessions(request)

    formatted_response = json.dumps((json.loads(result.raw_response)))
    print("/sessions response:\n" + formatted_response)

    return formatted_response