"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The phone number to send the verification code to
    "number": "+12106100045",

    # ISO 2-letter country code, assume numbers are based in this country. If not set numbers are
    # assumed to be in international format (with or without the leading + sign)
    "country_code": "",

    # Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA
    # methods. If not set then we will generate a secure random code
    "security_code": "",

    # The language to playback the verification code in, available languages are:
    # • de - German
    # • en - English
    # • es - Spanish
    # • fr - French
    # • it - Italian
    # • pt - Portuguese
    # • ru - Russian
    "language_code": "en",

    # The number of digits to use in the security code (between 4 and 12)
    "code_length": "6",

    # Limit the total number of calls allowed to the supplied phone number, if the limit is reached
    # within the TTL then error code 14 will be returned
    "limit": "3",

    # The delay in milliseconds between the playback of each security code
    "playback_delay": "800",

    # Set the TTL in number of days that the 'limit' option will remember a phone number (the default is
    # 1 day and the maximum is 365 days)
    "limit_ttl": "1"
}
response = client.phone_verify(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # True if the call is being made now
    print("calling:", data.get("calling"))

    # True if this a valid phone number
    print("number-valid:", data.get("number-valid"))

    # The security code generated, you can save this code to perform your own verification or you can
    # use the Verify Security Code API
    print("security-code:", "'{0}'".format(data.get("security-code")))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)
