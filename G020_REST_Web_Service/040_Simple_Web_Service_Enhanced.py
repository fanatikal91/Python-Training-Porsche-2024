from flask import Flask, jsonify

app = Flask(__name__)

# Sample data set: List of users with fixed IDs
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
    {"id": 4, "name": "Diana"},
    {"id": 5, "name": "Eve"}
]

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

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=65065,debug=True)

