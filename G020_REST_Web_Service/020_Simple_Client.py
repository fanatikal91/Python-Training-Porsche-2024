import requests

def get_user_by_id(user_id):
    url = f"http://127.0.0.1:65065/api/users/{user_id}"
    
    try:
        response = requests.get(url)
        
        # Check if the response was successful
        if response.status_code == 200:
            user_data = response.json()
            print("User Name:", user_data["user"])
        elif response.status_code == 404:
            print("Error:", response.json()["error"])
        else:
            print("Unexpected error occurred:", response.status_code)
    
    except requests.RequestException as e:
        print("An error occurred while connecting to the server:", e)

def main():
    print("Enter a user ID to retrieve the name. Enter -1 to quit.")
    
    while True:
        try:
            user_id = int(input("Enter User ID: "))
            
            if user_id == -1:
                print("Exiting the client.")
                break
            
            # Call the function to get user data by ID
            get_user_by_id(user_id)
        
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
