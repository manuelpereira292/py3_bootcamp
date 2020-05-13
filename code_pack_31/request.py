import requests

url= 'http://127.0.0.1:5000/api/predict'

r = requests.post(url, json={'rate':4, 'sales_1smonth': 300, 'sales_2month':500})

print (r.json())

