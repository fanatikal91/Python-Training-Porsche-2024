import requests

def get_current_time():
    url = "https://postman-echo.com/time/now"
    
    try:
        # Send GET request
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Extract and print the current time -- no JSON!!
            current_time = response.content
            print("Current Time:", current_time)
        else:
            print("Failed to retrieve current time:", response.status_code)
    
    except requests.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    get_current_time()
