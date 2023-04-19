Real-time Satellite Location Tracker using Python and MongoDB

This Python code establishes a connection to a MongoDB database and collects real-time data on the location of the International Space Station (ISS) using an API. It then inserts this data into the MongoDB database. The code uses the Python requests library to send a GET request to the API endpoint for the ISS's location. If the request is successful, the response is converted to JSON and inserted into a MongoDB collection.

Prerequisites This code requires the following libraries to be installed:

pymongo 
pandas 
requests 

To install these libraries, you can use pip, the Python package installer. Simply open a command prompt or terminal window and enter the following commands:

pip install pymongo 
pip install pandas 
pip install requests 

Running the Code The code should be run in a Python environment with access to the MongoDB database specified in the connection string.

To run the code, follow these steps:

Open a command prompt or terminal window.

Navigate to the directory containing the Python script.

Enter the following command to run the script:

python satellite_location_tracker.py 

The script will loop through the API request 10800 times, pausing for one second between each request. The location data for the ISS will be inserted into the MongoDB collection specified in the code.

If a connection error occurs, the code will retry the request up to three times before exiting.

Modifying the Code The code can be modified to collect data from other APIs or to insert data into different MongoDB collections.

To modify the code, follow these steps:

Open the Python script in a text editor or integrated development environment (IDE). Modify the variables at the beginning of the script to specify the API endpoint URL, the MongoDB connection string, and the name of the MongoDB collection where the data should be inserted. Modify the loop that sends requests to the API to collect data from a different endpoint or to collect data at a different interval. Save the changes to the script. Follow the steps in the "Running the Code" section to execute the modified script. Conclusion This code demonstrates how to collect real-time data from an API and insert it into a MongoDB database using Python. With some modifications, it can be used to collect and store data from a variety of different sources.