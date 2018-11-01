#!/usr/bin/python

# Give URL to scrape as command line parameter to this python script
# and it will scrape all of the possible bitcoin WIF private keys from the site
# and test if it is correct private key

from pybitcoin import BitcoinPrivateKey
import requests
import time
import os
import sys
from Utils.privateKeys import checkWIFkeyIsReal
from linkHandler import getLinks

links = getLinks()

if len(links):
    url =  str(sys.argv[1])

    command = 'bash getWIF.sh ' + url
    keys = os.popen(command).read()
    print keys
    if keys is not '0':
        keys = keys.split()
        print "Found: " + str(len(keys)) + " keys from URL: " + url
        if len(keys) > 0:
            print "Testing keys.."
        for key in keys:
            keyData = checkWIFkeyIsReal(key)
            if(keyData):
                print keyData

    else:
        print "Error getting keys with url: " + url
else:
    print "Command line argument missing!"


print("Exiting..")
