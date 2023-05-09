import sys
import os
import this
from twocaptcha import TwoCaptcha

def solveRecaptcha(site_key, site_url):

    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=site_key,
            url=site_url)

    except Exception as e:
        print(e)

    else:
        return result