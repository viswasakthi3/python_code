from contextlib import nullcontext
from typing import List
import requests
import json
from flask import Flask,render_template,request

response = requests.get('https://f8776af4-e760-4c93-97b8-70015f0e00b3.mock.pstmn.io/fruits')
response2 = requests.get('https://f8776af4-e760-4c93-97b8-70015f0e00b3.mock.pstmn.io/vegetables')
response3 = requests.get('https://f8776af4-e760-4c93-97b8-70015f0e00b3.mock.pstmn.io/grains')

    
    
def abc():
    lis=[]
    for data in (response.json()):
        if data['qty'] <= quantity:
            #print(data['name'])
            lis.append(data['name'])

    for data in (response2.json()):
        if data['qty'] <= quantity:
            #print(data['name'])
            lis.append(data['name'])
        
    for data in (response3.json()):
        if data['qty'] <= quatity:
            #print(data['name'])
            lis.append(data['name'])
    if lis==[]:
        print("not found")  
    else:
        print(lis)          
abc()            

             
            
