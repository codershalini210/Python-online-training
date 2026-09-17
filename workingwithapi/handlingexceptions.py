import requests
url = "https://jsonplaceholder.typicode.com/posts/"
try:
    params = {"id":1}
    response = requests.get(url,params,timeout=10)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.Timeout  :
    print("exception : request timeout")
except requests.exceptions.HTTPError :
    print("exception HTTP Err occured")
except requests.exceptions.RequestException :
    print("exception request failed")
except Exception as e:
    print(e)