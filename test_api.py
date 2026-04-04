import requests

BASE_URL = 'http://127.0.0.1:5000/users'

# 1. GET: Retrieve all users
print("--- GET Users ---")
response = requests.get(BASE_URL)
print(response.json())

# 2. POST: Add a new user
print("\n--- POST User ---")
new_user_data = {"id": 3, "name": "Ahmed"}
response = requests.post(BASE_URL, json=new_user_data)
print(response.status_code, response.json())

# Fetch again to verify addition
print("Users after POST:", requests.get(BASE_URL).json())

# 3. PUT: Update an existing user (updating user with ID 3)
print("\n--- PUT User ---")
update_data = {"name": "Ahmed Tousif"}
# Notice we add the user ID to the end of the URL
response = requests.put(f"{BASE_URL}/3", json=update_data) 
print(response.status_code, response.json())

# 4. DELETE: Delete a user (deleting user with ID 1)
print("\n--- DELETE User ---")
response = requests.delete(f"{BASE_URL}/1")
print(response.status_code, response.json())

# Fetch one last time to see the final list
print("\nFinal Users list:", requests.get(BASE_URL).json())
