import requests
api_url = 'http://jsonplaceholder.typicode.com/todos'

todos ={
    'userid': 909,
    'id': 909,
    'title': 'Patara Wongsanga',
    'complete': True

}



response = requests.post(api_url, json=todos)


print(response.json())
print(response.status_code)