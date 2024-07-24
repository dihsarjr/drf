import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint,json={"title":"full english","content":"no data","price":100.00}) 
print(get_response.text)