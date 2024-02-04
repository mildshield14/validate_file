import os
from bs4 import BeautifulSoup
import requests

def validate_file(file_path):
    url = "https://validator.w3.org/nu/"
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    
    if response.ok:
        return response.text
    else:
        return "Error occurred while validating the file."

def traverse_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                validation_result = validate_file(file_path)
                soup = BeautifulSoup(validation_result, 'html.parser')
                result_element = soup.find(id='results')
                if result_element:
                    print(f"\nValidation result for {file_path}:")
                    print(result_element.text.strip())



file_path = "CodeInitial"
validation_result = traverse_folder(file_path)
