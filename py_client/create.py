import requests

endpoint = "http://127.0.0.1:8000/api/products/"

get_response = requests.post(endpoint,json={"title":"full efdsfdfnglish","content":"no ddsfdsfata","price":100.00}) 
print(get_response.text)