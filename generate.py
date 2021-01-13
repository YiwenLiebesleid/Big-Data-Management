import random
import string
import json
from collections import defaultdict

CUSTNUM = 500001
# TRANSNUM = 5000001

cust = defaultdict(dict)
for i in range(1,CUSTNUM):
	tempdic = dict()
	tempdic['ID'] = i
	tempdic['Name'] = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',random.randint(10,20)))
	tempdic['Age'] = random.randint(10,70)
	tempdic['Gender'] = ''.join(random.sample(['male','female'],1))
	tempdic['CountryCode'] = random.randint(1,10)
	tempdic['Salary'] = 9900 * random.random() + 100
	cust[i] = tempdic

with open('Customer.json', 'w') as output:
	json.dump(cust, output)
