import requests
api_url = 'http://jsonplaceholder.typicode.com/todos/1'

todos ={
    'userid': 1,
    'id': 1,
    'title': 'Patara Wongsanga',
    'complete': True

}



response = requests.put(api_url, json=todos)


print(response.json())
print(response.status_code)