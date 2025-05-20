# Author: Skyeler Bala
# Course: CS 361 Sotware Engineering 1 
# Assignment: #8
# Description: I am creating a microservice A tester document to test that
# the functionalities of this program work correctly and as intended. 

# import the request library to make HTTP requests
import requests

# function to run test in seperate terminal
def run_test():

    # prompt the user to enter a music format category
    format_choice = input("Enter music format (vinyl, cd, cassette): ").strip().lower()
    # send the get response request to MicroserviceA.py 
    response = requests.get(f'http://localhost:5000/search?format={format_choice}')
    
    # checks is the request was sucessful
    if response.status_code == 200:
        data = response.json() # parses the response
        print("\nSearch Results:")
        for album in data["results"]: # print the album
            print(f"- {album['title']} | {album['price']} | {album['link']}")
    else:
        print(f"Error: {response.json().get('error', 'Unknown error')}") # print an error message if invalid format

# run test when script  is executed
if __name__ == "__main__":
    run_test()
