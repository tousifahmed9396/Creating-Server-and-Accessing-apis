from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Tousif"},
    {"id": 2, "name": "Shameer"}
]


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify({"message": "User added!"}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_data = request.get_json()
    for user in users:
        if user['id'] == user_id:
            user['name'] = updated_data.get('name')
            return jsonify({"message": "User updated!"})
    return jsonify({"error": "User not found"}), 404
    

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": "User deleted!"})

if __name__ == '__main__':
    app.run(debug=True)
