from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data set: Array of user names
users = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# Route to get all users
@app.route('/api/users', methods=['GET'])
def get_all_users():
    return jsonify({"users": users})

# Route to get a user by ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    if 0 <= user_id < len(users):
        return jsonify({"user": users[user_id]})
    else:
        return jsonify({"error": "User ID not found"}), 404

# Route to create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    # Get the new user name from the request data
    data = request.json
    user_name = data.get("name")
    
    if user_name:
        users.append(user_name)  # Add the new user to the list
        return jsonify({"message": "User created", "user": user_name}), 201
    else:
        return jsonify({"error": "Name is required"}), 400

# Route to update an existing user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if 0 <= user_id < len(users):
        data = request.json
        new_name = data.get("name")
        
        if new_name:
            users[user_id] = new_name  # Update the user name
            return jsonify({"message": "User updated", "user": new_name})
        else:
            return jsonify({"error": "Name is required"}), 400
    else:
        return jsonify({"error": "User ID not found"}), 404

# Route to delete a user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if 0 <= user_id < len(users):
        deleted_user = users.pop(user_id)  # Remove the user by ID
        return jsonify({"message": "User deleted", "user": deleted_user})
    else:
        return jsonify({"error": "User ID not found"}), 404

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=65065,debug=True)
