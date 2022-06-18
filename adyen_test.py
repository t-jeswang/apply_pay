import Adyen
import json
import uuid
def get_adyen_client_key():
    return "test_DT7EVPYLGNDHXI3QUMU63DAQNYIO45DI"
def get_adyen_hmac_key():
  return "89347796AC5FDEC4866BEBACDA5D07DF074BCCD102D9A4BE1D5A7F8F6E77FC65"
def adyen_sessions(host_url):
    
    ady = Adyen.Adyen()
    ady.payment.client.xapikey ="AQEnhmfuXNWTK0Qc+iSdm2cqqPeUTp8YXMpA6r4K0do+R+AIcN9JO7uMEMFdWw2+5HzctViMSCJMYAc=-U5i1IxiMBCMIe5ePGx4YhXR/bmZ2DpZsj7769NUKSYw=-+64Ier)A#{@Ta9,m"
    ady.payment.client.merchant_account = "Microsoft519_000001_TEST"
    ady.payment.client.platform = "test" # change to live for production
    ady.payment.client.hmac = "89347796AC5FDEC4866BEBACDA5D07DF074BCCD102D9A4BE1D5A7F8F6E77FC65"


    request = {}

    request['amount'] = {"value": "100", "currency": "USD"}  
    request['reference'] = f"Reference {uuid.uuid4()}"  # provide your unique payment reference
    # universally unique identifier
    # set redirect URL required for some payment methods
    request['returnUrl'] = f"{host_url}/redirect?shopperOrder=myRef"
    request['countryCode'] = "US"

    result = ady.checkout.sessions(request)
    
    formatted_response = json.dumps((json.loads(result.raw_response)))
    # print("/sessions response:\n" + formatted_response)

    return formatted_response, result.status_code

def adyen_apple_checkout(host_url):
    session = json.loads(adyen_sessions(host_url))
    if session == {}: return {}
    ady = Adyen.Adyen()
    ady.payment.client.xapikey = get_adyen_client_key()
    ady.payment.client.merchant_account = "Microsoft519_000001_TEST"
    ady.payment.client.platform = "test" # change to live for production
    ady.payment.client.hmac = "89347796AC5FDEC4866BEBACDA5D07DF074BCCD102D9A4BE1D5A7F8F6E77FC65"
    request = {}
    request['reference'] = f"Reference {uuid.uuid4()}"

    request['amount'] = {"value": "10", "currency": "USD"}  


    request['returnUrl'] = f"{host_url}/redirect?shopperOrder=myRef"
    request['countryCode'] = "US"

    request['sdkVersion'] = '5.16.0'

    
    # request['card'] = {
    #   'number': '6011000994462780',
    #   'expiryMonth': '11',
    #   'expiryYear': '2022',
    #   'cvc': '111',
    #   'holderName': 'alice'
    # }
    #     request['session'] = {'id':session['id'],
    #  'sessionData': session['sessionData'] }
    # request['environment'] = 'test'
    # request['clientKey'] = get_adyen_client_key()
   
      
    checkout = ady.checkout.payment_session(request)
    

    print(checkout.status_code)
    formatted_response = json.dumps((json.loads(checkout.raw_response)))
    print("/sessions response:\n" + formatted_response)

    return formatted_response, checkout.status_code