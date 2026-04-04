import requests

BASE_URL = 'http://127.0.0.1:5000/users'

# GET
print("--- GET Users ---")
response = requests.get(BASE_URL)
print(response.json())

# POST
print("\n--- POST User ---")
new_user_data = {"id": 3, "name": "Ahmed"}
response = requests.post(BASE_URL, json=new_user_data)
print(response.status_code, response.json())

print("Users after POST:", requests.get(BASE_URL).json())

# PUT
print("\n--- PUT User ---")
update_data = {"name": "Ahmed Tousif"}
# Notice we add the user ID to the end of the URL
response = requests.put(f"{BASE_URL}/3", json=update_data) 
print(response.status_code, response.json())

# DELETE
print("\n--- DELETE User ---")
response = requests.delete(f"{BASE_URL}/1")
print(response.status_code, response.json())

# final list
print("\nFinal Users list:", requests.get(BASE_URL).json())
