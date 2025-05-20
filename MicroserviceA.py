# Author: Skyeler Bala
# Course: CS 361 Sotware Engineering 1 
# Assignment: #8
# Description: I am creating a microservice A for my teammate Milton Molina.
# This microservice A, is a music collection app that is CLI-style marketplace
# option that searches the web for the album and format in (vinyl, casset, cd etc).
# This microservice also includes the search with a link along with pricing and
# allows the user to pick what format before searching.

# import necessary libraries from flask
from flask import Flask, request, jsonify

# create a flask app 
app = Flask(__name__)

# simulated a mock database of music albums grouped by format
mock_album_data = {
    'vinyl': [
        {"title": "Abbey Road", "link": "https://example.com/abbey-vinyl", "price": "$29.99"},
        {"title": "Thriller", "link": "https://example.com/thriller-vinyl", "price": "$24.99"}
    ],
    'cd': [
        {"title": "Back in Black", "link": "https://example.com/backinblack-cd", "price": "$14.99"},
        {"title": "The Wall", "link": "https://example.com/thewall-cd", "price": "$18.99"}
    ],
    'cassette': [
        {"title": "Purple Rain", "link": "https://example.com/purplerain-cassette", "price": "$9.99"},
        {"title": "Bad", "link": "https://example.com/bad-cassette", "price": "$7.99"}
    ]
}

# define a route that handles GET requests to "/search"
@app.route('/search', methods=['GET'])
def search():
    # get the value of the format parameter from the URL query string
    music_format = request.args.get('format', '').lower()
    # check if the format exists in the mock database
    if music_format in mock_album_data:
        return jsonify({"results": mock_album_data[music_format]}) # return album data as JSON response
    else:
        return jsonify({"error": "Invalid format"}), 400 # return an error response with a bad request

# start the flask web server when script is ran directly
if __name__ == '__main__':
    app.run(port=5000) # runs on localhost: 5000
