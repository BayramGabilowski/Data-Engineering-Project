import requests
import json

#random user api call and returns json format data
def random_user(resource,size=10,response_type='json',url=r"https://random-data-api.com/api/v2/,resource"):     
    # Construct the URL with query parameters
    url = f"{url}{resource}?size={size}&response_type={response_type}"
    # Make the req  uest
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
