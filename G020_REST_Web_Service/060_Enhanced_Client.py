import requests

BASE_URL = "http://127.0.0.1:65065/api/users"

def get_all_users():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("All Users:", response.json())
    else:
        print("Failed to retrieve users:", response.status_code)

def get_user_by_id(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    if response.status_code == 200:
        print("User:", response.json())
    elif response.status_code == 404:
        print("Error:", response.json()["error"])
    else:
        print("Unexpected error:", response.status_code)

def create_user(name):
    response = requests.post(BASE_URL, json={"name": name})
    if response.status_code == 201:
        print("User Created:", response.json())
    elif response.status_code == 400:
        print("Error:", response.json()["error"])
    else:
        print("Unexpected error:", response.status_code)

def update_user(user_id, name):
    response = requests.put(f"{BASE_URL}/{user_id}", json={"name": name})
    if response.status_code == 200:
        print("User Updated:", response.json())
    elif response.status_code == 404:
        print("Error:", response.json()["error"])
    elif response.status_code == 400:
        print("Error:", response.json()["error"])
    else:
        print("Unexpected error:", response.status_code)

def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
    if response.status_code == 200:
        print("User Deleted:", response.json())
    elif response.status_code == 404:
        print("Error:", response.json()["error"])
    else:
        print("Unexpected error:", response.status_code)

def main():
    print("Enhanced Client for User Management Service")
    print("Commands:")
    print("  1 - Get all users")
    print("  2 - Get a user by ID")
    print("  3 - Create a new user")
    print("  4 - Update an existing user")
    print("  5 - Delete a user")
    print("  6 - Exit")

    while True:
        try:
            command = int(input("\nEnter command: "))
            
            if command == 1:
                get_all_users()
            elif command == 2:
                user_id = int(input("Enter User ID: "))
                get_user_by_id(user_id)
            elif command == 3:
                name = input("Enter User Name: ")
                create_user(name)
            elif command == 4:
                user_id = int(input("Enter User ID to update: "))
                name = input("Enter new name: ")
                update_user(user_id, name)
            elif command == 5:
                user_id = int(input("Enter User ID to delete: "))
                delete_user(user_id)
            elif command == 6:
                print("Exiting the client.")
                break
            else:
                print("Invalid command. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
