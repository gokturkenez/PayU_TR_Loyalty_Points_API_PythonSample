'''
Project: PayU Turkey Loyalty Points Python Sample
Author: Göktürk Enez
'''
# Importing required libraries.
from datetime import datetime
import hmac
import hashlib
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# Endpoint
url = "https://secure.payu.com.tr/api/loyalty-points/check"

# PayU Merchant's Secret Key
secret = 'SECRET_KEY'

# Request @params Begin
array = {
    # PayU Merchant's Merchant ID
    'MERCHANT': 'OPU_TEST',
    'CC_OWNER': 'Gokturk Enez',
    'CC_NUMBER': '4355084355084358',
    'EXP_MONTH': '12',
    'EXP_YEAR': '2018',
    'CC_CVV': '000',
    'CURRENCY':'TRY',
    'DATE': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

}

# Initializing the hashstring @param
hashstring = ''

# Sorting Array @params
for k, v in sorted(array.items()):

# Adding the length of each field value at the beginning of field value
    hashstring += str(len(v)) + str(v)
print(hashstring)

# Calculating ORDER_HASH
signature = hmac.new(secret.encode('utf-8'), hashstring.encode('utf-8'), hashlib.md5).hexdigest()

# Adding ORDER_HASH @param to request array
array['HASH'] = signature

print(signature)

# Sending Request to Endpoint
request = Request(url, urlencode(array).encode())
response = urlopen(request).read().decode()

# Printing result/response
print(response)


