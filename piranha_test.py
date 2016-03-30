# piranha_test.py - Test script for the Piranha Amazon scraper

import piranha
import csv

def test():
    creds = {}
    with open("credentials/amazonrootkey") as csvfile:
        read = csv.reader(csvfile, delimiter='=')
        for line in read:
            creds[line[0]]=line[1]
    print(creds)
    p = piranha.Piranha(creds['AWSAccessKeyId'],creds['AWSSecretKey'],creds['AssociateId'])        
    while True:
        result = input("What are you looking for?: ")
        print(p.ItemSearch(Keywords=result))
