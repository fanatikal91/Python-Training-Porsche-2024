import requests

def get_ip():
    url = "https://postman-echo.com/ip"
    
    try:
        # Send GET request
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Extract and print the IP address from the JSON response
            json_data = response.json()
            ip_address = json_data.get("ip")
            print("Your IP Address:", ip_address)
        else:
            print("Failed to retrieve IP address:", response.status_code)
    
    except requests.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    get_ip()
