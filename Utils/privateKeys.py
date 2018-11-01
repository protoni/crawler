from pybitcoin import BitcoinPrivateKey
import requests
import time

#priv = "5Kb8kLf9zgWQnogidDA76MzPL6TsZZY36hWXMssSzNydYXYB9KF"
priv = "5Km2kuu7vtFDPpxywn4u3NLu8iSdrqhxWT8tUKjeEXs2fDqZ9iN"

# 
def checkWIFkeyIsReal(priv):
    try:
        p = BitcoinPrivateKey(priv)
        pub = p.public_key().address()
        r = requests.get("https://blockchain.info/rawaddr/{}".format(pub))
        time.sleep(1)

        return r

        '''
        print "{} {} {:20} {:20} {:20} ".format(priv, pub,
            r.json()['final_balance'],
            r.json()['total_received'],
            r.json()['total_sent'])
        '''
    except (AssertionError, IndexError):
        return 0

