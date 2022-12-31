from urllib import response
import requests
import json
a = requests.get('https://f8776af4-e760-4c93-97b8-70015f0e00b3.mock.pstmn.io/fruits')
lis=[]
n=8
for data in (a.json()):
            if data['qty'] >= int(n):
                lis.append(data['name'])
                print(lis)


