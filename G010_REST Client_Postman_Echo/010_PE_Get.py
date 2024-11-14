import requests

def get_postman_echo():
    url = "https://postman-echo.com/get?a=87&x=110&y=88"
    
    try:
        # Send GET request
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Print the JSON response
            json_data = response.json()
            print("Response JSON:", json_data)
        else:
            print("Failed to retrieve data:", response.status_code)
    
    except requests.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    get_postman_echo()
