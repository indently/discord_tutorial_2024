import json 
import os
from datetime import datetime
 
json_file_path = "news_data_.json"
total_hours = 5



def store_data(data):
   
    # Writing the dictionary to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file)
        
def get_data():
    
    try:
        # Reading data from the JSON file
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"File '{json_file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{json_file_path}'.")
        return None
        
def get_write_time():
    
    # Get the last modification time
    modification_time = os.path.getmtime(json_file_path)

    # Convert the modification time to a readable format
    last_modified_date = datetime.fromtimestamp(modification_time)
    
    return last_modified_date

def time_difference():

    last_modified_date = get_write_time()
    current_date = datetime.today()
    seconds_difference = (current_date - last_modified_date).total_seconds()
    hours_difference = seconds_difference / 3600
    
    return hours_difference

def should_fetch_live_data():
    return time_difference() > total_hours