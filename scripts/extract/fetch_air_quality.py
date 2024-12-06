import requests
import json
import os

def fetch_air_quality_data(api_url, save_path="data/raw/air_quality_2024.json"):
    """
    Fetches air quality data from the given API URL and stores it in a JSON file.

    Args:
        api_url (str): The API URL to fetch the data from.
        save_path (str): Path to save the fetched data as a JSON file.

    Returns:
        None
    """
    print("Fetching data from the API...")
    response = requests.get(api_url)
    
    if response.status_code == 200:
        print("Data fetched successfully!")
        data = response.json()
        
        # Ensure the save directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Save data to a JSON file
        with open(save_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        
        print(f"Data saved to {save_path}")
    else:
        print(f"Failed to fetch data: {response.status_code}, {response.text}")

if __name__ == "__main__":
    # Your API link
    api_url = "https://aqs.epa.gov/data/api/dailyData/byCounty?email=sonali.birje2024@gmail.com&key=goldheron12&param=42602,88502,42401,85173,42101&bdate=20240101&edate=20241201&state=06&county=037"
    
    # Call the function to fetch and store data
    fetch_air_quality_data(api_url)
