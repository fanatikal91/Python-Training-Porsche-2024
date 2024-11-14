from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial list of users with fixed IDs
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
    {"id": 4, "name": "Diana"},
    {"id": 5, "name": "Eve"}
]

# Function to generate a new unique ID
def generate_new_id():
    if users:
        return max(user["id"] for user in users) + 1
    else:
        return 1

# Route to get all users
@app.route('/api/users', methods=['GET'])
def get_all_users():
    return jsonify({"users": users})

# Route to get a user by ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User ID not found"}), 404

# Route to create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    user_name = data.get("name")
    
    if user_name:
        new_user = {"id": generate_new_id(), "name": user_name}
        users.append(new_user)
        return jsonify({"message": "User created", "user": new_user}), 201
    else:
        return jsonify({"error": "Name is required"}), 400

# Route to update an existing user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        data = request.json
        new_name = data.get("name")
        
        if new_name:
            user["name"] = new_name
            return jsonify({"message": "User updated", "user": user})
        else:
            return jsonify({"error": "Name is required"}), 400
    else:
        return jsonify({"error": "User ID not found"}), 404

# Route to delete a user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    
    if user:
        users = [u for u in users if u["id"] != user_id]
        return jsonify({"message": "User deleted", "user": user})
    else:
        return jsonify({"error": "User ID not found"}), 404

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=65065,debug=True)

