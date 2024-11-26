from flask import Flask, jsonify

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
    # Check if the user_id is within the valid range
    if 0 <= user_id < len(users):
        return jsonify({"user": users[user_id]})
    else:
        # Return an error if the user ID is not found
        return jsonify({"error": "User ID not found"}), 404

# Route to delete a user by ID
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    # Check if the user_id is within the valid range
    if 0 <= user_id < len(users):
        deleted_user = users.pop(user_id)
        return jsonify({"message": "User deleted", "deleted_user": deleted_user}), 200
    else:
        # Return an error if the user ID is not found
        return jsonify({"error": "User ID not found"}), 404


# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=65065,debug=True)
