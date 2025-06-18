import requests

params = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
print(requests)
r = requests.get('https://httpbin.org/get', params = params)
p = requests.post('https://httpbin.org/post', data = params)
print(r)
if r.status_code == 200:
    print("Request was successful!")
    print("Response content:", r.text[:100])  # Print the first 100 characters of the response content
    print("Response content:", p.text[:100])  # Print the first 100 characters of the response content